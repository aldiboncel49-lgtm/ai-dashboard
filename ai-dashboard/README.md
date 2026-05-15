# 🤖 AI Dashboard — Laporan Perusahaan

Dashboard berbasis web untuk menganalisis teks bisnis (laporan, email, dokumen) menggunakan **Claude AI** dari Anthropic. Menampilkan sentimen, risiko, topik utama, dan action items secara otomatis.

---

## ✨ Fitur

- 🔍 **Analisis Teks AI** — Masukkan teks bisnis, dapatkan ringkasan, sentimen, dan insight instan
- 📊 **Dashboard Statistik** — Lihat distribusi sentimen dan tren risiko dari semua analisis
- 📋 **Action Items Otomatis** — AI mengekstrak langkah-langkah yang perlu diambil
- 🕑 **Riwayat Analisis** — Semua hasil tersimpan lokal dalam JSON
- 📈 **Grafik Tren** — Visualisasi skor sentimen 7 analisis terakhir

---

## 🚀 Cara Menjalankan

### 1. Clone Repositori
```bash
git clone https://github.com/aldiboncel49-lgtm/ai-dashboard.git
cd ai-dashboard
```

### 2. Buat Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install Dependensi
```bash
pip install -r requirements.txt
```

### 4. Konfigurasi API Key
```bash
cp .env.example .env
# Edit .env dan isi ANTHROPIC_API_KEY dengan API key kamu
# Dapatkan API key di: https://console.anthropic.com
```

### 5. Jalankan Aplikasi
```bash
python app.py
```

Buka browser: **http://localhost:5000**

---

## 🗂️ Struktur Proyek

```
ai-dashboard/
├── app.py                  # Entry point Flask
├── src/
│   ├── ai_analyzer.py      # Modul analisis AI (Claude)
│   └── report_generator.py # Modul pembuatan laporan
├── templates/
│   └── index.html          # UI Dashboard
├── data/                   # Riwayat analisis (auto-generated)
├── tests/
│   └── test_report.py      # Unit tests
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## 🧪 Menjalankan Tests
```bash
python -m pytest tests/
```

---

## 🛠️ Tech Stack

| Teknologi | Fungsi |
|-----------|--------|
| Python 3.10+ | Backend |
| Flask | Web Framework |
| Anthropic SDK | Claude AI |
| HTML/CSS/JS | Frontend Dashboard |

---

## 📄 Lisensi

MIT License — bebas digunakan dan dimodifikasi.
