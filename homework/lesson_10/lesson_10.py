def calculate_total(price, tax_percent):
    if tax_percent > 20:
        return "Ошибка: налог не должен превышать 20%"
    elif price < 0:
        return "Ошибка: цена не должна быть отрицательной"
    total = price + price * tax_percent / 100
    return total


def get_level(points):
    if points >= 100:
        return "Эксперт"
    elif points >= 50:
        return "Продвинутый"
    elif points >= 20:
        return "Начинающий"
    else:
        return "Новичок"


def process_status(status):
    match status:
        case "active":
            return "Статус активен"
        case "inactive":
            return "Статус неактивен"
        case "pending":
            return "Статус в ожидании"
        case "blocked":
            return "Статус заблокирован"
        case _:
            return "Неизвестный статус"
