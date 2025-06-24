from abc import ABC, abstractmethod

class cakeable(ABC):
    @abstractmethod
    def adon(self): 
        pass

    @abstractmethod
    def panggang(self):
        pass

class Developable(ABC):
    @abstractmethod
    def kembangkan(self): 
        pass

class Toppable(ABC):
    @abstractmethod
    def topping(self): 
        pass


class Produk(ABC):
    def __init__(self, nama, kode, bahan_baku, harga_jual):
        self.nama = nama
        self.kode = kode
        self.bahan_baku = bahan_baku  
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
    def proses_produksi(self):
        pass

class KueKering(Produk, cakeable, Toppable):
    def __init__(self, nama, kode, bahan_baku, harga_jual):
        super().__init__(nama, kode, bahan_baku, harga_jual)


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
                print(f"\nSimulasi proses :")
                jenis = p.__class__.__name__.lower()
                if jenis == "rotimanis":
                    print(f"{p.nama} > RotiManis = Pengadonan, Pengembangan, Pemanggangan")
                elif jenis == "croissant":
                    print(f"{p.nama} > Croissant = Pengadonan, Pengembangan, Pemanggangan")
                elif jenis == "muffin":
                    print(f"{p.nama} > Muffin = Pengadonan, Pengembangan, Pemanggangan, Topping")
                elif jenis == "buttercookies":
                    print(f"{p.nama} > ButterCookies = Pengadonan, Pemanggangan, Topping")
                else:
                    print("Jenis produk tidak dikenali.")
                return
        print("Produk tidak ditemukan.")