from Note import Note

if __name__ == '__main__':
    while True:
        print('Список команд:'
                '\nadd - создать заметку'
                '\nread - прочитать все заметки'
                '\nread_ID - вывести заметку по ID(пример: read_1)'  
                '\nchange - изменить заметку'
                '\ndelete - удалить заметку'
                '\nexit - выйти из приложения')

        choose = input('Введите команду: ')

        if choose == 'add':
            title = input('Введите заголовок заметки: ')
            body = input('Введите тело заметки: ')
            note = Note(title, body)
            note.save()
            print('Заметка успешно сохранена!!!')

        elif choose == 'read':
            try:
                notes = Note.read()
                if notes:
                    print('Список заметок:')
                    for note in notes:
                        print(f'ID: {note[0]}. =={note[1]}== \n текст: {note[2]}\n дата: {note[3]}\n')
                else:
                    print('Нет заметок')
            except FileNotFoundError:
                print('\nФайл заметок не создан\n')

        elif choose.__contains__('read_'):
            try:
                read,id = choose.split('_')
                note = Note.read_one(int(id))
                print(f'ID: {note[0]}. =={note[1]}== \n текст: {note[2]}\n дата: {note[3]}\n')
            except ValueError:
                print('\nВы ошиблись с вводом\n')

        elif choose == 'change':
            try:
                a = True
                while a:
                    try:
                        number_of_change = int(input('Введите номер заметки, которую хотите изменить: '))
                        a = False
                    except ValueError:
                        print('Введено не число')

                new_title = input('Введите новый заголовок: ')
                new_body = input('Введите новое тело заметки: ')
                Note.change(number_of_change, new_title, new_body)
                print('Заметка успешно изменена!!!')
            except FileNotFoundError:
                print('\nНевозможно изменить заметку, т.к. файл с заметками ещё не создан\n')

        elif choose == 'delete':
            try:
                a = True
                while a:
                    try:
                        number_of_delete = int(input('Введите номер заметки, которую хотите удалить: '))
                        a = False
                    except ValueError:
                        print('Введено не число')

                Note.delete(number_of_delete)
                print('Заметка успешно удалена!!!')
            except FileNotFoundError:
                print('\nНевозможно удалить заметку, т.к. файл с заметками ещё не создан\n')

        elif choose == 'exit':
            break