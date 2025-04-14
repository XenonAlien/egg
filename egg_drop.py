def egg_drop(max_floor, egg_breaks, verbose=True):
    step = 1
    current_floor = 0
    attempts = 0
    
    while current_floor <= max_floor:
        if verbose:
            print(f"Попытка {attempts+1}: этаж {current_floor}", end=" — ")
        if egg_breaks(current_floor):
            if verbose:
                print("РАЗБИЛОСЬ! (переходим к бинарному поиску)")
        else:
            if verbose:
                print("не разбилось")
            # Фаза 2: Бинарный поиск
            low = current_floor // 2
            high = current_floor
            while high - low > 1:
    mid = low + (high - low) // 2
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


# Пример использования
def test_egg_breaks(floor):
    """Тестовая функция: яйцо разбивается на 64+ этаже"""
    return floor >= 64


if __name__ == "__main__":
    floor, attempts = egg_drop(100, test_egg_breaks)
    print(f"Критический этаж: {floor}, Попыток: {attempts}")
