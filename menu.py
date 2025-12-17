from mahasiswa import mahasiswa
from data import load_data, save_data, append_data

data_mahasiswa = []

def input_valid_nilai(prompt):
    while True:
        try:
            nilai = int(input(prompt))
            if 0 <= nilai <= 100:
                return nilai
            else:
                print("Nilai harus berada dalam rentang 0-100. ") 

        except ValueError:
            print("Input tidak valid")

def cari_mahasiswa(nim):
    for mhs in data_mahasiswa:
        if mhs.nim == nim:
            return mhs
    return None
    
def manajemen_data_mahasiswa():
    while True:
        print("\n=== Manajemen Data Mahasiswa (CRUD) ===")
        print("1. Tambah Data Mahasiswa")
        print("2. Cari Data Mahasiswa")
        print("3. Update Data Mahasiswa")
        print("4. Hapus Data Mahasiswa")
        print("5. Kembali")

        pilihan = input("Pilih menu (1-5): ").strip()

        # ================= CREATE =================
        if pilihan == "1":
            nim = input("Masukkan NIM (Unik): ").strip()
            if cari_mahasiswa(nim):
                print("NIM sudah terdaftar.")
                continue

            nama = input("Masukkan Nama: ").strip()
            mhs_baru = mahasiswa(nim, nama)

            data_mahasiswa.append(mhs_baru)
            append_data(mhs_baru)

            print(f"Mahasiswa {nama} ({nim}) berhasil ditambahkan.")

        # ================= READ =================
        elif pilihan == "2":
            nim = input("Masukkan NIM yang dicari: ").strip()
            mhs = cari_mahasiswa(nim)

            if not mhs:
                print("Data mahasiswa tidak ditemukan.")
            else:
                print("\nData Mahasiswa")
                print(f"NIM  : {mhs.nim}")
                print(f"Nama : {mhs.nama}")
                print(f"Tugas: {mhs.tugas}")
                print(f"UTS  : {mhs.uts}")
                print(f"UAS  : {mhs.uas}")
                print(f"Kehadiran: {mhs.kehadiran}")

        # ================= UPDATE =================
        elif pilihan == "3":
            nim = input("Masukkan NIM mahasiswa yang akan diupdate: ").strip()
            mhs = cari_mahasiswa(nim)

            if not mhs:
                print("Mahasiswa tidak ditemukan.")
                continue

            print(f"Data nama lama : {mhs.nama}")
            print(f"Data nilai tugas lama : {mhs.tugas}")
            print(f"Data nilai uts lama : {mhs.uts}")
            print(f"Data nilai uas lama : {mhs.uas}")

            print("\n# Kosongkan jika tidak diubah")
            nama_baru = input("Masukkan Nama Baru : ").strip()
            nilai_tugas = input("Masukan nilai tugas baru : ")
            nilai_uts = input("Masukan nilai uts baru : ")
            nilai_uas = input("Masukan nilai uas baru : ")

            if nama_baru:
                mhs.nama = nama_baru

            if nilai_tugas or nilai_uts or nilai_uas:
                mhs.tugas = int(nilai_tugas)
                mhs.uts = int(nilai_uts)
                mhs.uas = int(nilai_uas)

            mhs.hitung_nilai()
            save_data(data_mahasiswa)
            print("Data mahasiswa berhasil diperbarui.")

        # ================= DELETE =================
        elif pilihan == "4":
            nim = input("Masukkan NIM mahasiswa yang akan dihapus: ").strip()
            mhs = cari_mahasiswa(nim)

            if not mhs:
                print("Mahasiswa tidak ditemukan.")
                continue

            konfirmasi = input("Yakin ingin menghapus? (y/n): ").strip().lower()
            if konfirmasi == "y":
                data_mahasiswa.remove(mhs)
                save_data(data_mahasiswa)
                print("Data mahasiswa berhasil dihapus.")

        # ================= EXIT =================
        elif pilihan == "5":
            break

        else:
            print("Pilihan tidak valid.")


