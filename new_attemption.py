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
random = Random()


def random_str(randomlength=6):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

def random_num(randomlength=6):
    str = ''
    chars = '0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def get_score(passcode):
    if passcode.isdigit():
        return random.uniform(0.1, 0.2)
    elif passcode.isalpha() and passcode.istitle():
        return random.uniform(0.3, 0.4)
    counter = 0
    for i in range(len(passcode)):
        if passcode[i].isdigit():
            counter += 1
    if counter == 5:
        return random.uniform(0.2, 0.4)
    if counter == 0:
        return random.uniform(0.5, 0.6)
    elif counter == 1 or counter == 4:
        return random.uniform(0.7, 0.8)
    else:
        return random.uniform(0.8, 0.9)


key = 0
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(2000):
        a = random_num()
        acode = ed.decode(a)
        writer.writerow([a, acode, get_score(a), key])
    for i in range(8000):
        if i == 1000:
            key = 1
        a = random_str()
        acode = ed.decode(a)
        writer.writerow([a, acode, get_score(a), key])
