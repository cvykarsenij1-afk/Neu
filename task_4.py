import math
import datetime
import os

LOG_FILE = "calculator.log"

def show_last_operations(n=5):
    if not os.path.exists(LOG_FILE):
        print("Лог-файл пуст или не существует.")
        return
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    last_lines = lines[-n:] if lines else []
    if not last_lines:
        print("Лог-файл пуст.")
    else:
        print("\n--- Последние операции ---")
        for line in last_lines:
            print(line.strip())
        print("----------------------------\n")

def log_operation(expression, result):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {expression} = {result}\n")

def clear_log():
    with open(LOG_FILE, "w", encoding="utf-8"):
        pass
    print("Лог-файл очищен.")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число.")

def main():
    print("Калькулятор с логированием")
    print("Доступные операции: +, -, *, /, log (натуральный), sin (радианы)")
    print("Команды: 'clear' - очистить лог, 'exit' - выход")

    show_last_operations()

    while True:
        op = input("\nВведите операцию (или команду): ").strip().lower()
        if op == "exit":
            print("До свидания!")
            break
        elif op == "clear":
            clear_log()
            continue
        elif op in ("+", "-", "*", "/"):
            a = get_number("Введите первое число: ")
            b = get_number("Введите второе число: ")
            if op == "+":
                result = a + b
                expr = f"{a} + {b}"
            elif op == "-":
                result = a - b
                expr = f"{a} - {b}"
            elif op == "*":
                result = a * b
                expr = f"{a} * {b}"
            elif op == "/":
                if b == 0:
                    print("Ошибка: деление на ноль!")
                    continue
                result = a / b
                expr = f"{a} / {b}"
            print(f"Результат: {result}")
            log_operation(expr, result)
        elif op in ("log", "sin"):
            x = get_number("Введите число: ")
            if op == "log":
                if x <= 0:
                    print("Ошибка: логарифм определён только для положительных чисел.")
                    continue
                result = math.log(x)
                expr = f"ln({x})"
            elif op == "sin":
                result = math.sin(x)
                expr = f"sin({x})"
            print(f"Результат: {result}")
            log_operation(expr, result)
        else:
            print("Неизвестная операция. Попробуйте +, -, *, /, log, sin, clear, exit.")

if __name__ == "__main__":
    main()