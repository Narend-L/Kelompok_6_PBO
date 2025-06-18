from abc import ABC, abstractmethod

class Karyawan(ABC):
    def __init__(self, nama_karyawan, kode_karyawan, posisi, masa_kerja, gender):
        self.nama_karyawan = nama_karyawan
        self.kode_karyawan = kode_karyawan
        self.posisi = posisi
        self.masa_kerja = masa_kerja
        self.gender = gender

    @abstractmethod
    def gaji_pokok(self):
        pass

    def tunjangan(self):
        return self.gaji_pokok() * 0.1 if self.gender == "L" else 0

    def insentif(self):
        if self.posisi == "ceo":
            return 0 
        else:
            return self.gaji_pokok() * (0.2 if self.masa_kerja < 10 else 0.4)

    @abstractmethod
    def total_gaji(self):
        pass

    def info(self):
        return (f"Nama Karyawan: {self.nama_karyawan}, "
                f"Kode Karyawan: {self.kode_karyawan}, "
                f"Posisi: {self.posisi}, "
                f"Masa Kerja: {self.masa_kerja}, "
                f"Gender: {self.gender}, "
                f"Tunjangan: {self.tunjangan()}, "
                f"Insentif: {self.insentif()},  "
                f"Total Gaji: {self.total_gaji()}")

class CEO(Karyawan):
    def gaji_pokok(self):
        return 15000000

    def total_gaji(self):
        return self.gaji_pokok() + self.tunjangan()


class Bendahara(Karyawan):
    def gaji_pokok(self):
        return 10000000

    def total_gaji(self):
        return self.gaji_pokok() + self.tunjangan() + self.insentif()


class KepalaDivisi(Karyawan):
    def __init__(self, nama_karyawan, nama_divisi, kode_karyawan, posisi, masa_kerja, gender):
        super().__init__(nama_karyawan, kode_karyawan, posisi, masa_kerja, gender)
        self.nama_divisi = nama_divisi

    def gaji_pokok(self):
        return 9000000

    def total_gaji(self):
        return self.gaji_pokok() + self.tunjangan() + self.insentif()


class Staff(Karyawan):
    def __init__(self, nama_karyawan, nama_divisi, kode_karyawan, posisi, masa_kerja, gender):
        super().__init__(nama_karyawan, kode_karyawan, posisi, masa_kerja, gender)
        self.nama_divisi = nama_divisi

    def gaji_pokok(self):
        return 5000000

    def total_gaji(self):
        return self.gaji_pokok() + self.tunjangan() + self.insentif()


def tambah_karyawan(karyawan_list):
    print("=== Tambah Karyawan ===")
    nama = input("Nama Karyawan: ")
    kode = input("Kode Karyawan: ")
    posisi = input("Posisi (CEO/Bendahara/Kepala Divisi/Staff): ")
    masa_kerja = int(input("Masa Kerja (dalam tahun): "))
    gender = input("Gender (L/P): ")

    if posisi.lower() == "ceo":
        karyawan = CEO(nama, kode, posisi, masa_kerja, gender)
    elif posisi.lower() == "bendahara":
        karyawan = Bendahara(nama, kode, posisi, masa_kerja, gender)
    elif posisi.lower() == "kepala divisi":
        nama_divisi = input("Nama Divisi: ")
        karyawan = KepalaDivisi(nama, nama_divisi, kode, posisi, masa_kerja, gender)
    elif posisi.lower() == "staff":
        nama_divisi = input("Nama Divisi: ")
        karyawan = Staff(nama, nama_divisi, kode, posisi, masa_kerja, gender)
    else:
        print("Posisi tidak valid!")
        return

    karyawan_list.append(karyawan)
    print("Karyawan berhasil ditambahkan!")

def tampilkan_karyawan(karyawan_list):
    print("=== Data Karyawan ===")
    for karyawan in karyawan_list:
        print(karyawan.info())

def main():
    karyawan_list = []
    while True:
        print("\n=== Menu ===")
        print("1. Tambah Karyawan")
        print("2. Tampilkan Data Karyawan")
        print("3.  Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            tambah_karyawan(karyawan_list)
        elif pilihan == "2":
            tampilkan_karyawan(karyawan_list)
        elif pilihan == "3":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    main()
