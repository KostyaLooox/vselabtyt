def z1():
    c = {
        "Россия": "Москва",
        "США": "Вашингтон",
        "Франция": "Париж",
        "Китай": "Пекин",
        "Германия": "Берлин"
    }
    strana = input("Введите название страны: ")
    if strana in c:
        sity = c[strana]
        print(f"Столица {strana} - {sity}")
    else:
        print("Такой страны нет в списке")

    sorted_c = sorted(c.items())
    print("Список стран и их столиц в алфавитном порядке:")
    for strana, sity in sorted_c:
        print(f"{strana} - {sity}")

def z2():
    scores = {
        "А": 1, "Б": 3, "В": 1, "Г": 3, "Д": 2, "Е": 1, "Ё": 3, "Ж": 5, "З": 5,
        "И": 1, "Й": 4, "К": 2, "Л": 2, "М": 2, "Н": 1, "О": 1, "П": 2, "Р": 1,
        "С": 1, "Т": 1, "У": 2, "Ф": 10, "Х": 5, "Ц": 5, "Ч": 5, "Ш": 8, "Щ": 10,
        "Ъ": 10, "Ы": 4, "Ь": 3, "Э": 8, "Ю": 8, "Я": 3
    }
    word = input("Введите слово: ").upper() # upper все в верхний регистр
    total = sum(scores[letter] for letter in word)
    print(f"Стоимость слова '{word}' равна {total} очкам")


def z3():
    students = [
        {"name": "Иван", "languages": ["английский", "французский", "испанский"]},
        {"name": "Мария", "languages": ["немецкий", "русский", "английский"]},
        {"name": "Петр", "languages": ["японский", "китайский", "английский"]},
        {"name": "Анна", "languages": ["испанский", "итальянский", "французский"]}
    ]
    langu = set()
    for student in students:
        langu.update(student["languages"])


    sorl = sorted(langu)
    print("Список всех языков:", sorl)

    chin = []
    for student in students:
        if "китайский" in student["languages"]:
            chin.append(student["name"])
    print("Студенты, знающие китайский язык:", chin)

z1()
z2()
z3()
