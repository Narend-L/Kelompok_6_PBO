from manajemen import ManajemenProduk
from produk import RotiManis, Croissant, Muffin, ButterCookies

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

if __name__ == "__main__":
    menu()
