from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title('Калькулятор для втб')
#root.iconbitmap(default="png.ico")
root.geometry('600x300')



def func():
    try:
        a = float(entry_1.get())
        b = float(entry_2.get())
        c = float(entry_3.get())
        b = a*b / 100 
        round(b, 0)
        a -= b
        a -= 6000000
        round(a, 0)
        c1 = 100 - c
        a = a/c1*100
        final = a * c / 100
        round(final, 2)

        label_3 = tk.Label(root, text="Комиссиия будет равна: {}". format(final))
        label_3.place(x = 3, y = 90, width=250, height=20)
    except ValueError:
        label_4 = tk.Label(root, text='Ошибка, введите цифры.')
        label_4.place(x = 3, y = 110, width=140, height=30)


entry_1 = tk.Entry(root)
entry_1.place(x=135, y = 5, width=50, height=15)
entry_2 = tk.Entry(root)
entry_2.place(x=240, y = 25, width=50, height=15)
entry_3 = tk.Entry(root)
entry_3.place(x=165, y = 45, width=50, height=15)

label = tk.Label(root, text="Введите цену кваритры:")
label.pack(anchor="nw")
label_1 = tk.Label(root, text="Введите процент первоначального взноса:")
label_1.pack(anchor="w")
label_2 = tk.Label(root, text="Введите процент коммисии:")
label_2.pack(anchor="sw")
label_5 = tk.Label(root, text='Для ввода больших сумм что бы не ошибиться с нулями нужно использовать "_", например: 10_000_000')
label_5.place(x = 3, y = 140)
label_6 = tk.Label(root, text='Десятые и сотые нужно вводить через точку, например: 11.8')
label_6.place(x = 3, y = 160)
button = tk.Button(root, text='Посчитать коммисию.', command=func)
button.place(x=3, y = 65, width=150, height=25)
root.mainloop()