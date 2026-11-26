import os
import shutil
from datetime import datetime
from pathlib import Path


class SmartFileOrganizer:
    """Belirtilen dizindeki dağınık dosyaları uzantılarına göre alt klasörlere ayıran otomasyon aracı."""

    KATEGORILER = {
        "Belgeler": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
        "Gorseller": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
        "Kod_Dosyalari": [".py", ".cs", ".cpp", ".c", ".ino", ".js", ".html", ".css", ".sql"],
        "Arsivler": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Kurulum_ve_Uygulamalar": [".exe", ".msi"],
        "Medya": [".mp4", ".mkv", ".mp3", ".wav"],
    }

    def __init__(self, hedef_dizin: str):
        self.hedef_dizin = Path(hedef_dizin).expanduser().resolve()
        self.log_dosyasi = self.hedef_dizin / "organizasyon_log.txt"

    def _kategori_bul(self, uzanti: str) -> str:
        uzanti = uzanti.lower()
        for kategori, uzantilar in self.KATEGORILER.items():
            if uzanti in uzantilar:
                return kategori
        return "Diger"

    def _benzersiz_yol_uret(self, hedef_klasor: Path, dosya_adi: str) -> Path:
        hedef_yol = hedef_klasor / dosya_adi
        sayac = 1
        kok = Path(dosya_adi).stem
        uzanti = Path(dosya_adi).suffix
        while hedef_yol.exists():
            hedef_yol = hedef_klasor / f"{kok}_{sayac}{uzanti}"
            sayac += 1
        return hedef_yol

    def _log_yaz(self, mesaj: str) -> None:
        zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_dosyasi, "a", encoding="utf-8") as f:
            f.write(f"[{zaman}] {mesaj}\n")

    def duzenle(self) -> int:
        if not self.hedef_dizin.exists() or not self.hedef_dizin.is_dir():
            raise FileNotFoundError(f"Geçersiz dizin: {self.hedef_dizin}")

        tasinan_sayisi = 0
        for oge in self.hedef_dizin.iterdir():
            if oge.is_dir() or oge.name == self.log_dosyasi.name:
                continue

            kategori = self._kategori_bul(oge.suffix)
            kategori_klasoru = self.hedef_dizin / kategori
            kategori_klasoru.mkdir(exist_ok=True)

            yeni_konum = self._benzersiz_yol_uret(kategori_klasoru, oge.name)
            shutil.move(str(oge), str(yeni_konum))
            self._log_yaz(f"{oge.name} -> {kategori}/{yeni_konum.name}")
            tasinan_sayisi += 1

        return tasinan_sayisi


if __name__ == "__main__":
    varsayilan_yol = os.path.join(os.path.expanduser("~"), "Downloads")
    girilen_yol = input(f"Düzenlenecek klasör yolu (Varsayılan: {varsayilan_yol}): ").strip()
    secilen_dizin = girilen_yol if girilen_yol else varsayilan_yol

    duzenleyici = SmartFileOrganizer(secilen_dizin)
    adet = duzenleyici.duzenle()
    print(f"İşlem tamamlandı. Toplam {adet} dosya kategorilere ayrıldı.")
