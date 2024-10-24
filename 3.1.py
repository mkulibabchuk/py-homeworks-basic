
# Задача № 3

import os
import glob


def get_file_paths():
    """Возвращает список путей к файлам"""
    # переменная которая хранит путь к каталогу со считываемыми файлами
    files_path = os.getcwd() + "/sorted/"
    # переменная которая хранит пути к файлам в каталоге
    file_paths = glob.glob(files_path + "*.txt")
    # возвращение путей к файлам
    return file_paths


def read_file_and_write_to_result():
    """Читает каждый файл в каталогеи пишет его содержимое в
    итоговый файл согласно заданным параметрам (сортировка по кол-ву строк,
    указанию имени файла и кол-ва строк"""
    # вызов функции по получению путей файлов
    file_paths = get_file_paths()
    # инициализация списка для работы с файлами
    file_content_lst = []
    # итерация по путям к файлов для доступа к данным и параметрам записи
    for file in file_paths:
        # получение имени файла
        file_name = file.split("/")[-1]
        # открытие файла и чтение его содержимого
        with open(file, encoding="utf-8") as f:
            # запись содержимого файла в список
            data = f.readlines()
            # создание вложенного списка для последующей сортировки
            file_content_lst.append([len(data), file_name, data])
    # сортировка для записи в итоговый файл
    file_content_lst.sort()
    # начало записи в итоговый файл
    with open("result.txt", "w", encoding="utf-8") as res_f:
        # итерация по вложенному списку чтобы записать
        # содержимое каждого файла в отдельную строку
        for el in file_content_lst:
            # запись содержимого каждого файла по-строчно в итоговый файл
            res_f.write(f"{el[0]}\n{el[1]}\n{''.join(el[2])}\n")


# вызов функции
read_file_and_write_to_result()
