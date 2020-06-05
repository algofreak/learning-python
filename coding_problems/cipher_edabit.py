# Problem: https://edabit.com/challenge/KZrmicjc8zCZyGNee

def encrypt(str):
    if str is not None:
        prev = 0
        result = []
        for i in range(0, len(str)):
            ascii_val = ord(str[i])
            result.append(ascii_val - prev)
            prev = ascii_val

        return result


def decrypt(asciis):
    if asciis is not None:
        prev = 0
        result = ""
        for i in range(0, len(asciis)):
            char = chr(asciis[i] + prev)
            result += char
            prev = asciis[i] + prev

        return result


print(decrypt([65, 32, 17, -17, 21, -86, 48, 34, -17, 3, 5, 7, -80, 39, 26, 9, 0, -9, 17]))