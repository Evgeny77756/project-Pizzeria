# import tkinter
# import tkinter.messagebox
#
# class MyGUI:
#     def __init__(self, term, zak, seller):
#         self.main_window = tkinter.Tk()
#         self.term = term
#         self.zak = zak
#         self.seller = seller
#
#         self.my_button = tkinter.Button(self.main_window, text="Нажми меня!", command=self.do_something)
#
#         self.frame = tkinter.Frame(self.main_window)
#
#         self.label1 = tkinter.Label(self.frame, text="Привет!!!")
#         self.label1.pack()
#
#         self.my_button.pack()
#
#         tkinter.mainloop()


    # def do_something(self):
    #     self.term.print_check(self.zak, self.seller)
    #     tkinter.messagebox.showinfo('hdsuav;', f"{self.frame}")

# my_gui = MyGUI(term, zak, seller)

# import datetime
# import time
# start = datetime.datetime.now()
# time.sleep(3)
# end = datetime.datetime.now()
# print(end - start)
#
# print(start < end)

# from datetime import datetime
# ts0 = int("0")
# ts = int("0")
# print(int(datetime.fromtimestamp(ts).strftime('%H:%M:%S')) - int(datetime.fromtimestamp(ts).strftime('%H:%M:%S')))

import time
from datetime import datetime

t1 = datetime.now()
t11 = t1.timetuple()
time.sleep(1)
t2 = datetime.now()
t22 = t2.timetuple()

print(time.mktime(t22) - time.mktime(t11))