# ABS funtion is used to convert negative values to positive


class ImplementsABS:

    def __init__(self, string):

        self.string = string

    def __abs__(self):

        return self.string.lower()

custom_obj = ImplementsABS("HELLO")

print(abs(custom_obj))

print(abs(-10))