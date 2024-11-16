# Задача №1.
# Параллельная обработка файлов. Напишите программу, которая использует модуль
# multiprocessing для параллельной обработки нескольких текстовых файлов. Пусть программа
# подсчитывает количество слов в каждом файле и выводит результат для каждого файла. Входные
# файлы задаются списком путей, и каждый процесс должен обрабатывать один файл.

import os
from multiprocessing import Pool


def count_words_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            word_count = len(text.split())
            return (file_path, word_count)
    except Exception as e:
        return (file_path, f'Ошибка: {e}')

def main(file_paths):
    with Pool(processes=os.cpu_count()) as pool:
        results = pool.map(count_words_in_file, file_paths)

    for file_path, word_count in results:
        print(f'Файл: {file_path}, Количество слов: {word_count}')

if __name__ == '__main__':
    files_to_process = ['test.txt','products.txt',]

    main(files_to_process)

# Задача №2 :
# Параллельное вычисление факториалов. Создайте программу, которая запускает несколько
# процессов для параллельного вычисления факториалов чисел из заданного списка. Каждый
# процесс должен рассчитывать факториал одного числа. Итоговый результат должен включать
# вывод всех вычисленных факториалов в формате:"Число: результат".

from multiprocessing import Pool
import math


def calculate_factorial(n):
    return (n, math.factorial(n))

def main(numbers):
    with Pool(processes=os.cpu_count()) as pool:
        results = pool.map(calculate_factorial, numbers)

    for number, factorial in results:
        print(f'Число: {number}, Факториал: {factorial}')

if __name__ == '__main__':
    numbers_to_process = [5, 10, 15, 20]

    main(numbers_to_process)

# Задача №3:
# Скачивание веб-страниц в несколько процессов. Напишите программу, которая использует
# multiprocessing для одновременного скачивания содержимого веб-страниц по списку URL-адресов.
# Каждый процесс должен загружать одну страницу и сохранять её содержимое в отдельный файл.


import requests
from multiprocessing import Pool

def download_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        filename = url.split("/")[-1] + ".html"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f'Скачана страница {url} и сохранена в файл {filename}')
    except requests.exceptions.RequestException as e:
        print(f'Ошибка при скачивании страницы {url}: {e}')

def main(urls):
    with Pool(processes=os.cpu_count()) as pool:
        pool.map(download_page, urls)

if __name__ == '__main__':
    urls_to_download = ['https://mail.ru/','https://www.wildberries.ru/']

    main(urls_to_download)
