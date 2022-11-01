contacts = input()
phonebook = {}
while '-' in contacts:
    phonebook_name, phonebook_number = contacts.split('-')
    phonebook[phonebook_name] = phonebook.get(phonebook_name, phonebook_number)
    contacts = input()
for _ in range(int(contacts)):
    searched_name = input()
    if searched_name in phonebook:
        print(f'{searched_name} -> {phonebook[searched_name]}')
    else:
        print(f'Contact {searched_name} does not exist.')
