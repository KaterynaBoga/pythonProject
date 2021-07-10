from collections import namedtuple

AddressBook = namedtuple('AddressBook', ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])

address_book_1 = AddressBook('1', 'Jhon', '+38050', 'New-York', 'test@test.com', '2015-01-01', 6)

print(address_book_1[0])
print(address_book_1.age)
print(address_book_1)

