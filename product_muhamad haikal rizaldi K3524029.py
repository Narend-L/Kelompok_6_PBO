from abc import ABC, abstractmethod
from interfaces import cakeable, Developable, Toppable

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
    def proses_produksi(self): pass

class RotiManis(Produk, cakeable, Developable, Toppable):
    def adon(self): print(f"[{self.nama}] Mengadon roti manis...")
    def kembangkan(self): print(f"[{self.nama}] Pengembangan roti manis...")
    def panggang(self): print(f"[{self.nama}] Memanggang roti manis...")
    def topping(self): print(f"[{self.nama}] Menambahkan topping roti manis...")

    def proses_produksi(self):
        self.adon(); self.kembangkan(); self.panggang(); self.topping()

class Croissant(Produk, cakeable, Developable, Toppable):
    def adon(self): print(f"[{self.nama}] Adon laminasi croissant...")
    def kembangkan(self): print(f"[{self.nama}] Pengembangan croissant...")
    def panggang(self): print(f"[{self.nama}] Panggang croissant...")
    def topping(self): print(f"[{self.nama}] Tambah butter glaze...")

    def proses_produksi(self):
        self.adon(); self.kembangkan(); self.panggang(); self.topping()

class KueKering(Produk, cakeable, Toppable):
    def __init__(self, nama, kode, bahan_baku, harga_jual):
        super().__init__(nama, kode, bahan_baku, harga_jual)

class ButterCookies(KueKering):
    def adon(self): print(f"[{self.nama}] Aduk adonan butter cookies...")
    def panggang(self): print(f"[{self.nama}] Panggang butter cookies...")
    def topping(self): print(f"[{self.nama}] Tambah hiasan gula...")

    def proses_produksi(self):
        self.adon(); self.panggang(); self.topping()

class Muffin(KueKering, Developable):
    def adon(self): print(f"[{self.nama}] Campur adonan muffin...")
    def kembangkan(self): print(f"[{self.nama}] Diamkan adonan muffin...")
    def panggang(self): print(f"[{self.nama}] Panggang muffin...")
    def topping(self): print(f"[{self.nama}] Tambah choco chips...")

    def proses_produksi(self):
        self.adon(); self.kembangkan(); self.panggang(); self.topping()
