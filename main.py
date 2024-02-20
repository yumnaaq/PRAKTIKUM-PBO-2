class Hewan:
    def __init__(self, nama, jenis, habitat):
        self.nama = nama
        self.jenis = jenis
        self.habitat = habitat

    def tampilkan_data(self):
        print("nama : " + self.nama)
        print("jenis : " + self.jenis)
        print("habitat : " + self.habitat)

hewan1 = Hewan("Kucing", "Mamalia", "darat")
hewan2 = Hewan("ikan", "vertebrata", "air")

hewan1.tampilkan_data()
hewan2.tampilkan_data()
