def is_narcissistic_number(value):
    '''Check whether a given number is a narcissistic number or not.

    Keyword arguments:
    value -- the number to check

    Returns: boolean

    '''

    return value == sum([int(digit)**len(str(value)) for digit in str(value)])


if __name__ == '__main__':
    print(is_narcissistic_number(153))
    print(is_narcissistic_number(370))
    print(is_narcissistic_number(407))
    print(is_narcissistic_number(409))
    print(is_narcissistic_number(1634))
    print(is_narcissistic_number(8208))
    print(is_narcissistic_number(9474))
    print(is_narcissistic_number(9475))
