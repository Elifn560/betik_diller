from pathlib import Path
from .dekorator import timer
import csv
import json
from typing import List, Dict, Any


@timer
def read_csv(path: Path) -> List[Dict]:
    """CSV dosyasını okur ve liste (dict) döner."""
    # path'in Path objesi olması varsayıldı
    with path.open("r", encoding="utf-8", newline="") as f:
        # Her satırı sözlük olarak döndürme mantığı korunuyor
        return list(csv.DictReader(f))


@timer
def write_json(path: Path, obj: Any):
    """Nesneyi JSON formatında yazar."""
    with path.open("w", encoding="utf-8") as f:
        json.dump(obj, f, indent=4, ensure_ascii=False)

@timer
def write_text(path: Path, text: str):
    """Metin verisini .txt dosyasına yazar."""
    # Path.write_text kullanımı daha sade
    path.write_text(text, encoding="utf-8")