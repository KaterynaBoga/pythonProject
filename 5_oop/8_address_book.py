class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __repr__(self):
        return f"AddressBook(key='{self.key}', name='{self.name}', phone_number='+{self.phone_number}', address='{self.address}', email='{self.email}', birthday='{self.birthday}', age='{self.age}')"


address_book = AddressBook('1', 'Jhon', '+38050', 'New-York', 'test@test.com', '2015-01-01', 6)
print(address_book)

