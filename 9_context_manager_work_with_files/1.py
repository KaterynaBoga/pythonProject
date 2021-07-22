d = {}
with open("task1.txt") as file:
    for line in file:
        key = line.strip('\n')
        value = file.readline().strip('\n')
        d[key] = value

    print(d)

with open("new_file.txt", 'w') as file:
    for value in d.values():
        file.write(value)


file = open('task2', "rt")
print(file.read())



