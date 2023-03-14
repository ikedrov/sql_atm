import sqlite3


class SqlAtm:

    @staticmethod
    def create_table():
        with sqlite3.connect('atm.db') as db:
            cur = db.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS Users_data(
            UserID INTEGER PRIMARY KEY AUTOINCREMENT,
            Card_number INTEGER NOT NULL,
            Pin_code INTEGER NOT NULL,
            Balance INTEGER NOT NULL);''')
            print('Created Users_data table')

    @staticmethod
    def add_users(data_users):
        with sqlite3.connect('atm.db') as db:
            cur = db.cursor()
            cur.execute('''INSERT INTO Users_data (Card_number, Pin_code, Balance) VALUES (?, ?, ?)''', data_users)
            print('Added new user')

    @staticmethod
    def card_input(card_number):
        try:
            with sqlite3.connect('atm.db') as db:
                cur = db.cursor()
                cur.execute(f'''SELECT Card_number FROM Users_data WHERE Card_number = {card_number}''')
                card_result = cur.fetchone()
                if card_result == None:
                    print('No such card number')
                    return False
                else:
                    print(f'Inserted card # {card_number}')
                    return True
        except:
            print('No such card number')

    @staticmethod
    def pin_input(card_number):
        pin_code = input('Enter pin code: ')
        with sqlite3.connect('atm.db') as db:
            cur = db.cursor()
            cur.execute(f'''SELECT Pin_code FROM Users_data WHERE Card_number = {card_number}''')
            pin_result = cur.fetchone()
            code_input = pin_result[0]
            try:
                if code_input == int(pin_code):
                    print('Pin OK')
                    return True
                else:
                    print('Incorrect Pin')
                    return False
            except:
                print('Incorrect Pin')
                return False




