from functools import wraps
import time

def timer(func):
    """Bir fonksiyonun çalışma süresini ölçer."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        total_time = time.perf_counter() - t0
        # Düzeltme: func._name_ yerine func.__name__ kullanılıyor
        print(f"[ZAMAN] {func.__name__} süresi: {total_time:.4f} sn") 
        return result
    return wrapper


def required_column(requireds: set[str]):
    """
    CSV satırlarında belirtilen zorunlu sütunların var olup olmadığını kontrol eder.
    Eksik varsa ValueError fırlatır.
    """
    def deco(func):
        @wraps(func)
        def wrapper(rows, *args, **kwargs):
            if not rows:
                # Daha açıklayıcı bir hata mesajı
                raise ValueError(f"{func.__name__} fonksiyonuna boş veri seti geldi.") 
            keys = set(rows[0].keys())
            missing = requireds - keys
            if missing:
                raise ValueError(f"Eksik kolon(lar) bulundu: {', '.join(missing)}")
            return func(rows, *args, **kwargs)
        return wrapper
    return deco