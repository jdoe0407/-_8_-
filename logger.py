import os

def input_contact():
    # f = open('data.txt', 'r')
    # if not f:
    #     f = open('data.txt', 'w')
    #     f.close()
    # else:
    #     f.close()
    if not os.path.isfile('data.txt'):
        f = open('data.txt', 'w')
        f.close()


    with open('data.txt', 'a', encoding='utf-8') as f:
        user = input('Введите имя, фамилию и телефон: ').strip().split()
        f.write(';'.join(user) + '\n')


def print_contacts():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    for contact in contacts:
        print(*contact.strip().split(';'))


def find_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    while True:
        print('По каким параметрам ищем контакт?:\n1. Имя\n2. Фамилия\n3. Телефон')
        command_index = int(input('Команда: '))
        if str(command_index) not in '123':
            print('Других параметров нету.')
        else:
            break
    data = input('Введите данные: ')
    print('Найденные контакты: ')
    for contact in contacts:
        full_contact = contact.strip().split(';')
        if data.lower() == full_contact[command_index-1].lower():
            print(' '.join(full_contact))

def change_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    while True:
        print('Какой контакт изменить? Найти по:\n1. Имя\n2. Фамилия\n3. Телефон')
        command_index = int(input('Команда: '))
        if str(command_index) not in '123':
            print('Других параметров нету.')
        else:
            break   
    n = input('Введите значение: ')
    flg=False
    st=-1
    for contact in contacts:
        st+=1
        new_contact = contact.strip().split(';')
        if n.lower() == new_contact[command_index-1].lower():
            print('Найден следующий контакт: ', *new_contact)
            answer=input('Это искомый контакт?: ')
            if answer.lower() == 'да':
                flg=True
                break
            else:
                continue
    if flg==True:
        n1 = input('Введите имя: ') #c
        n2= input('Введите фамилию: ')#Фамилия
        n3 = input('Введите телефон: ') #Телефон
        contacts[st] =  ';'.join([n1, n2, n3])
        with open('data.txt', 'w', encoding='utf-8') as f:
            f.writelines(contacts)
  
def delete_contact():
    with open('data.txt', 'r', encoding='utf-8') as f:
        contacts = f.readlines()
    while True:
        print('Какой контакт удалить? Найти по:\n1. Имя\n2. Фамилия\n3. Телефон')
        command_index = int(input('Команда: '))
        if str(command_index) not in '123':
            print('Других параметров нету.')
        else:
            break   
    n = input('Введите значение: ')
    print('Удалены следующие контакты: ')
    for contact in contacts:
        new_contact = contact.strip().split(';')
        if n.lower() == new_contact[command_index-1].lower():
            print(*new_contact)
            contacts.remove(contact)
    with open('data.txt', 'w', encoding='utf-8') as f:
        f.writelines(contacts)


            
        
        


