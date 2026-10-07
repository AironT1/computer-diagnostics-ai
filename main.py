from app.expert_system import ExpertSystem


def build_demo_system():
    system = ExpertSystem()

    # Концепты
    system.add_concept("computer", "Компьютер")
    system.add_concept("monitor", "Монитор")
    system.add_concept("power_supply", "Блок питания")
    system.add_concept("video_card", "Видеокарта")
    system.add_concept("ram", "Опер��тивная память")
    system.add_concept("cpu", "Центральный процессор")
    system.add_concept("hard_drive", "Жесткий диск")

    # Семантические связи
    system.add_relation("computer", "monitor", "connected_to")
    system.add_relation("computer", "power_supply", "uses")
    system.add_relation("computer", "video_card", "has_part")
    system.add_relation("computer", "ram", "has_part")
    system.add_relation("computer", "cpu", "has_part")
    system.add_relation("computer", "hard_drive", "has_part")

    # Правила диагностики
    system.add_rule(
        {"power_on": False},
        {"check": "power_supply", "diagnosis": "Проверьте питание и блок питания."},
        confidence=0.9,
        description="Компьютер не включается — проверить питание",
    )

    system.add_rule(
        {"no_image": True, "monitor_on": True},
        {"check": "video_cable", "diagnosis": "Проверьте кабель монитора и подключение видеокарты."},
        confidence=0.88,
        description="Нет изображения при включенном мониторе — проверить видеокабель",
    )

    system.add_rule(
        {"no_image": True, "monitor_on": False},
        {"check": "monitor_power", "diagnosis": "Проверьте питание монитора и его подключение."},
        confidence=0.8,
        description="Нет изображения и монитор выключен — проверить питание монитора",
    )

    system.add_rule(
        {"computer_reboots": True},
        {"check": "temperature", "diagnosis": "Проверьте перегрев и систему охлаждения."},
        confidence=0.84,
        description="Компьютер перезагружается — проверить перегрев",
    )

    system.add_rule(
        {"slow_work": True},
        {"check": "ram_and_drive", "diagnosis": "Проверьте оперативную память и состояние диска."},
        confidence=0.75,
        description="Компьютер работает медленно — проверить RAM и диск",
    )

    system.add_rule(
        {"no_sound": True},
        {"check": "audio_output", "diagnosis": "Проверьте громкость, динамики и драйверы звука."},
        confidence=0.7,
        description="Нет звука — проверить аудиовыход",
    )

    system.add_rule(
        {"network_error": True},
        {"check": "network_adapter", "diagnosis": "Проверьте сетевой адаптер и подключение к сети."},
        confidence=0.82,
        description="Проблемы сети — проверить сетевой адаптер",
    )

    # Вероятностные веса
    system.add_probability("no_image", 0.9)
    system.add_probability("monitor_on", 0.8)
    system.add_probability("power_on", 0.95)
    system.add_probability("slow_work", 0.7)
    system.add_probability("computer_reboots", 0.82)
    system.add_probability("network_error", 0.76)

    return system


if __name__ == "__main__":
    system = build_demo_system()

    sample = {
        "power_on": True,
        "no_image": True,
        "monitor_on": True,
    }

    result = system.diagnose(sample)
    print("Результат диагностики:")
    print(result)
