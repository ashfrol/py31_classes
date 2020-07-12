

class PhoneBook:

    def __init__(self, name):
        self.name = name
        self.contact_list = []

    def show_contacts(self):
        [print(item) for item in self.contact_list]

    def add_contact(self, Contact):
        self.contact_list.append(Contact)

    def delete_contact(self, phone_number):
        for item in self.contact_list:
            if item.phone_number == phone_number:
                self.contact_list.remove(item)
                print(f'Контакт {item.name} {item.second_name} удален')

    def find_favourite_contacts(self):
        for item in self.contact_list:
            if item.favorite == 'Да':
                print(item)

    def find_contact(self, name, second_name):
        for item in self.contact_list:
            if item.name == name and item.second_name == second_name:
                print(item)


class Contact:

    def __init__(self, name, second_name, phone_number, favorite='Нет', **kwargs):
        self.name = name
        self.second_name = second_name
        self.phone_number = phone_number
        self.more_info = kwargs
        if favorite == 'Нет':
            self.favorite = favorite
        else:
            self.favorite = 'Да'

    def __str__(self):
        main_data = f'Имя: {self.name}\n' \
                    f'Фамилия: {self.second_name}\n' \
                    f'Телефон: {self.phone_number}\n' \
                    f'В избранных: {self.favorite}\n'
        optional_data_list = ['Дополнительная информация:\n']
        for key, value in self.more_info.items():
            info = f'\t{key}: {value}\n'
            optional_data_list.append(info)
        return main_data + ''.join(optional_data_list)


john = Contact('John', 'Smith', '+71234567809', telegram='@johny', email='johny@smith.com')
mary = Contact('Mary', 'Smith', '+71234577809', favorite='Да', telegram='@mary', email='mary@smith.com')
kate = Contact('Kate', 'Johnes', '+71234561819', favorite='Да', email='kate@johnes.com')
nora = Contact('Nora', 'Alt', '+71234577855', favorite='Да')
# print(john)

phone_book1 = PhoneBook('Moscow')

phone_book1.add_contact(john)
phone_book1.add_contact(mary)
phone_book1.add_contact(kate)
phone_book1.add_contact(nora)

# phone_book1.show_contacts()

# phone_book1.delete_contact('+71234567809')
# phone_book1.find_contact('Mary', 'Smith')
# phone_book1.show_contacts()

phone_book1.find_favourite_contacts()