#Naren
from abc import ABC, abstractmethod

# -------------------- Interface Produksi --------------------
class cakeable(ABC):
    @abstractmethod
    def adon(self): pass

    @abstractmethod
    def panggang(self): pass

class Developable(ABC):
    @abstractmethod
    def kembangkan(self): pass

class Toppable(ABC):
    @abstractmethod
    def topping(self): pass

# -------------------- Kelas Abstrak Produk --------------------
class Produk(ABC):
    def __init__(self, nama, kode, bahan_baku, harga_jual):
        self.nama = nama
        self.kode = kode
        self.bahan_baku = bahan_baku  # dict: {nama_bahan: {"jumlah": int, "harga_per_unit": int}}
        self.harga_jual = harga_jual
        self.biaya_produksi = self.hitung_biaya_produksi()

    def hitung_biaya_produksi(self):
        return sum(info["jumlah"] * info["harga_per_unit"] for info in self.bahan_baku.values())

    def estimasi_profit(self, jumlah):
        total_jual = self.harga_jual * jumlah
        total_biaya = self.biaya_produksi * jumlah
        return total_jual - total_biaya

    def jenis_produk(self):
        return self.__class__.__name__

    @abstractmethod
    def proses_produksi(self): pass

# -------------------- Implementasi Produk --------------------
class RotiManis(Produk, cakeable, Developable, Toppable):
    def __init__(self, nama, kode, bahan_baku, harga_jual):
        super().__init__(nama, kode, bahan_baku, harga_jual)

    def adon(self): print(f"[{self.nama}] Mengadon roti manis...")
    def kembangkan(self): print(f"[{self.nama}] pengembangan roti manis...")
    def panggang(self): print(f"[{self.nama}] Memanggang roti manis...")
    def topping(self): print(f"[{self.nama}] Menambahkan topping roti manis...")

    def proses_produksi(self):
        self.adon()
        self.kembangkan()
        self.panggang()
        self.topping()

class Croissant(Produk, cakeable, Developable, Toppable):
    def __init__(self, nama, kode, bahan_baku, harga_jual):
        super().__init__(nama, kode, bahan_baku, harga_jual)

    def adon(self): print(f"[{self.nama}] Adon laminasi croissant...")
    def kembangkan(self): print(f"[{self.nama}] pengembangan croissant...")
    def panggang(self): print(f"[{self.nama}] Panggang croissant...")
    def topping(self): print(f"[{self.nama}] Tambah butter glaze...")

    def proses_produksi(self):
        self.adon()
        self.kembangkan()
        self.panggang()
        self.topping()

# -------------------- Superclass Kue Kering --------------------
class KueKering(Produk, cakeable, Toppable):
    def __init__(self, nama, kode, bahan_baku, harga_jual):
        super().__init__(nama, kode, bahan_baku, harga_jual)

# -------------------- Turunan Kue Kering --------------------
class ButterCookies(KueKering):
    def adon(self): print(f"[{self.nama}] Aduk adonan butter cookies...")
    def panggang(self): print(f"[{self.nama}] Panggang butter cookies...")
    def topping(self): print(f"[{self.nama}] Tambah hiasan gula...")

    def proses_produksi(self):
        self.adon()
        self.panggang()
        self.topping()

class Muffin(KueKering, Developable):
    def adon(self): print(f"[{self.nama}] Campur adonan muffin...")
    def kembangkan(self): print(f"[{self.nama}] Diamkan adonan muffin...")
    def panggang(self): print(f"[{self.nama}] Panggang muffin...")
    def topping(self): print(f"[{self.nama}] Tambah choco chips...")

    def proses_produksi(self):
        self.adon()
        self.kembangkan()
        self.panggang()
        self.topping()
