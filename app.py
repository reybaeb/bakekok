import os
import zipfile
import fitz  # PyMuPDF
from flask import Flask, flash, redirect, render_template, request, send_file, url_for
from werkzeug.utils import secure_filename
import uuid
from PIL import Image
import tempfile
import shutil
import io

app = Flask(__name__)
app = Flask(__name__)
# Generate a random secret key if not provided in environment (better than static default)
app.secret_key = os.getenv("secret_key") or os.urandom(24)

# Define allowed extensions for each file type
ALLOWED_EXTENSIONS = {
    "image": {"jpg", "jpeg", "png", "gif"},
    "document": {"pdf"},
    "archive": {"zip"},
}

# Create directories if they don't exist
for folder in ["uploads", "compressed"]:
    for subfolder in ["images", "documents", "archives"]:
        os.makedirs(os.path.join(folder, subfolder), exist_ok=True)

def allowed_file(filename, file_type):
    """Check if the file extension is allowed for the given file type."""
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS[file_type]
    )

def compress_image(input_path, output_path, quality=85):
    """Compress an image file."""
    try:
        with Image.open(input_path) as img:
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            img.save(output_path, optimize=True, quality=quality)
        return True
    except Exception as e:
        app.logger.error(f"Image compression error: {e}")
        return str(e)

def compress_pdf(input_path, output_path, aggressive=False):
    """Compress a PDF file. If aggressive, also compress images inside."""
    try:
        doc = fitz.open(input_path)
        if aggressive:
            # Aggressive compression: find and compress images
            for page_num in range(len(doc)):
                page = doc[page_num]
                img_list = page.get_images(full=True)
                for img_index, img in enumerate(img_list):
                    xref = img[0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    
                    # Use Pillow to re-compress the image
                    try:
                        pil_img = Image.open(io.BytesIO(image_bytes))
                        if pil_img.mode in ("RGBA", "P"):
                            pil_img = pil_img.convert("RGB")
                        
                        output_buffer = io.BytesIO()
                        pil_img.save(output_buffer, format="JPEG", quality=75) # Aggressive quality
                        new_image_bytes = output_buffer.getvalue()

                        # Update the image in the PDF
                        doc.update_image(xref, stream=new_image_bytes)
                    except Exception:
                        continue # Skip if image can't be processed

        # Save with optimization flags
        doc.save(output_path, garbage=4, deflate=True, clean=True)
        doc.close()
        return True
    except Exception as e:
        app.logger.error(f"PDF compression error: {e}")
        return str(e)

def compress_zip(input_path, output_path, aggressive=False):
    """Re-compress a ZIP file. If aggressive, compress images inside."""
    if not aggressive:
        # Standard ZIP compression
        try:
            with zipfile.ZipFile(input_path, 'r') as zip_in:
                with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zip_out:
                    for item in zip_in.infolist():
                        buffer = zip_in.read(item.filename)
                        zip_out.writestr(item, buffer)
            return True
        except Exception as e:
            app.logger.error(f"ZIP compression error: {e}")
            return str(e)
    else:
        # Aggressive ZIP compression
        temp_dir = tempfile.mkdtemp()
        try:
            with zipfile.ZipFile(input_path, 'r') as zip_in:
                zip_in.extractall(temp_dir)
            
            for root, _, files in os.walk(temp_dir):
                for name in files:
                    file_path = os.path.join(root, name)
                    if name.lower().endswith(('.png', '.jpg', '.jpeg')):
                        # Use our image compressor
                        compress_image(file_path, file_path, quality=75)
            
            # Create a new zip from the compressed files
            shutil.make_archive(output_path.replace('.zip', ''), 'zip', temp_dir)
            return True
        except Exception as e:
            app.logger.error(f"Aggressive ZIP compression error: {e}")
            return str(e)
        finally:
            shutil.rmtree(temp_dir)

@app.route("/", methods=["GET", "POST"])
def compressor_route():
    if request.method == "POST":
        compression_type = request.form.get("compression_type")
        uploaded_file = request.files.get("file")
        aggressive_mode = request.form.get("aggressive") == "true"

        if not uploaded_file or uploaded_file.filename == "":
            flash("Tidak ada file yang dipilih.", "error")
            return redirect(request.url)

        if not compression_type:
            flash("Silakan pilih jenis kompresi.", "error")
            return redirect(request.url)
            
        if not allowed_file(uploaded_file.filename, compression_type):
            flash(f"Jenis file tidak valid untuk kompresi '{compression_type}'. Yang diizinkan: {', '.join(ALLOWED_EXTENSIONS[compression_type])}", "error")
            return redirect(request.url)
            
        # Secure the filename to prevent path traversal
        original_filename = secure_filename(uploaded_file.filename)
        # Add UUID to prevent filename collisions
        filename = f"{uuid.uuid4().hex}_{original_filename}"
        
        type_folder_map = {
            "image": "images",
            "document": "documents",
            "archive": "archives"
        }
        subfolder = type_folder_map.get(compression_type)

        # Ensure directories exist (redundant with startup check but safe)
        os.makedirs(os.path.join("uploads", subfolder), exist_ok=True)
        os.makedirs(os.path.join("compressed", subfolder), exist_ok=True)

        input_path = os.path.join("uploads", subfolder, filename)
        output_path = os.path.join("compressed", subfolder, filename)
        
        uploaded_file.save(input_path)
        
        compression_function_map = {
            "image": compress_image,
            "document": compress_pdf,
            "archive": compress_zip
        }
        
        compress_func = compression_function_map.get(compression_type)
        
        # Pass aggressive flag to PDF/ZIP functions
        if compression_type in ["document", "archive"]:
            compression_result = compress_func(input_path, output_path, aggressive=aggressive_mode)
        else:
            compression_result = compress_func(input_path, output_path)

        if compression_result is True:
            flash("File berhasil dikompres!", "success")
            return redirect(url_for("download_compressed", file_type=subfolder, filename=filename))
        else:
            flash(f"Kesalahan Kompresi: {compression_result}", "error")
            return redirect(request.url)

    return render_template("index.html")

@app.route("/download/<file_type>/<filename>")
def download_compressed(file_type, filename):
    """Download the compressed file from the correct subfolder."""
    path = os.path.join("compressed", file_type, filename)
    if not os.path.exists(path):
        flash("Tidak dapat menemukan file terkompresi untuk diunduh.", "error")
        return redirect(url_for('compressor_route'))
    return send_file(path, as_attachment=True)

@app.route("/manual")
def manual():
    """Render the user guide page."""
    return render_template("manual.html")

if __name__ == "__main__":
    app.run(debug=True) 