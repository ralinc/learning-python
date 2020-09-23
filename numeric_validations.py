import re


def is_roman_numeral(value):
    pattern = '''
    ^                   # beginning of string
    M{0,3}              # thousands - 0 to 3 Ms
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                        #            or 500-800 (D, followed by 0 to 3 Cs)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                        #        or 50-80 (L, followed by 0 to 3 Xs)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                        #        or 5-8 (V, followed by 0 to 3 Is)
    $                   # end of string
    '''

    return bool(re.search(pattern, value, re.VERBOSE))


def is_phone_number(value):
    pattern = '''
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    '''

    return bool(re.search(pattern, value, re.VERBOSE))


if __name__ == '__main__':
    print(is_roman_numeral('M'))
    print(is_roman_numeral('MCMLXXXIX'))
    print(is_roman_numeral('MMMDCCCLXXXVIII'))

    print(is_phone_number('800-555-1212'))
    print(is_phone_number('(800)5551212 ext. 1234'))
    print(is_phone_number('work 1-(800) 555.1212 #1234'))
