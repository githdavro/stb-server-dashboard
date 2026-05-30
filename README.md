<div align="center">

# STB Server Dashboard

### Monitoring realtime untuk STB Armbian yang mendapat kehidupan kedua sebagai server.

<img src="./preview.png" alt="Dashboard Preview" width="100%">

<br>

Lightweight • Realtime • Browser-Based • Armbian Linux

</div>

---

## Tentang Project

STB Server Dashboard adalah dashboard monitoring sederhana yang dibuat untuk perangkat STB yang menjalankan Armbian Linux.

Project ini berawal dari rasa penasaran saat mengubah STB bekas menjadi server rumahan. Setelah beberapa layanan berjalan di atasnya, muncul kebutuhan untuk memantau kondisi perangkat dengan cepat tanpa harus terus-menerus membuka beberapa utilitas monitoring secara terpisah.

Semua informasi yang ditampilkan sebenarnya sudah tersedia melalui command line Linux dan file sistem seperti `/proc` maupun `/sys`.

Dashboard ini tidak dibuat untuk menggantikan command line.

Tujuannya adalah menyajikan informasi penting dalam satu tampilan yang ringkas, visual, dan mudah diakses dari browser, baik melalui desktop maupun perangkat mobile.

---

## Fitur

* Monitoring CPU secara realtime
* Informasi jumlah core CPU
* Deteksi frekuensi CPU
* Monitoring penggunaan RAM
* Monitoring penggunaan storage
* Informasi sisa kapasitas penyimpanan
* Monitoring suhu perangkat
* Informasi uptime sistem
* Status konektivitas node
* Responsive layout
* Material You inspired interface
* Android-style ripple interaction
* Automatic refresh
* Visibility-aware polling
* Offline fallback mode

---

## Apa yang Ditampilkan?

```text
CPU Usage
CPU Frequency
CPU Cores

RAM Usage

Storage Usage
Available Storage

Temperature

System Uptime

Node Status
```

---

## Arsitektur

```text
┌──────────────────┐
│     Browser      │
│  Dashboard UI    │
└────────┬─────────┘
         │
         │ GET /api/status
         │
┌────────▼─────────┐
│      app.py      │
│ Python HTTP API  │
└────────┬─────────┘
         │
         ├── /proc/meminfo
         ├── /proc/cpuinfo
         ├── /proc/uptime
         ├── os.statvfs()
         └── thermal_zone0
```

---

## Struktur Project

```text
.
├── app.py
├── index.html
├── preview.png
└── README.md
```

---

## Teknologi yang Digunakan

| Komponen | Teknologi               |
| -------- | ----------------------- |
| Frontend | HTML                    |
| Styling  | Tailwind CSS            |
| Logic    | Vanilla JavaScript      |
| Backend  | Python Standard Library |
| API      | HTTPServer              |
| Platform | Armbian Linux           |

---

## Menjalankan Project

Clone repository:

```bash
git clone https://github.com/username/stb-server-dashboard.git
cd stb-server-dashboard
```

Jalankan backend:

```bash
python3 app.py
```

Kemudian buka browser dan akses:

```text
http://IP_SERVER:5000
```

Atur nilai `API_URL` pada frontend apabila dashboard dan backend dijalankan pada host yang berbeda.

---

## Kenapa Tidak Pakai Framework?

Project ini sengaja dibuat sesederhana mungkin.

Backend hanya menggunakan Python Standard Library melalui `http.server`.

Frontend menggunakan HTML, Tailwind CDN, dan Vanilla JavaScript.

Pendekatan ini membuat project tetap ringan, mudah dipahami, dan mudah dijalankan pada perangkat dengan spesifikasi terbatas seperti STB berbasis Armbian.

---

## Kenapa Membuat Dashboard Jika Sudah Ada CLI?

Karena keduanya punya tujuan yang berbeda.

Command line tetap menjadi cara paling fleksibel dan powerful untuk melakukan monitoring sistem Linux.

Namun dashboard memberikan tampilan visual yang lebih cepat dipahami dalam sekali lihat.

Saat server berjalan terus-menerus di rumah atau di jaringan lokal, membuka satu halaman dashboard sering kali lebih praktis dibanding membuka beberapa utilitas monitoring secara terpisah.

Project ini lebih merupakan eksperimen dan sarana belajar membangun monitoring dashboard ringan daripada mencoba menggantikan workflow berbasis terminal.

---

## Hardware Target

Project ini dikembangkan dan diuji pada perangkat STB yang menjalankan Armbian Linux.

Meskipun dibuat untuk perangkat kelas bawah, dashboard tetap dapat digunakan pada mini PC, SBC, VPS, maupun server Linux lainnya selama informasi sistem tersedia melalui antarmuka Linux standar.

---

## Catatan

Tidak ada database.

Tidak ada framework frontend.

Tidak ada dependency backend tambahan.

Hanya Python, HTML, JavaScript, dan sebuah STB yang menolak pensiun.

---

## License

MIT License
