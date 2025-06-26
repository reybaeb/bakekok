[![codecov](https://codecov.io/gh/k1lgor/image-compressor/branch/master/graph/badge.svg?token=OWVSAGHDPL)](https://codecov.io/gh/k1lgor/image-compressor)

# Aplikasi Web Kompresi Gambar

## Deskripsi
Aplikasi ini adalah web sederhana untuk mengompres gambar secara otomatis, dibangun menggunakan framework Flask (Python). Pengguna dapat mengunggah gambar, mengompresnya, dan mengunduh hasil kompresi dengan mudah melalui antarmuka web yang intuitif.

## Bahasa & Teknologi yang Digunakan
- **Python 3.6+**
- **Flask** (web framework)
- **Pillow (PIL)** untuk pengolahan gambar
- **HTML, CSS** (Jinja2 Template bawaan Flask)
- **Docker** (opsional, untuk deployment)

## Fitur Utama
- Upload gambar dari perangkat pengguna
- Kompresi otomatis gambar dengan menjaga kualitas
- Download hasil kompresi
- Notifikasi jika format gambar tidak didukung atau terjadi error
- Antarmuka web sederhana dan responsif

## Cara Instalasi & Menjalankan
1. **Clone repository:**
   ```bash
   git clone https://github.com/USERNAME/REPO.git
   cd REPO
   ```
2. **Install dependensi:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Jalankan aplikasi:**
   ```bash
   flask run
   ```
4. **Akses di browser:**
   Buka `http://localhost:5000`

### Menjalankan dengan Docker (Opsional)
1. Build dan jalankan:
   ```bash
   docker-compose up -d
   ```
2. Akses aplikasi di `http://localhost:5000`

## Struktur Folder Penting
- `uploads/` : Menyimpan file gambar yang diunggah oleh pengguna
- `templates/` : Berisi file HTML untuk tampilan web
