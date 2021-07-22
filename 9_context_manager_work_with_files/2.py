import pickle

with open("task2", "rb") as file:
    data = file.read()
    obj = pickle.loads(data)
    sum = 0
    for i in obj:
        sum += i
        result = sum / len(obj)

    print(result)

