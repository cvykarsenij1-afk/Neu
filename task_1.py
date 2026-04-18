lines_to_write = [
    "Это первая строка. Тут писать",

]

with open("text.txt", "w", encoding="utf-8") as f:
    for line in lines_to_write:
        f.write(line + "\n")

with open("text.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

lines = [line.rstrip("\n") for line in lines]

num_lines = len(lines)
print(f"Количество строк в файле: {num_lines}")

total_words = 0
for line in lines:
    words = line.split()
    total_words += len(words)
print(f"Количество слов в файле: {total_words}")

longest_line = max(lines, key=len, default="")
print(f"Самая длинная строка: {longest_line}")

vowels = set("аеёиоуыэюя")
consonants = set("бвгджзйклмнпрстфхцчшщ")

total_vowels = 0
total_consonants = 0

for line in lines:
    for ch in line.lower():
        if ch in vowels:
            total_vowels += 1
        elif ch in consonants:
            total_consonants += 1

print(f"Общее количество гласных букв: {total_vowels}")
print(f"Общее количество согласных букв: {total_consonants}")