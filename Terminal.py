import datetime
import time


class Terminal:

    def __init__(self, bar, pep, sea):
        self.menu = [bar, pep, sea]
        self.order = []
        self.flag = False   # флаг, который позволяет узнать открыта
                            # или закрыта касса
        self.cash = 0
        self.card_payment = 0
        self.openTerminal = None
        self.closeTerminal = None

    def print_menu(self):
        print(f" {self.menu[0].title:25}  {self.menu[1].title:25}  {self.menu[2].title:25}")
        for i in range(len(self.menu[0].filling) - 1):
            print(f"\t{self.menu[0].filling[i]:25} \t{self.menu[1].filling[i]:25} \t{self.menu[2].filling[i]:25}")

    def __str__(self):
        return f"ДОБРО ПОЖАЛОВАТЬ В НАШУ ПИЦЦЕРИЮ!\n" \
               f"предлагаем на выбор наши пиццы:\n"

    # функция открывает терминал
    def open(self):
        self.flag = True
        self.openTerminal = datetime.datetime.now()
        return self.flag

    # функция закрывает теминал
    def close(self):
        self.flag = False
        self.closeTerminal = datetime.datetime.now()
        return self.flag

    # принять оплату
    def give_money(self, zak):

        print("сумма вашего заказа: ", zak.summa(self.menu[0], self.menu[1], self.menu[2]))
        choice = input("оплата: \n1 - наличными\n"
                  "2 - картой\n")
        if choice == "1":

            nal = 0
            while nal < zak.summa(self.menu[0], self.menu[1], self.menu[2]):
                n = int(input("введите сумму, которою вносите: "))
                nal += n
                if nal >= zak.summa(self.menu[0], self.menu[1], self.menu[2]):
                    print("Ваша сдача: ", nal - zak.summa(self.menu[0], self.menu[1], self.menu[2]))
                else:
                    print("внесите ещё ", zak.summa(self.menu[0], self.menu[1], self.menu[2]) - nal)

            self.cash += zak.summa(self.menu[0], self.menu[1], self.menu[2])

        if choice == "2":
            print("приложите карту к терминалу")
            time.sleep(1)
            print("успешно!")
            self.card_payment += zak.summa(self.menu[0], self.menu[1], self.menu[2])

    # печать чека
    def print_check(self, zak, seller):
        print("Кассир: ", seller.FIO)
        print("Чек открыт: ", self.openTerminal)
        print("Ваш заказ:")
        for i in range(len(zak.list_pizza)):
            if zak.list_pizza[i].title == "Барбекю":
                print(zak.list_pizza[i].title, "\t\t * ", zak.bar_count, " = ",
                      zak.list_pizza[i].price * zak.bar_count)

            elif zak.list_pizza[i].title == "Пепперони":
                print(zak.list_pizza[i].title, "\t\t * ", zak.pep_count, " = ",
                      zak.list_pizza[i].price * zak.pep_count)

            elif zak.list_pizza[i].title == "Дары Моря":
                print(zak.list_pizza[i].title, "\t\t * ", zak.sea_count, " = ",
                      zak.list_pizza[i].price * zak.sea_count)


        print("\tИтого: ", zak.summa(self.menu[0], self.menu[1], self.menu[2]))
        print("Чек закрыт: ", self.closeTerminal)

