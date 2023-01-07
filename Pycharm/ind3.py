#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Маршруты
    ways = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input('>>> ').lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о маршруте.
            start = input('Название начального маршрута: ')
            finish = input('Название конечного маршрута: ')
            num = int(input('Номер маршрута: '))

            # Создать словарь.
            way = {
                'start': start,
                'finish': finish,
                'num': num,
            }

            # Добавить словарь в список.
            ways.append(way)
            # Отсортировать список в случае необходимости.
            if len(way) > 1:
                ways.sort(key=lambda item: item.get(num, ' '))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 30,
                '-' * 15
                )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^30} | {:^15} |'.format(
                    "No",
                    "Название начального маршрута",
                    "Название конечного маршрута",
                    "Номер маршрута"
                )
            )
            print(line)

            # Вывести данные о всех маршрутах
            for idx, way in enumerate(ways, 1):
                print(
                    '| {:>4} | {:<30} | {:<30} | {:>15} |'.format(
                        idx,
                        way.get('start', ''),
                        way.get('finish', ''),
                        way.get('num', 0)
                    )
                )
            print(line)

        elif command == 'find':
            f = input('Введите номер маршрута: ')
            for way in ways:
                flag = 1
                if f in str(way.values()):
                    flag = 0
                    print('Маршрут найден:')
                    print(
                        f"Название начального маршрута: {way.get('start', '')} \n"
                        f"Название конечного маршрута: {way.get('finish', 0)} \n"
                        f"Номер маршрута: {way.get('num', 0)}"
                    )
                    continue

            if flag == 1:
                print('Маршрут не найден')

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить маршрут;")
            print("list - вывести список маршрутов;")
            print("find - вывод информации о маршруте;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
