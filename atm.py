from sql_query import SqlAtm


class Atm:

    def atm_logic(self):
        SqlAtm.create_table()
#        SqlAtm.add_users((1234, 1111, 10000))
        card_number = input('Card number: ')
        while True:
            if SqlAtm.card_input(card_number):
                if SqlAtm.pin_input(card_number):
                    print('OK')
                else:
                    break
            else:
                break

start = Atm()
start.atm_logic()

