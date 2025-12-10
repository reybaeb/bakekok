# Helper script untuk menjalankan aplikasi lokal dengan mudah
$ErrorActionPreference = "Stop"

Write-Host "🚀 Menyiapkan lingkungan..." -ForegroundColor Cyan

# Cek apakah virtual environment ada
if (-not (Test-Path ".venv")) {
    Write-Host "Virtual environment tidak ditemukan. Membuat..." -ForegroundColor Yellow
    python -m venv .venv
}

# Install dependencies jika belum
Write-Host "📦 Memastikan dependencies terinstall..." -ForegroundColor Cyan
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt | Out-Null

# Jalankan Flask
Write-Host "🔥 Menjalankan Server Flask..." -ForegroundColor Green
Write-Host "Kunjungi: http://127.0.0.1:5000" -ForegroundColor Green
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"
& ".\.venv\Scripts\python.exe" -m flask run
