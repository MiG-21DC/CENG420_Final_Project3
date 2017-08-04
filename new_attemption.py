from random import Random
import csv

BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

class BaseTransfer:

    def encode(self,num, alphabet=BASE62):
        """Encode a positive number in Base X

        Arguments:
        - `num`: The number to encode
        - `alphabet`: The alphabet to use for encoding
        """
        if num == 0:
            return alphabet[0]
        arr = []
        base = len(alphabet)
        while num:
            num, rem = divmod(num, base)
            arr.append(alphabet[rem])
        arr.reverse()
        return ''.join(arr)

    def decode(self,string, alphabet=BASE62):
        """Decode a Base X encoded string into the number

        Arguments:
        - `string`: The encoded string
        - `alphabet`: The alphabet to use for encoding
        """
        base = len(alphabet)
        strlen = len(string)
        num = 0

        idx = 0
        for char in string:
            power = (strlen - (idx + 1))
            num += alphabet.index(char) * (base ** power)
            idx += 1

        return num

ed = BaseTransfer()



def random_str(randomlength=6):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

random = Random()
key = 0
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(1000):
        if i == 200:
            key = 1
        a = random_str()
        acode = ed.decode(a)
        writer.writerow([a, acode, random.uniform(0.1, 0.9), key])
