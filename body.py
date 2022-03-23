import os.path
from tkinter import ttk
import tkinter as tk
import socket


def default():
    pass


def frame_label(app_name, width):
    return ttk.Labelframe(app_name, width=width)


def buttons(app_name, desc, width, function=default()):
    varname = tk.Button(app_name, text=desc, width=width, command=function)
    varname.pack(padx=10, pady=10)


def labels(location_name, width, desc):
    return ttk.Label(location_name, width=width, text=desc, anchor='n', )


def combobox(loc_name, width, string_name, ls):
    var_name = ttk.Combobox(loc_name, width=width, textvariable=string_name)
    var_name['values'] = [x for x in ls]
    var_name.pack(padx=10, pady=15)


def is_real(way):
    return os.path.exists(way)


def formatar_dados():
    path = f'C:/Users/lukki/Desktop/Cotacao/{os.getlogin()}'
    if is_real(path) is False:
        os.mkdir(path)
    arqs = os.listdir(path)
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    a = open(f'{path}/{len(arqs)}.txt', 'w', encoding='utf-8')
    a.write(f'ID : {ip}\n')
    a.write(f'CPU : {cpu_select.get()}\n')
    a.write(f'GEN : {gen_select.get()}\n')
    a.write(f'S.O : {sys_select.get()}\n')
    a.write(f'RAM : {ram_select.get()}\n')
    a.write(f'R$ MAX : {preco_select.get()}\n')
    a.write(f'PAG : {condicao_select.get()}')
    a.close()


cpu = [
    'Celeron', 'Pentium', 'I3', 'I5', 'I7', 'Ryzen 3', 'Ryzen 5', 'Ryzen 7'
]
gen = [
    '5th ou inferior', '5th ou superior', '7th ou inferior', 'superior a 7th'
]
sys = [
        'Win 7', 'Win 10', 'Win 11', 'Linux', 'Mac'
]
ram = [
    '2gb', '4gb', '8gb', '16gb', '16gb ++'
]
preco = [
    'até R$ 2500', 'até R$ 3500', 'até R$ 4500', 'até R$ 5500', 'mais de R$ 5500'
]
condicao = [
    'à vista', 'parcelamento sem juros', 'mais de 6x', 'qualquer uma'
]
app = tk.Tk()
app.title('Body')
cpu_select = tk.StringVar()
gen_select = tk.StringVar()
sys_select = tk.StringVar()
ram_select = tk.StringVar()
preco_select = tk.StringVar()
condicao_select = tk.StringVar()
a = frame_label(app, 100)
a.pack(padx=10, pady=10)
b = labels(a, 50, 'Processadores')
b.pack(padx=10, pady=10)
combobox(a, 100, cpu_select, cpu)
c = labels(a, 50, 'Geração')
c.pack(padx=10, pady=10)
combobox(a, 100, gen_select, gen)
d = labels(a, 50, 'Sistema Operacional')
d.pack(padx=10, pady=10)
combobox(a, 100, sys_select, sys)
e = labels(a, 50, 'Memória RAM')
e.pack(padx=10, pady=10)
combobox(a, 100, ram_select, ram)
f = labels(a, 50, 'Orçamento')
f.pack(padx=10, pady=10)
combobox(a, 100, preco_select, preco)
g = labels(a, 50, 'Condição de Pagamento')
g.pack(padx=10, pady=10)
combobox(a, 100, condicao_select, condicao)
buttons(app, 'Salvar', 100, formatar_dados)
buttons(app, 'Sair', 100, app.quit)
app.geometry('200x700+200+200')
app.mainloop()