def input_nilai_akademik():
    print("2. Input Nilai Akademik Anda")
    nim = input("masukkan NIM anda : ").strip()
    mhs = cari_mahasiswa(nim)

    if not mhs:
        print(f"Error: Mahasiswa dengan NIM {nim} tidak dapat ditemukkan. ")
        return
    
    print(f"\nInput nilai untuk: {mhs.nama} ({mhs.nim}) ")
    mhs.tugas = input_valid_nilai("Masukkan Nilai Tugas (0-100): ")
    mhs.uts = input_valid_nilai("Masukkan Nilai UTS (0-100): ")
    mhs.uas = input_valid_nilai("Masukkan Nilai UAS (0-100): ")

    mhs.hitung_nilai()
    save_data(data_mahasiswa)
    print(f"Nilai berhasil diperbarui. Nilai akhir : {mhs.nilai_akhir:.2f}, Grade: {mhs.grade} ")

def input_presensi_otomatis():
    print("3. Input Presensi Otomatis")
    print("Gunakan: h = hadir | i = izin | a = alpha")

    while True:
        try:
            pertemuan_ke = int(input("Masukkan Angka Pertemuan Ke-N: "))
            if pertemuan_ke > 0:
                break
            print("Angka pertemuan harus > 0")
        except ValueError:
            print("Input tidak valid")

    jenis_sesi = "Teori" if pertemuan_ke % 2 != 0 else "Praktikum"
    print(f"\nPertemuan ke-{pertemuan_ke} ({jenis_sesi})")

    if not data_mahasiswa:
        print("Tidak ada data mahasiswa")
        return

    for mhs in data_mahasiswa:
        while len(mhs.kehadiran) < pertemuan_ke:
            mhs.kehadiran.append("-")

        while True:
            status = input(
                f"{mhs.nama} ({mhs.nim}) [h/a/i]: "
            ).strip().lower()

            if status == "h" or status == "a" or status == "i":
                break
            else:
                print("Input salah! Harus h, a, atau i")

        mhs.kehadiran[pertemuan_ke - 1] = status
        mhs.hitung_persentase_hadir()

    print("Presensi berhasil dicatat")


def tampilkan_laporan():
    print("4. Laporan Data dan Nilai Mahasiswa")
    if not data_mahasiswa:
        print("Tidak ada data mahasiswa untuk ditampilkan. ")
        return
    
    print("-" * 101)
    print(f"| {"NIM" :^5} | {"Nama" :<25} | {"Tugas" :<5} | {"UTS" :<5} | {"UAS" :<5} | {"NA" :<6} | {"Grade" :<5} | {"Pertemuan" :<9} | {" % Hadir" :<8} |")
    print("-" * 101)
    for mhs in data_mahasiswa:
        mhs.hitung_nilai()
        mhs.hitung_persentase_hadir()

        print(f"| {mhs.nim:^5} | {mhs.nama:<25} | {mhs.tugas:^5} | {mhs.uts:^5} | {mhs.uas:^5} | {mhs.nilai_akhir:^6} | {mhs.grade:^5} | {mhs.total_pertemuan:^9} | {mhs.persentase_hadir:^8} |")
    
    print("-" * 101); print()

def tampilkan_data_singkat():
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
        return

    print("\nDaftar Mahasiswa:")
    print("-" * 50)
    for mhs in data_mahasiswa:
        print(f"NIM: {mhs.nim} | Nama: {mhs.nama}")
    print("-" * 50)

def main_menu():
    global data_mahasiswa
    data_mahasiswa = load_data()
    
    while True:
        print("Sistem Manajemen Nilai Undiknas")
        print("1. Manajemen data Mahasiswa ")
        print("2. Input Nilai Akademik ")
        print("3. Input Presensi otomatis ")
        print("4. Tampilkan Laporan / Output data ")
        print("5. Keluar dan simpan data ")

        pilihan = input("Masukkan pilihan angka (1-5): ").strip ()

        if pilihan == "1":
            manajemen_data_mahasiswa()
        elif pilihan == "2":
            input_nilai_akademik()
        elif pilihan == "3":
            input_presensi_otomatis()
        elif pilihan =="4":
            tampilkan_laporan()
        elif pilihan == "5":
            save_data(data_mahasiswa)
            print("Program Selesai. ")
            break
        else:
            print("Pilihan Tidak Valid.")

main_menu()