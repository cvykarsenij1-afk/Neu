import csv
import os

CSV_FILE = "products.csv"
SORTED_FILE = "sorted_products.csv"
FIELD_NAMES = ["Название", "Цена", "Количество"]


def load_data(filename):
    data = []
    if not os.path.exists(filename):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELD_NAMES)
            writer.writeheader()
        return data
    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["Цена"] = int(row["Цена"])
            row["Количество"] = int(row["Количество"])
            data.append(row)
    return data


def save_data(filename, data):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELD_NAMES)
        writer.writeheader()
        writer.writerows(data)
    print(f"Данные сохранены в {filename}")


def add_product(data):
    name = input("Введите название товара: ").strip()
    if not name:
        print("Название не может быть пустым.")
        return
    for item in data:
        if item["Название"].lower() == name.lower():
            print("Товар с таким названием уже существует.")
            choice = input("Добавить всё равно? (да/нет): ").strip().lower()
            if choice != "да":
                return
            break

    try:
        price = int(input("Введите цену (руб): "))
        quantity = int(input("Введите количество: "))
    except ValueError:
        print("Цена и количество должны быть целыми числами.")
        return

    data.append({"Название": name, "Цена": price, "Количество": quantity})
    print(f"Товар '{name}' добавлен.")
    save_data(CSV_FILE, data)


def search_product(data):
    query = input("Введите название для поиска: ").strip().lower()
    if not query:
        print("Поисковый запрос пуст.")
        return
    found = [item for item in data if query in item["Название"].lower()]
    if found:
        print("\nРезультаты поиска:")
        print(f"{'Название':<15} {'Цена':<6} {'Количество':<10}")
        for p in found:
            print(f"{p['Название']:<15} {p['Цена']:<6} {p['Количество']:<10}")
    else:
        print("Товары не найдены.")


def total_value(data):
    total = sum(p["Цена"] * p["Количество"] for p in data)
    print(f"Общая стоимость всех товаров на складе: {total} руб.")


def save_sorted_by_price(data):
    if not data:
        print("Нет данных для сортировки.")
        return
    sorted_data = sorted(data, key=lambda x: x["Цена"])
    save_data(SORTED_FILE, sorted_data)
    print(f"Отсортированные по цене продукты сохранены в {SORTED_FILE}")


def display_menu():
    print("\n" + "=" * 40)
    print("CSV-Обработчик продуктов")
    print("1. Показать все товары")
    print("2. Добавить новый товар")
    print("3. Поиск товара по названию")
    print("4. Рассчитать общую стоимость")
    print("5. Сохранить данные (в products.csv)")
    print("6. Сохранить отсортированные по цене (в sorted_products.csv)")
    print("7. Выйти")
    print("=" * 40)


def show_products(data):
    if not data:
        print("Список товаров пуст.")
        return
    print("\nТекущий список товаров:")
    print(f"{'Название':<15} {'Цена':<6} {'Количество':<10}")
    for p in data:
        print(f"{p['Название']:<15} {p['Цена']:<6} {p['Количество']:<10}")


def main():
    data = load_data(CSV_FILE)

    while True:
        display_menu()
        choice = input("Выберите действие (1-7): ").strip()
        if choice == "1":
            show_products(data)
        elif choice == "2":
            add_product(data)
            # после добавления data обновляется и сохраняется внутри add_product
        elif choice == "3":
            search_product(data)
        elif choice == "4":
            total_value(data)
        elif choice == "5":
            save_data(CSV_FILE, data)
        elif choice == "6":
            save_sorted_by_price(data)
        elif choice == "7":
            print("Выход из программы. Сохраняем изменения...")
            save_data(CSV_FILE, data)
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()