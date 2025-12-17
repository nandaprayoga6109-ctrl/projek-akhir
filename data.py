import csv 
import os
from mahasiswa import mahasiswa

file_data = "tugas akhir/data_mahasiswa.csv"
def load_data() :
    data_mahasiswa = []
    if not os.path.exists(file_data):
        return data_mahasiswa

    try:
        with open(file_data, mode = "r", newline = "") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                nim, nama, tugas, uts, uas, presensi_str = row

                mhs = mahasiswa (nim, nama)
                mhs.tugas = int(tugas)
                mhs.uts = int (uts)
                mhs.uas = int (uas)

                mhs.kehadiran = presensi_str.strip('[]').replace("'", "").split(', ')
                if mhs.kehadiran == ['']:
                    mhs.kehadiran = []

                mhs.hitung_nilai()
                mhs.hitung_persentase_hadir()
                data_mahasiswa.append(mhs) 
                # print(f"data{len(data_mahasiswa)} mahasiswa berhasil dimuat. ")

    except ValueError as e:
        print(f"error saat memuat data:{e}")

    return data_mahasiswa

def save_data(data_mahasiswa):
    try:
        with open(file_data, mode = "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["NIM","Nama", "Tugas", "UTS", "UAS", "Kehadiran"])
            for mhs in data_mahasiswa:
                writer.writerow([
                    mhs.nim,
                    mhs.nama,
                    mhs.tugas,
                    mhs.uts,
                    mhs.uas,
                    mhs.kehadiran
                ])
        print(f"\ndata berhasil disimpan ke {file_data}.")
    except ValueError as e:
        print(f"error saat menyimpan data: {e}")

def append_data(mhs):
    file_exists = os.path.exists(file_data)

    try:
        with open(file_data, mode="a", newline="") as file:
            writer = csv.writer(file)

            # jika file belum ada, tulis header dulu
            if not file_exists:
                writer.writerow(["NIM", "Nama", "Tugas", "UTS", "UAS", "Kehadiran"])

            writer.writerow([
                mhs.nim,
                mhs.nama,
                mhs.tugas,
                mhs.uts,
                mhs.uas,
                mhs.kehadiran
            ])

        print(f"Data mahasiswa {mhs.nama} berhasil disimpan ke file.")

    except Exception as e:
        print(f"Error saat menambahkan data: {e}")
