#Программа сортировки введенных пользователем чисел с вычислением времени сортировки

#импортируем библиотеки
from tkinter import *
import time
from tkinter import messagebox as mb

#создаем родительское окно
root = Tk()
#указываем размеры окна
root.geometry("300x200")

#функция сортировки введенной пользователем строки - обработчик нажатия на кнопку Start
def sstr():
    try:
        #проверка ввода чисел через запятую, а не букв
        if not e1.get().replace(",","").isdigit():
            raise (Exception("Надо ввести числа через запятую, а не буквы!"))
        #проверка ввода чисел через запятую
        if not "," in e1.get():
            raise (Exception("Надо ввести числа через запятую!"))
        #получение данных пользователя из строки ввода e1 и превращение их в числа, используя генератор 
        n = [int(x) for x in e1.get().split(",")]
        start_time = time.perf_counter()  # время начала выполнения сортировки
        #сортировка чисел с учетом варианта сортировки, выбранного пользователем через радиокнопки
        label['text']=sorted(n, reverse=var.get())
        end_time = time.perf_counter() #время конца выполнения сортировки
        execution_time = end_time - start_time #время сортировки
        label2['text']="Время сортировки - {}".format(execution_time)
    except Exception as e:
        mb.showerror("Ошибка сортировки: ", e)

#создаем и размещаем виджет Entry - строку ввода
e1 = Entry(width=50)  
e1.pack()
#создаем и размещаем радиокнопки для выбора варианта сортировки
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
