# Bakekok - Universal File Compressor

## Deskripsi

Aplikasi web modern untuk mengompres **Gambar**, **PDF**, dan **ZIP** secara efisien. Dibangun dengan Python (Flask) dengan antarmuka **Modern Bauhaus** yang unik dan responsif.

## Fitur Unggulan

- 🎨 **Modern Bauhaus UI**: Desain antarmuka unik, bersih, dan estetik.
- ⚡ **Multi-Format**: Dukungan kompresi untuk Image (JPG/PNG), Dokumen (PDF), dan Arsip (ZIP).
- 🛡️ **Aman**: Dilengkapi sanitasi nama file dan perlindungan path traversal.
- 🚀 **Mode Agresif**: Opsi kompresi tinggi untuk mengecilkan ukuran file secara ekstrim.

## Cara Menjalankan (Windows)

Cara termudah dan anti-gagal adalah menggunakan script helper yang telah disediakan.

### Prasyarat

- Pastikan **Python 3.9+** sudah terinstall di komputer Anda.

### Langkah Cepat

1. Buka terminal di folder ini.
2. Jalankan perintah berikut:
   ```powershell
   .\run_local.ps1
   ```
   _(Script ini otomatis membuat virtual environment, install dependensi, dan menjalankan server)_
3. Buka browser dan kunjungi: **http://127.0.0.1:5000**

## Cara Menjalankan dengan Docker (Opsional)

Jika Anda memiliki Docker terinstall:

```bash
docker-compose up --build
```

## Teknologi

- **Backend**: Flask, Pillow, PyMuPDF
- **Frontend**: HTML5, Modern CSS (Bauhaus Theme)
- **Infrastructure**: Docker
