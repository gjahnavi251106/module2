numbers = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40,
    "e": 50
}

if all(value % 2 == 0 for value in numbers.values()):
    print("All values are even")
else:
    print("All values are not even")