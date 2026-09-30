Index.html
# MR.COFFEE - Website Cafe & Online Ordering

Proyek web sederhana untuk sistem informasi dan pemesanan menu secara *online* di cafe **MR.COFFEE**. Dibuat menggunakan HTML, CSS, dan JavaScript murni (Vanilla JS) sebagai bagian dari tugas/portofolio pemrograman web dasar.

---

## 📌 Fitur Utama

- **Single Page View / Multi-Tab Navigation**: Perpindahan halaman (Home, Menu, Rewards, About Us, Pemesanan) tanpa melakukan *reload* seluruh halaman (*Single Page App* sederhana menggunakan JS).
- **Katalog & Filter Menu**: Menampilkan berbagai kategori menu (Kopi, Jus, Coklat, Snack, Teh) dengan fitur filter.
- **Form Pemesanan & Keranjang**: 
  - Perhitungan total harga secara dinamis.
  - Form validasi input (Nama, Email, Alamat, Metode Pembayaran, Pilihan Pengiriman).
  - Pilihan Add-ons dan persetujuan syarat/ketentuan.
- **Halaman Rewards & Promo**: Informasi promo mingguan dan tautan unduh aplikasi.

---

## 🛠️ Teknologi yang Digunakan

* **HTML5**: Struktur dan elemen halaman web.
* **CSS3**: Penataan tampilan (*layouting* dan *styling*).
* **JavaScript (Vanilla JS)**: Logika pemesanan, filter menu, dan navigasi antarhalaman.

---

## 📂 Struktur Folder

```text
.
├── index.html          # Halaman utama & elemen antarmuka
├── index.css           # Berkas gaya/tampilan
├── index.js            # Berkas logika & interaktivitas JS
└── *.jpg / *.png       # Gambar pendukung menu & assets
```

---

## 🚀 Cara Menjalankan Proyek

1. *Clone* atau *download* repositori ini:
   ```bash
   git clone https://github.com/username-kamu/nama-repo.gith
   ```
2. Buka folder proyek.
3. Buka file `index.html` langsung di *browser* pilihanmu (Double click / Buka dengan Chrome/Edge/Firefox).

---

## 💡 Poin Pembelajaran (Untuk Diskusi Wawancara Magang)

Proyek ini membantu saya memahami konsep dasar *front-end development*, antara lain:
1. Manipulasi DOM (Document Object Model) untuk navigasi halaman dinamis dan keranjang belanja.
2. Penanganan *event handler* di JavaScript (seperti `onclick`, `onsubmit`, dan validasi form).
3. Pengelolaan *form input* dan logika kalkulasi harga secara langsung di sisi klien (*client-side*).

---
Dikembangkan oleh [Marselino Sanjaya] - [Binus University/Computer Science]



Test.py
# Sistem Perpustakaan Digital (Python & SQLite)

Proyek ini adalah aplikasi Manajemen Perpustakaan sederhana berbasis *Command Line Interface* (CLI) yang dibuat menggunakan **Python** dan **Database SQLite**.

Aplikasi ini dirancang untuk mengelola ketersediaan buku, transaksi peminjaman dengan aturan durasi, serta simulasi integrasi layanan pembelian buku melalui API Pihak Ke-3.

---

## 🛠️ Fitur Utama

1. **Lihat Daftar Buku**: Menampilkan seluruh data buku dan jumlah stok yang tersimpan di database.
2. **Cari Buku**: Mencari buku berdasarkan kata kunci judul.
3. **Tambah Buku Baru (Admin)**: Memasukkan data buku dan stok baru secara langsung ke database SQLite.
4. **Pinjam Buku (Anggota)**: 
   * Memproses peminjaman buku dan mengupdate stok secara otomatis.
   * **Aturan Bisnis**: Peminjaman maksimal **7 hari (1 minggu)**. Peminjaman di atas 7 hari akan ditolak oleh sistem.
5. **Fitur Beli Buku (API Pihak Ke-3)**: Simulasi panggilan *API Gateway* eksternal (Status: `503 Service Unavailable / In Development`).

---

## 👥 Aktor Sistem & Hak Akses

* **Anggota / Mahasiswa**: Dapat melihat daftar buku, mencari buku, dan meminjam buku.
* **Admin Perpustakaan**: Dapat menginput/menambah buku baru ke dalam database.
* **API Gateway (Pihak Ke-3)**: Layanan luar untuk penanganan pembelian buku baru.

---

## 🗄️ Struktur Database (`perpustakaan.db`)

Sistem menggunakan database lokal **SQLite** dengan tabel utama `buku`:

| Nama Kolom | Tipe Data | Keterangan |
| :--- | :--- | :--- |
| `id` | INTEGER | ID Unik Buku (Primary Key, Auto Increment) |
| `judul` | TEXT | Judul Buku |
| `penulis` | TEXT | Nama Penulis Buku |
| `stok` | INTEGER | Jumlah Stok Buku Tersedia |

---

## 🚀 Cara Menjalankan Program (VS Code)

1. Pastikan **Python 3.x** sudah terinstall di komputer.
2. Buka folder proyek di **VS Code**.
3. Jalankan program melalui terminal:
   ```bash
   python Test.py



