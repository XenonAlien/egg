def egg_drop(max_floor):
    """
    Оптимальный алгоритм для задачи о яйцах и небоскрёбе.
    Возвращает минимальный этаж, где яйцо разбивается, и число попыток.
    """
    step = 1
    current_floor = 0
    attempts = 0

    # Фаза 1: Экспоненциальный поиск (1, 2, 4, 8...)
    while current_floor <= max_floor:
        if egg_breaks(current_floor):  # Замени на реальную проверку!
            # Фаза 2: Бинарный поиск
            low = current_floor // 2
            high = current_floor
            while low <= high:
                mid = (low + high) // 2
                if egg_breaks(mid):
                    high = mid - 1
                else:
                    low = mid + 1
                attempts += 1
            return high, attempts
        current_floor += step
        step *= 2
        attempts += 1
    return max_floor, attempts

# Пример использования (замени egg_breaks на свою логику!)
def egg_breaks(floor):
    """Тестовая функция: яйцо разбивается на 64+ этаже."""
    return floor >= 64

critical_floor, total_attempts = egg_drop(100)
print(f"Критический этаж: {critical_floor}, Попыток: {total_attempts}")
