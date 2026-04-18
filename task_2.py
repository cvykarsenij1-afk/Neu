students = []

try:
    with open('students.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            name, grades_str = line.split(':')
            grades = list(map(int, grades_str.split(',')))
            average = sum(grades) / len(grades)
            students.append({
                'name': name,
                'grades': grades,
                'average': average
            })
except FileNotFoundError:
    print("Ошибка: файл 'students.txt' не найден.")
    exit(1)
except ValueError:
    print("Ошибка: некорректный формат данных в файле.")
    exit(1)

if not students:
    print("Файл не содержит данных о студентах.")
    exit(0)

max_student = max(students, key=lambda s: s['average'])
min_student = min(students, key=lambda s: s['average'])

print(f"Студент с наивысшим средним баллом: {max_student['name']} ({max_student['average']:.2f})")
print(f"Студент с наинизшим средним баллом: {min_student['name']} ({min_student['average']:.2f})")

with open('result.txt', 'w', encoding='utf-8') as out_file:
    for student in students:
        if student['average'] > 4.0:
            grades_str = ','.join(map(str, student['grades']))
            out_file.write(f"{student['name']}:{grades_str}\n")

print("Результат сохранён в файл 'result.txt'.")