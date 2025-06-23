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
