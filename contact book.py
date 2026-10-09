class Contact:
    def __init__(self, name, phone, email):
        self.name= name
        self.phone= phone
        self.email= email
    def __str__(self):
        return f'Name: {self.name}, Phone: {self.phone}, Email: {self.email}'
contacts=[]
def add_contact(name, phone, email):
    new_contact= Contact(name, phone, email)
    contacts.append(new_contact)
def search_contact(name):
    for contact in contacts:
        if contact.name == name:
            return contact
def delete_contact(name):
    for contact in contacts:
        if contact.name == name:
            contacts.remove(contact)
            return True

add_contact('pr', '12345', 'fgh')
add_contact('br', '97864', 'jg')
for c in contacts:
    print(c)
print('Searching for contact with name "pr":')
result = search_contact('pr')
if result:
    print(result)
else:
    print('Contact not found.')
print('Deleting contact with name "br":')
if delete_contact('br'):
    print('Contact deleted.')
else:
    print('Contact not found.')