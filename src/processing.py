from .dekorator import required_column, timer
from typing import List, Dict

@timer
@required_column({"name", "age", "city"})
def clean_data(rows: List[Dict]) -> List[Dict]:
    """Veri temizleme işlemleri."""
    cleaned = []
    for row in rows:
        # Daha kısa ve okunaklı atama
        name = row.get("name", "").strip()
        age_str = row.get("age", "").strip()
        city = row.get("city", "").strip()

        # age boşsa veya sayısal değilse atla
        if not age_str.isdigit():
            continue
        
        # Yaşı int'e çevir
        age = int(age_str)

        cleaned.append({
            "name": name,
            "age": age,
            "city": city
        })
    return cleaned


@timer
def stats(rows: List[Dict]) -> Dict:
    """Temizlenmiş kayıtlardan istatistik üretir."""
    if not rows:
        return {"count": 0, "avg_age": 0, "by_city": {}}

    ages = [r["age"] for r in rows]
    
    # city'ye göre sayım için 'collections.defaultdict' veya 'Counter' yerine 
    # projedeki orijinal mantık korunmuştur.
    by_city = {}
    for r in rows:
        by_city[r["city"]] = by_city.get(r["city"], 0) + 1

    return {
        "count": len(rows),
        "avg_age": round(sum(ages) / len(ages), 2),
        "by_city": by_city
    }


def build_report(st: Dict) -> str:
    """İstatistikleri metin formatında rapora dönüştürür."""
    lines = []
    lines.append("=== RAPOR ===")
    lines.append(f"Geçerli kayıt sayısı: {st['count']}")
    lines.append(f"Ortalama yaş: {st['avg_age']}")
    lines.append("Şehirlere göre dağılım:")
    for c, n in st["by_city"].items():
        lines.append(f"  - {c}: {n}") # İki boşluk ile standart girinti
    return "\n".join(lines) + "\n"