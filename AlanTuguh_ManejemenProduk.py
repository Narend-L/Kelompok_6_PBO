from produk import Produk, RotiManis, Croissant, ButterCookies, Muffin

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
                    print("RotiManis = Pengadonan, Pengembangan, Pemanggangan")
                elif jenis == "croissant":
                    print("Croissant = Pengadonan, Pengembangan, Pemanggangan")
                elif jenis == "muffin":
                    print("Muffin = Pengadonan, Pengembangan, Pemanggangan, Topping")
                elif jenis == "buttercookies":
                    print("ButterCookies = Pengadonan, Pemanggangan, Topping")
                else:
                    print("Jenis produk tidak dikenali.")
                return
        print("Produk tidak ditemukan.")
