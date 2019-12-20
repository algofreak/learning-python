import math

print("Hello World !!!")
print("*" * 10)

str = "Hello World!!!"

print(str[2:10])
print(str[0:5])
print(str[6:])
print(str[:])
print(str[-14])

message = "Hello"
print(type(message))

message = """
Python Programming 
is the best languauge in the
entire world
"""
print(message.title())

first = "Pradip"
last = "Gajjar"
print(f"{first} {last}")

print("Python \"Programming\"")
print('"Python" Programming')

print(first.find("dip"))
print(first.replace("dip", "rav"))
print("Prog" in first)
print("Prad" in first)


x = 10

x = 0b10
print(bin(x))

x = 0x12c
print(hex(x))

print(10 // 3)

PI = 3.14
print(round(PI))
print(abs(PI))

# x = int(input("x: "))
# x += 1
# print(x)

age = int(input("Enter your age: "))

if 0 < age < 18:
    print("Teenager")
else:
    print("Adult")

name = "prad"

if name:
    print("name is not empty")
else:
    print("name is empty")


print("name is not empty") if name else print("name is empty")

for i in "Pradip":
    print(i)

for i in ['a', 'b', 'c']:
    print(i)

for i in range(5, 10):
    print(i)


def increment(number: int, by: int) -> tuple:
    return number, number + by, by


print(increment(by=3, number=2))
apps = ["jingle", "rio", "vwf-systems",
        "G5Ambassador", "G5Scheduler", "G5VideoProcessor"]
results = []

for app in apps:
    if app.startswith("Vwf") or app.startswith("g5"):
        results.append(app)
        print(f"Video Workflow app \"{app}\" found")
        break
else:
    print("No Video Workflow apps found in the list ", apps)


def process_list(*args):
    for item in args:
        print(item)


process_list(apps)


def process_dict(**kwargs):
    for key, value in kwargs.items():
        print(f"Key: {key}\tValue: {value}")


process_dict(name="pradip", age=38, address="Cupertino")
process_dict(name="Aarav", age=8, address="Cupertino")


def swap(a, b):
    tmp = a
    a = b
    b = tmp

x = [1, 2, 3]
y = [5, 6]
print(f"X: {x}, Y: {y}")
swap(x, y)
print(f"X1: {x}, Y1: {y}")

nums = list(range(1, 10, 2))
print(nums)


