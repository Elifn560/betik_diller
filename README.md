<img width="1128" height="357" alt="Ekran görüntüsü 2025-11-03 215435" src="https://github.com/user-attachments/assets/60565740-431e-445a-84be-5b29cd33e161" />
<img width="439" height="792" alt="Ekran görüntüsü 2025-11-03 221021" src="https://github.com/user-attachments/assets/f1979a9a-5313-4eeb-829f-d5e896ddecbe" />


Bu proje, bir CSV dosyasından veri okuma, temizleme, istatistik üretme ve raporlama süreçlerini kapsayan modüler bir Python uygulamasıdır. Projede kullanılan dekoratörler, fonksiyonların çalışma sürelerini takip etmeye ve zorunlu kolon kontrolleri yapmaya olanak tanır.

PROJE YAPISI
Proje, görevleri ayırmak ve okunabilirliği artırmak amacıyla küçük modüllere bölünmüştür.

#Ana Modüllerin Fonksiyonları

 *`src/dosya_islemleri.py`**: CSV okuma, JSON ve TXT formatında yazma gibi tüm Girdi/Çıktı (I/O) işlemlerini yönetir.
* *`src/processing.py`**:
    * `clean_data`: Gelen veriyi temizler ve gerekli format dönüşümlerini yapar (örn. yaşı tam sayıya çevirme).
    * `stats`: Temizlenmiş veri üzerinden istatistikler (ortalama yaş, şehirlere göre dağılım vb.) üretir.
    * `build_report`: Üretilen istatistikleri anlaşılır bir metin raporu formatına dönüştürür.
  *`src/dekorator.py`**:
    * `timer`: Fonksiyonların çalışma süresini ölçerek konsola yazdıran dekoratör.
    * `required_column`: İşlem görecek veri setinde bulunması zorunlu olan kolonları kontrol eden dekoratör.
  *`src/app.py`**: Projenin ana çalıştırma dosyasıdır; tüm işlem adımlarını sırasıyla koordine eder.

 -Veri Akışı ve Çıktılar

*Girdi Dosyası**: `data/people.csv`
*Üretilen Çıktılar**:
    * `data/cleaned_data.json`: Temizlenmiş ve işlenmiş kayıtların JSON formatı.
    * `data/stats.json`: Hesaplanan ham istatistiklerin JSON formatı.
    * `data/report.txt`: Nihai analiz sonuçlarını içeren metin raporu.

- Kurulum ve Çalıştırma

Projenin yerel ortamınızda doğru şekilde çalıştırılması için aşağıdaki adımlar izlenmelidir.

-Önkoşullar

* Python 3.x sürümü kurulu olmalıdır.

-Çalıştırma Talimatı

Proje, içe aktarma hatalarını önlemek amacıyla *projenin ana dizininden* (`exercise` klasörü) bir Python *modülü* olarak çalıştırılmalıdır.

1.  *Terminalde Dizin Değiştirme:** Komut satırınızı, `src` ve `data` klasörlerini içeren ana dizine (`exercise`) taşıyın.
    ```bash
    cd path/to/exercise
    ```

2.  *Modül Olarak Çalıştırma:** Uygulamayı modül olarak başlatın.
    ```bash
    python -m src.app
    ```

-| Beklenen Sonuç |-

Konsolda, her işlemin başlatıldığına ve tamamlandığına dair bilgilendirme ile birlikte çalışma süreleri listelenecektir. Tüm işlemler bittiğinde, aşağıdaki onay mesajı görüntülenecektir:
