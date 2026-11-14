print("=== PENGELOLAAN RUANG PENYIMPANAN ===")

kapasitas = int(input("Masukkan kapasitas penyimpanan (GB): "))
jumlah_file = int(input("Masukkan jumlah file: "))
files = []

for i in range(jumlah_file):
    print("\nFile ke-", i + 1)
    nama = input("Masukkan nama file: ")
    ukuran = int(input("Masukkan ukuran file (GB): "))
    prioritas = int(input("Masukkan prioritas file: "))
    files.append({"nama": nama,"ukuran": ukuran,"prioritas": prioritas})
    
total_kombinasi = 2 ** jumlah_file
prioritas_terbaik = 0
ukuran_terbaik = 0
terpilih = []

for angka in range(total_kombinasi):
    kombinasi = []
    total_ukuran = 0
    total_prioritas = 0
    for i in range(jumlah_file):
        if angka & (1 << i):
            kombinasi.append(files[i])
            total_ukuran += files[i]["ukuran"]
            total_prioritas += files[i]["prioritas"]
    if total_ukuran <= kapasitas:
        if total_prioritas > prioritas_terbaik:
            prioritas_terbaik = total_prioritas
            ukuran_terbaik = total_ukuran
            terpilih = kombinasi

print("\n=== HASIL BRUTE FORCE ===")
print("Kapasitas:", kapasitas, "GB")
print("\nFile yang Terpilih:")
for file in terpilih:
    print(file["nama"], "-", file["ukuran"], "GB","- Prioritas:", file["prioritas"])

print("\n=== HASIL AKHIR ===")
print("Total Kombinasi Diperiksa:", total_kombinasi)
print("Total File Terpilih:", len(terpilih))
print("Total Kapasitas Terpakai:", ukuran_terbaik, "GB")
print("Sisa Kapasitas:", kapasitas - ukuran_terbaik, "GB")
print("Total Nilai Prioritas:", prioritas_terbaik)
