egg_drop(max_floor, egg_breaks):
    """
    Оптимальный алгоритм для задачи о яйцах и небоскрёбе
    :param max_floor: количество этажей (int)
    :param egg_breaks: функция, возвращающая True если яйцо разбивается на указанном этаже
    :return: (критический этаж, количество попыток)
    """
    step = 1
    current_floor = 0
    attempts = 0

    # Фаза 1: Экспоненциальный поиск
    while current_floor <= max_floor:
        if egg_breaks(current_floor):
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
