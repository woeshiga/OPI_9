#!/usr/bin/env python3
# -*- coding: utf-8 -*-¬

if __name__ == '__main__':
    dct = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    print('Исходный словарь:', dct)
    d = dct.items()
    print('Применение метода items():', d)
    swapped = dict(map(reversed, d))
    print('Обратный словарь:',swapped)
    