# source: https://github.com/django/django/blob/master/django/utils/baseconv.py


class Base62:
    decimal_digits = "0123456789"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    sign = "-"

    @staticmethod
    def encode(i):
        neg, value = Base62.convert(i, Base62.decimal_digits, Base62.digits, "-")
        if neg:
            return Base62.sign + value
        return value

    @staticmethod
    def decode(s):
        neg, value = Base62.convert(
            s, Base62.digits, Base62.decimal_digits, Base62.sign
        )
        if neg:
            value = "-" + value
        return int(value)

    @staticmethod
    def convert(number, from_digits, to_digits, sign):
        if str(number)[0] == sign:
            number = str(number)[1:]
            neg = 1
        else:
            neg = 0

        # make an integer out of the number
        x = 0
        for digit in str(number):
            x = x * len(from_digits) + from_digits.index(digit)

        # create the result in base 'len(to_digits)'
        if x == 0:
            res = to_digits[0]
        else:
            res = ""
            while x > 0:
                digit = x % len(to_digits)
                res = to_digits[digit] + res
                x = int(x // len(to_digits))
        return neg, res
