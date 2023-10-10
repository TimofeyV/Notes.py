from datetime import datetime
from Counter import counter


class Note:
    def __init__(self, title="заголовок", body="текст",
                 date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id:int = Note.get_id()
        self.title = title
        self.body = body
        self.date = date

    def save(self):
        with open('notes.csv', 'a', encoding='utf-8') as file:
            file.write(f'{self.id};{self.title};{self.body};{self.date}\n')

    @staticmethod
    def get_id():
        try:
            with open('notes.csv', 'r', encoding='utf-8') as file:
                notes = file.read().split('\n')[:-1]
            return len(notes)+1
        except FileNotFoundError:
            return 1

    @staticmethod
    def read():
        with open('notes.csv', 'r', encoding='utf-8') as file:
            notes = file.read().split('\n')[:-1]
        return [note.split(';', 3) for note in notes]

    @staticmethod
    def read_one(note_id):
        with open('notes.csv', 'r', encoding='utf-8') as file:
            notes = file.read().split('\n')[:-1]

        for note in notes:
            id, title, body, date = note.split(';', 3)
            if int(id) == note_id:
                return note.split(';',3)



    @staticmethod
    def change(change_number, new_title, new_body):
        with open('notes.csv', 'r', encoding='utf-8') as file:
            notes = file.read().split('\n')[:-1]

        change_notes = []
        for note in notes:
            id, title, body, date = note.split(';', 3)
            if int(id) == change_number:
                new_note = f'{id};{new_title};{new_body};{str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))}'
            else:
                change_notes.append(note.strip())
        change_notes.append(new_note)

        with open('notes.csv', 'w', encoding='utf-8') as file:
            file.write('\n'.join(change_notes) + '\n')

    @staticmethod
    def delete(delete_number):
        with open('notes.csv', 'r', encoding='utf-8') as file:
            notes = file.read().split('\n')[:-1]

        leave_notes = []
        for note in notes:
            id, title, body, date = note.split(';', 3)
            if int(id) != delete_number:
                leave_notes.append(note.strip())

        with open('notes.csv', 'w', encoding='utf-8') as file:
            if len(leave_notes) < 1:
                file.write('\n'.join(leave_notes))
            else:
                file.write('\n'.join(leave_notes) + '\n')
