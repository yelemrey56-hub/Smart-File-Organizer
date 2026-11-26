# Smart File Organizer — Otomatik Klasör Düzenleyici

Dağınık dizinlerdeki (İndirilenler, Masaüstü vb.) dosyaları uzantılarına göre analiz edip ilgili kategori klasörlerine ayıran ve tüm işlemleri zaman damgasıyla kayıt altına alan Python otomasyon aracıdır.

### 🚀 Özellikler
- **Otomatik Kategorizasyon:** Belgeler, Görseller, Kod Dosyaları, Arşivler, Kurulum Dosyaları ve Medya türlerini otomatik sınıflandırır.
- **Çakışma Önleme:** Hedef klasörde aynı isimde dosya bulunması durumunda üzerine yazmayı önlemek için otomatik numaralandırma uygular.
- **İşlem Kaydı (Logging):** Taşınan her dosyanın eski ve yeni konumunu tarih-saat bilgisiyle `organizasyon_log.txt` dosyasına işler.
- **Standart Kütüphane Mimarisi:** Ek harici bağımlılık gerektirmeden (`os`, `shutil`, `pathlib`) doğrudan çalışır.

### ▶️ Kullanım
```bash
python organizer.py
