#Программа сортировки чисел с вычислением времени сортировки

#импортируем библиотеки
from tkinter import *
import time

#создаем родительское окно
root = Tk()
#указываем размеры окна
root.geometry("300x200")

#функция сортировки введенной пользователем строки
def sstr():
    start_time = time.perf_counter()  # время начала выполнения
    label['text']=sorted(list(e1.get().split(",")), reverse=var.get())
    end_time = time.perf_counter() #время конца выполнения
    execution_time = end_time - start_time #время сортировки
    label2['text']="Время сортировки - {}".format(execution_time)

#создаем и размещаем виджет Entry - строку ввода
e1 = Entry(width=50)  
e1.pack()
#создаем и размещаем радиокнопки
var = IntVar()
rad0 = Radiobutton(root, text="Reverse=false", variable=var, value=FALSE)
rad1 = Radiobutton(root, text="Reverse=true", variable=var, value=TRUE)
rad0.pack()
rad1.pack()
#создаем и размещаем виджет Label1 - строку вывода результат сортировки
label = Label()
label.pack()
#создаем и размещаем виджет Label2 - строку вывода времени сортировки
label2 = Label()
label2.pack()
#создаем и размещаем виджет Button - кнопку запуса сортировки
b = Button(text="Start", command=lambda:sstr())
b.pack()
#запуск программы
root.mainloop()