def count_uppercase(string):
    hasil = sum(true for char in string if char.isupper())
    return hasil