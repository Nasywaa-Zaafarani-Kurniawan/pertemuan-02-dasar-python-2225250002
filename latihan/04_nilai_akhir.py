nama = input("Masukkan Nama: ")
nilai_tugas = float(input("Masukkan nilai Tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

bobot_tugas = 0.20
bobot_uts = 0.30
bobot_uas = 0.50

nilai_akhir = (nilai_tugas * bobot_tugas) + (nilai_uts * bobot_uts) + (nilai_uas * bobot_uas)

print()
print(f"Nama        : {nama}")
print(f"Nilai Akhir : {nilai_akhir:.2f}")