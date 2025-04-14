# Оптимальный алгоритм для задачи о яйцах

## Использование
```python
from egg_drop import egg_drop

def your_egg_test(floor):
    return floor >= 64  # Ваша логика

floor, attempts = egg_drop(100, your_egg_test)
