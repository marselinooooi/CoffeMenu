import sqlite3
import os

# ==========================================
# 1. INTEGRASI & INISIALISASI DATABASE
# ==========================================
DB_NAME = "perpustakaan.db"

def init_db():
    """Membuat koneksi ke SQLite dan menyiapkan tabel serta data awal."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Buat tabel buku jika belum ada
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS buku (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            judul TEXT NOT NULL,
            penulis TEXT NOT NULL,
            stok INTEGER NOT NULL
        )
    ''')
    
    # Cek apakah tabel masih kosong. Jika kosong, isi data default.
    cursor.execute("SELECT COUNT(*) FROM buku")
    if cursor.fetchone()[0] == 0:
        buku_awal = [
            ("Laskar Pelangi", "Andrea Hirata", 3),
            ("Bumi Manusia", "Pramoedya Ananta Toer", 1),
            ("Pemrograman Python RPL", "Dr. Budi", 2)
        ]
        cursor.executemany("INSERT INTO buku (judul, penulis, stok) VALUES (?, ?, ?)", buku_awal)
        conn.commit()
        print("[DATABASE] Berhasil menginisialisasi tabel 'buku' dengan data awal.")
    
    conn.close()

# ==========================================
# 2. LOGIKA OPERASI DATABASE (CRUD)
# ==========================================
def dapatkan_semua_buku():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, judul, penulis, stok FROM buku")
    hasil = cursor.fetchall()
    conn.close()
    return hasil

def cari_buku_by_judul(judul):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, judul, penulis, stok FROM buku WHERE LOWER(judul) LIKE LOWER(?)", (f"%{judul}%",))
    hasil = cursor.fetchall()
    conn.close()
    return hasil

def tambah_buku_baru(judul, penulis, stok):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO buku (judul, penulis, stok) VALUES (?, ?, ?)", (judul, penulis, stok))
    conn.commit()
    conn.close()

def update_stok_buku(buku_id, stok_baru):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE buku SET stok = ? WHERE id = ?", (stok_baru, buku_id))
    conn.commit()
    conn.close()

# ==========================================
# 3. INTERFACE CLI (MENU UTAMA)
# ==========================================
def jalankan_sistem():
    init_db()
    
    while True:
        print("\n" + "="*45)
        print("  SISTEM PERPUSTAKAAN DIGITAL (SQLITE DB)  ")
        print("="*45)
        print("1. Lihat Semua Buku")
        print("2. Cari Buku")
        print("3. Tambah Buku Baru (Input User Admin)")
        print("4. Pinjam Buku")
        print("5. Fitur Beli Buku (Third-Party API)")
        print("6. Keluar")
        
        pilihan = input("\nPilih menu (1-6): ").strip()
        
        if pilihan == "1":
            buku_list = dapatkan_semua_buku()
            print("\n--- DAFTAR BUKU TERSEDIA ---")
            print(f"{'ID':<4} | {'Judul Buku':<25} | {'Penulis':<20} | {'Stok':<5}")
            print("-" * 60)
            for b in buku_list:
                print(f"{b[0]:<4} | {b[1]:<25} | {b[2]:<20} | {b[3]:<5}")
                
        elif pilihan == "2":
            query = input("Masukkan judul buku yang dicari: ").strip()
            hasil = cari_buku_by_judul(query)
            if hasil:
                print("\n--- HASIL PENCARIAN ---")
                for b in hasil:
                    print(f"ID: {b[0]} | Judul: {b[1]} | Penulis: {b[2]} | Stok: {b[3]}")
            else:
                print("❌ Buku tidak ditemukan di database.")
                
        elif pilihan == "3":
            print("\n--- INPUT BUKU BARU KE DATABASE ---")
            judul = input("Masukkan Judul Buku: ").strip()
            penulis = input("Masukkan Nama Penulis: ").strip()
            try:
                stok = int(input("Masukkan Jumlah Stok: "))
                if stok < 1:
                    print("❌ Stok harus lebih dari 0.")
                    continue
                tambah_buku_baru(judul, penulis, stok)
                print(f"✅ Buku '{judul}' berhasil disimpan ke database SQLite!")
            except ValueError:
                print("❌ Input stok harus berupa angka integer!")

        elif pilihan == "4":
            print("\n--- PROSES PINJAM BUKU ---")
            query = input("Masukkan nama/ID buku yang ingin dipinjam: ").strip()
            
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            if query.isdigit():
                cursor.execute("SELECT id, judul, stok FROM buku WHERE id = ?", (int(query),))
            else:
                cursor.execute("SELECT id, judul, stok FROM buku WHERE LOWER(judul) = LOWER(?)", (query,))
            buku = cursor.fetchone()
            conn.close()

            if not buku:
                print("❌ Buku tidak ditemukan.")
                continue

            buku_id, judul, stok = buku[0], buku[1], buku[2]
            
            if stok <= 0:
                print(f"❌ Stok buku '{judul}' habis!")
                continue

            try:
                durasi = int(input("Masukkan durasi peminjaman (hari): "))
                if durasi > 7:
                    print("❌ GAGAL: Batas maksimal peminjaman adalah 7 hari (1 minggu).")
                    print("   Pengajuan ditolak oleh Aturan Bisnis Perpustakaan.")
                else:
                    update_stok_buku(buku_id, stok - 1)
                    print(f"✅ BERHASIL: Buku '{judul}' dipinjam selama {durasi} hari.")
                    print(f"   Stok tersisa di DB: {stok - 1}")
            except ValueError:
                print("❌ Input durasi harus berupa angka!")

        elif pilihan == "5":
            print("\n--- MOCK THIRD-PARTY PROCUREMENT API ---")
            print("Connecting to API Gateway...")
            print("Status Code: 503 Service Unavailable")
            print("Message: [IN DEVELOPMENT] Fitur pembelian buku lewat pihak ke-3 belum aktif.")

        elif pilihan == "6":
            print("Terima kasih telah menggunakan sistem perpustakaan.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    jalankan_sistem()