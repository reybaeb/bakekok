[![codecov](https://codecov.io/gh/k1lgor/image-compressor/branch/master/graph/badge.svg?token=OWVSAGHDPL)](https://codecov.io/gh/k1lgor/image-compressor)

# Aplikasi Web Kompresi Gambar

Aplikasi Web Kompresi Gambar adalah aplikasi berbasis Flask yang memungkinkan pengguna untuk mengunggah gambar dan mengompresnya tanpa mengurangi kualitas secara signifikan. Aplikasi ini cocok untuk menghemat ruang penyimpanan dan mempercepat proses upload gambar di berbagai platform.

## Fitur Utama
- **Unggah Gambar:** Pengguna dapat mengunggah gambar dari perangkat mereka.
- **Kompresi Otomatis:** Gambar yang diunggah akan dikompresi secara otomatis dengan tetap menjaga kualitas.
- **Unduh Gambar:** Setelah proses kompresi, pengguna dapat langsung mengunduh gambar hasil kompresi.
- **Antarmuka Sederhana:** Tampilan web yang mudah digunakan dan responsif.
- **Notifikasi Error:** Menampilkan pesan jika format gambar tidak didukung atau terjadi kegagalan kompresi.

## Cara Menjalankan Aplikasi

### Prasyarat
- Python 3.6 atau lebih baru
- Flask
- Pillow (Python Imaging Library)

### Instalasi
1. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan aplikasi Flask:
   ```bash
   flask run
   ```
3. Buka browser dan akses `http://localhost:5000`

### Menggunakan Docker
1. Pastikan Docker dan Docker Compose sudah terpasang.
2. Build image dan jalankan:
   ```bash
   docker-compose up -d
   ```
3. Akses aplikasi di `http://localhost:5000`

## Struktur Folder Penting
- `uploads/` : Menyimpan file gambar yang diunggah oleh pengguna.
- `templates/` : Berisi file HTML untuk tampilan web.

## Lisensi
Proyek ini menggunakan lisensi MIT. Lihat file [LICENSE](./LICENSE) untuk detail.

## Code Coverage

For detailed code coverage information, see the [Code Coverage Report](./README_COVERAGE.md).
