import re


class ValidCarNumber:

    def __init__(self, number):
        self.number = number

    def is_valid(self):
        is_valid = re.search(r"0([1-9])+KG([0-9]{3})([A-Z]{3})", self.number)
        if not is_valid:
            print('Number is NOT valid.')
        elif self.number[is_valid.start():is_valid.end()] == self.number:
            print('Number is valid.')


tesla = ValidCarNumber('01KG111LEE')
tesla.is_valid()