#ALAN
# -------------------- Manajemen Produk --------------------
class ManajemenProduk:
    def __init__(self):
        self.daftar_produk = []

    def tambah_produk(self, produk: Produk):
        if any(p.kode == produk.kode for p in self.daftar_produk):
            print(f"Produk dengan kode {produk.kode} sudah ada.")
        else:
            self.daftar_produk.append(produk)
            print(f"Produk '{produk.nama}' berhasil ditambahkan.")

    def tampilkan_produk(self):
        if not self.daftar_produk:
            print("Belum ada produk yang ditambahkan.")
            return
        print("\nDaftar Produk:")
        for p in self.daftar_produk:
            print(f"{p.kode} - {p.nama} ({p.jenis_produk()}) | Biaya: Rp{p.biaya_produksi:,} | Harga Jual: Rp{p.harga_jual:,}")

    def estimasi_profit(self, kode, jumlah):
        for p in self.daftar_produk:
            if p.kode == kode:
                profit = p.estimasi_profit(jumlah)
                print(f"Estimasi profit untuk {jumlah} pcs {p.nama}: Rp{profit:,.0f}")
                return
        print("Produk tidak ditemukan.")

    def simulasi_produksi(self, kode):
        for p in self.daftar_produk:
            if p.kode == kode:
                print(f"\nSimulasi produksi untuk {p.nama} ({p.jenis_produk()}):")
                print("Langkah-langkah produksi:")

                langkah = 1
                if isinstance(p, cakeable):
                    print(f"{langkah}. Pengadonan    ➜ ", end=""); p.adon(); langkah += 1
                if isinstance(p, Developable):
                    print(f"{langkah}. Pengembangan  ➜ ", end=""); p.kembangkan(); langkah += 1
                if isinstance(p, cakeable):
                    print(f"{langkah}. Pemanggangan  ➜ ", end=""); p.panggang(); langkah += 1
                if isinstance(p, Toppable):
                    print(f"{langkah}. Topping       ➜ ", end=""); p.topping()
                return
        print("Produk tidak ditemukan.")
#ALDI
# -------------------- Tambah Produk dari Input --------------------
def input_produk_baru(manajer: ManajemenProduk):
    print("\n--- Tambah Produk Baru ---")
    nama = input("Nama produk: ")
    kode = input("Kode produk (unik): ")
    jenis = input("Jenis produk (RotiManis/Croissant/ButterCookies/Muffin): ").strip().lower()

    bahan_baku = {}
    while True:
        bahan = input("Nama bahan (ketik 'selesai' untuk berhenti): ")
        if bahan.lower() == 'selesai':
            break
        try:
            jumlah = int(input(f"Jumlah {bahan}: "))
            harga_per_unit = int(input(f"Harga per satuan {bahan}: "))
            if jumlah <= 0 or harga_per_unit <= 0:
                print("Jumlah dan harga harus lebih dari 0.")
                continue
            bahan_baku[bahan] = {"jumlah": jumlah, "harga_per_unit": harga_per_unit}
        except ValueError:
            print("Input jumlah dan harga harus berupa angka.")

    try:
        harga = int(input("Harga jual per pcs (Rp): "))
        if harga <= 0:
            print("Harga jual harus lebih dari 0.")
            return
    except ValueError:
        print("Harga jual harus angka.")
        return

    if jenis == "rotimanis":
        produk = RotiManis(nama, kode, bahan_baku, harga)
    elif jenis == "croissant":
        produk = Croissant(nama, kode, bahan_baku, harga)
    elif jenis == "buttercookies":
        produk = ButterCookies(nama, kode, bahan_baku, harga)
    elif jenis == "muffin":
        produk = Muffin(nama, kode, bahan_baku, harga)
    else:
        print("Jenis produk tidak dikenali.")
        return

    manajer.tambah_produk(produk)

#MAUL
# -------------------- Menu Utama --------------------
def menu():
    manajer = ManajemenProduk()

    

    while True:
        print("\n--- Hanari Bakery Menu ---")
        print("1. Tambah Produk Baru")
        print("2. Tampilkan Semua Produk")
        print("3. Estimasi Profit")
        print("4. Simulasi Proses Produksi")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            input_produk_baru(manajer)
        elif pilihan == "2":
            manajer.tampilkan_produk()
        elif pilihan == "3":
            kode = input("Masukkan kode produk: ")
            try:
                jumlah = int(input("Masukkan jumlah pcs: "))
                if jumlah <= 0:
                    print("Jumlah harus positif.")
                    continue
            except ValueError:
                print("Input jumlah harus angka.")
                continue
            manajer.estimasi_profit(kode, jumlah)
        elif pilihan == "4":
            kode = input("Masukkan kode produk: ")
            manajer.simulasi_produksi(kode)
        elif pilihan == "5":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid.")

# -------------------- Eksekusi --------------------
if __name__ == "__main__":
    menu()
