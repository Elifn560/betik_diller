from pathlib import Path
from src.dosya_islemleri import read_csv, write_json, write_text
from src.processing import clean_data, stats, build_report


def main():
    # Düzeltme: Path(__file__) kullanarak dosyanın gerçek yolunu alır
    base_path = Path(__file__).parent.parent  # src -> exercise

    # CSV ve çıktılar data klasörü içinde
    data_path = base_path / "data"
    read_doc = data_path / "people.csv"
    cleaned_json = data_path / "cleaned_data.json"
    stats_json = data_path / "stats.json"
    report_txt = data_path / "report.txt"

    # 1. CSV dosyasını oku
    print(f"[{read_csv.__name__}] Okunuyor: {read_doc}")
    rows = read_csv(read_doc)

    # 2. Veriyi temizle
    print(f"[{clean_data.__name__}] Temizleniyor...")
    cleaned_rows = clean_data(rows)

    # 3. Temizlenmiş veriyi JSON olarak kaydet
    print(f"[{write_json.__name__}] Kaydediliyor: {cleaned_json}")
    write_json(cleaned_json, cleaned_rows)

    # 4. İstatistikleri üret
    print(f"[{stats.__name__}] İstatistikler hesaplanıyor...")
    st = stats(cleaned_rows)

    # 5. İstatistikleri JSON olarak kaydet
    print(f"[{write_json.__name__}] Kaydediliyor: {stats_json}")
    write_json(stats_json, st)

    # 6. Raporu .txt dosyasına kaydet
    report = build_report(st)
    print(f"[{write_text.__name__}] Kaydediliyor: {report_txt}")
    write_text(report_txt, report)

    print(f"\n✅ İşlem **başarıyla** tamamlandı: Veriler '{data_path}' klasörüne kaydedildi.")

if __name__ == "__main__":
    main()