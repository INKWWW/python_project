#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''check the validity of id whose length is 18'''

def is_valid_idcard(self, idcard):
    IDCARD_REGEX = '[1-9][0-9]{14}([0-9]{2}[0-9X])?'
    if isinstance(idcard, int):
        idcard = str(idcard)
    if not re.match(IDCARD_REGEX, idcard):
        return False
    factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    items = [int(item) for item in idcard[:-1]]
    copulas = sum([a * b for a, b in zip(factors, items)])
    ckcodes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    result = ckcodes[copulas % 11].upper() == idcard[-1].upper()
    return result

if __name__ == '__main__':
    id_num = '123456789123456789'

