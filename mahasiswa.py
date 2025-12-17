# print("tugas mahasiswa")
class mahasiswa :
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.tugas = 0
        self.uts = 0
        self.uas = 0
        self.nilai_akhir = 0.0
        self.grade = "e"
        self.kehadiran = []
        self.total_pertemuan = 0
        self.persentase_hadir = 0.0

    def hitung_nilai(self):
        bobot_tugas = 0.30
        bobot_uts = 0.35
        bobot_uas = 0.35

        kalkulator_na = lambda t, u1, u2:(t * bobot_tugas) + (u1 * bobot_uts) + (u2 * bobot_uas)
        
        self.nilai_akhir = kalkulator_na(self.tugas, self.uts, self.uas)
        if self.nilai_akhir >= 85:
            self.grade = "a"
        elif self.nilai_akhir >= 70:
            self.grade = "b"
        elif self.nilai_akhir >= 55:
            self.grade = "c"
        elif self.nilai_akhir >=40:
            self.grade = "d"
        else:
            self.grade = "e"

    def hitung_persentase_hadir(self):
        status = [s for s in self.kehadiran if s in ("h", "a", "i")]

        if not status:
            self.total_pertemuan = 0
            self.persentase_hadir = 0.0
            return

        self.total_pertemuan = len(status)
        hadir = status.count("h")
        self.persentase_hadir = (hadir / self.total_pertemuan) * 100

