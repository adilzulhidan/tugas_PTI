# Array mata kuliah
mata_kuliah = ["Algoritma", "Bahasa Inggris", "Kalkulus", "Agama", "Pancasila", "PTI", "Statistika"]

# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas):
    return (nilai_tugas * 0.3) + (nilai_uts * 0.3) + (nilai_uas * 0.4)

# Fungsi untuk menentukan huruf nilai
def tentukan_huruf_nilai(nilai_akhir):
    if nilai_akhir >= 85:
        return 'A'
    elif nilai_akhir >= 70:
        return 'B'
    elif nilai_akhir >= 55:
        return 'C'
    elif nilai_akhir >= 40:
        return 'D'
    else:
        return 'E'

# Array data mahasiswa
data_mahasiswa = []

# Memasukkan data nilai mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

for i in range(jumlah_mahasiswa):
    nama = input(f"\nMasukkan nama mahasiswa ke-{i+1}: ")

    nilai_mahasiswa = {}
    
    for mata in mata_kuliah:
        print(f"\nMasukkan nilai untuk mata kuliah {mata}:")
        nilai_tugas = float(input("Nilai Tugas: "))
        nilai_uts = float(input("Nilai UTS: "))
        nilai_uas = float(input("Nilai UAS: "))
        
        nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)
        huruf_nilai = tentukan_huruf_nilai(nilai_akhir)
        
        # Simpan nilai akhir dan huruf nilai
        nilai_mahasiswa[mata] = {"Nilai Akhir": nilai_akhir, "Huruf Nilai": huruf_nilai}
    
    data_mahasiswa.append({"Nama": nama, "Nilai": nilai_mahasiswa})

# Output hasil
print("\nHasil Nilai Mahasiswa Semester 1:")
for mahasiswa in data_mahasiswa:
    print(f"\nNama: {mahasiswa['Nama']}")
    for mata, nilai in mahasiswa['Nilai'].items():
        print(f"Mata Kuliah: {mata}, Nilai Akhir : {nilai['Nilai Akhir']:.2f}, Huruf Nilai : {nilai['Huruf Nilai']}")
