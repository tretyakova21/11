import os
import csv
import time

def print_docs(directory):
    for root, dirs, files in os.walk(directory):
        print(f"Папка: {root}")
        for file in files:
            print(f"  Файл: {file}")

def longest_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        words = content.split()
        max_length = max(len(word) for word in words)
        longest_words_list = [word for word in words if len(word) == max_length]
        return longest_words_list

def create_csv():
    with open('rows_300.csv', 'w', newline='') as csvfile:
        fieldnames = ['№', 'Секунда', 'Микросекунда']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(1, 301):
            time.sleep(0.01)
            current_time = time.time()
            seconds = int(current_time)
            microseconds = int((current_time - seconds) * 1e6)
            writer.writerow({'№': i, 'Секунда': seconds, 'Микросекунда': microseconds})

# Пример использования
directory_path = '/путь/к/папке'  # Замените на свой путь
print_docs(directory_path)

file_path = 'article.txt'  # Замените на свой путь
longest_words_list = longest_words(file_path)
print("Самые длинные слова в файле:", longest_words_list)

create_csv()
print("CSV-файл 'rows_300.csv' создан.")


def print_docs(directory):
    for root, dirs, files in os.walk(directory):
        print(f"Папка: {root}")
        for file in files:
            print(f"  Файл: {file}")

# Пример использования
directory_path = '/путь/к/папке'  # Замените на свой путь
print_docs(directory_path)
