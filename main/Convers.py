from tkinter import *
from tkinter import ttk, messagebox
from main.styledWidgets import HoverButton


def size_check(*args):
    for name in (
        timeValue, barValue, lengthValue, weigthValue,
        volumeValue, areaValue, speedValue, tempValue, energyValue):
        value = name.get()
        if len(value) > 1:
            if ((value[0] == '0') and (value[1] == '0')) or (
                (value[0] == '0') and (value[1] != '.')):
                name.set(value[1:])
        if len(value) > 8:
            name.set(value[:8])


class Convers(Frame):
    def __init__(self, parent, db):

        # Задание основных переменных
        self.parent = parent
        self.db = db
        timeValue = StringVar()
        barValue = StringVar()
        lengthValue = StringVar()
        weigthValue = StringVar()
        volumeValue = StringVar()
        areaValue = StringVar()
        speedValue = StringVar()
        tempValue = StringVar()
        energyValue = StringVar()

        # Кнопка возврата назад
        self.back = HoverButton(
            self.parent,
            font=("Courier", 18),
            text='Назад',
            activebackground='#00ff00',
            command=self.returnBack
        )
        self.back.pack(anchor=NW, padx=20, pady=20)

        # Основной фрейм
        self.mainPart = Frame(self.parent)

        # Создаем переводчик величин времени
        self.Label_time = Label(self.mainPart, font=("Courier", 18),
                                text='Перевод величин времени')
        self.Label_time.grid(row=0, column=0, columnspan=5, stick='we')

        time = ('год', 'месяц', 'неделя', 'сутки', 'час', 'минута', 'секунда',
                'милисекунда')

        timeValue.trace('w', size_check)
        self.entry_time = Entry(self.mainPart, justify=RIGHT,
                                font=('Comic Sans', 15), width=8,
                                textvariable=timeValue)
        self.entry_time.grid(row=1, column=0)
        self.entry_time.insert(0, '0')

        self.combo_time1 = ttk.Combobox(self.mainPart, values=time)
        self.combo_time1.current(0)
        self.combo_time1.set('выберите значение>')
        self.combo_time1.grid(row=1, column=1, stick='wens')

        self.run_time = Button(self.mainPart, text='->',
                               bd=3, font=('Comic Sans', 10),
                               fg='red', bg='yellow',
                               command=lambda: self.get_value(
                                   [[1, 12, 365/7, 365, 8760, 525600,
                                     31536000, 31536000000],
                                    [1/12, 1, 365/84, 31, 744, 44640, 2678400,
                                     2678400000],
                                    [7/365, 84/365, 1, 7, 168, 10080, 604800,
                                     604800000],
                                    [1/365, 1/31, 1/7, 1, 24, 1440, 86400,
                                     86400000],
                                    [1/8760, 1/744, 1/168, 1/24, 1, 60, 3600,
                                     3600000],
                                    [1/525600, 1/44640, 1/10080, 1/1440, 1/60,
                                     1, 60, 60000],
                                    [1/31536000, 1/2678400, 1/604800, 1/86400,
                                     1/3600, 1/60, 1, 1000],
                                    [1/31536000000, 1/2678400000,
                                     1/604800000, 1/86400000, 1/3600000,
                                     1/60000, 1/1000, 1]], time,
                                   self.combo_time1, self.combo_time2,
                                   self.entry_time, self.outry_time,
                                   'normal'))
        self.run_time.grid(row=1, column=2, stick='wens')

        self.mainPart.grid_columnconfigure(2, minsize=20)

        self.outry_time = Entry(self.mainPart, justify=RIGHT,
                                font=('Comic Sans', 15), width=25)
        self.outry_time.insert(0, '0')
        self.outry_time['state'] = DISABLED
        self.outry_time.grid(row=1, column=3, stick='we')
        self.mainPart.grid_columnconfigure(3, minsize=20)

        self.combo_time2 = ttk.Combobox(self.mainPart, values=time)
        self.combo_time2.current(0)
        self.combo_time2.set('выберите значение>')
        self.combo_time2.grid(row=1, column=4, stick='wens')

        self.mainPart.grid_columnconfigure(5, minsize=40)

        # Создаем переводчик величин давления
        self.Label_bar = Label(self.mainPart, font=("Courier", 18),
                               text='Перевод величин давления')
        self.Label_bar.grid(row=0, column=6, columnspan=5, stick='we')

        bar = ('атмосфера', 'бар', 'мм.рт.ст', 'паскаль')

        barValue.trace('w', size_check)
        self.entry_bar = Entry(self.mainPart, justify=RIGHT,
                               font=('Comic Sans', 15), width=8,
                               textvariable=barValue)
        self.entry_bar.grid(row=1, column=6)
        self.entry_bar.insert(0, '0')

        self.combo_bar1 = ttk.Combobox(self.mainPart, values=bar)
        self.combo_bar1.current(0)
        self.combo_bar1.set('выберите значение>')
        self.combo_bar1.grid(row=1, column=7, stick='wens')

        self.run_bar = Button(self.mainPart, text='->',
                              bd=3, font=('Comic Sans', 10),
                              fg='red', bg='yellow',
                              command=lambda: self.get_value(
                                  [[1, 1.013, 760, 101325],
                                   [0.9869, 1, 750.1, 100000],
                                   [1/760, 0.001333, 1, 133.3],
                                   [0.000009869, 0.00001, 0.007501, 1]],
                                  bar, self.combo_bar1, self.combo_bar2,
                                  self.entry_bar, self.outry_bar, 'normal'))
        self.run_bar.grid(row=1, column=8, stick='wens')

        self.mainPart.grid_columnconfigure(8, minsize=20)

        self.outry_bar = Entry(self.mainPart, justify=RIGHT,
                               font=('Comic Sans', 15), width=25)
        self.outry_bar.insert(0, '0')
        self.outry_bar['state'] = DISABLED
        self.outry_bar.grid(row=1, column=9, stick='we')
        self.mainPart.grid_columnconfigure(9, minsize=20)

        self.combo_bar2 = ttk.Combobox(self.mainPart, values=bar)
        self.combo_bar2.current(0)
        self.combo_bar2.set('выберите значение>')
        self.combo_bar2.grid(row=1, column=10, stick='wens')

        self.mainPart.grid_rowconfigure(2, minsize=80)

        # Создаем переводчик величин длины
        self.Label_length = Label(self.mainPart, font=("Courier", 18),
                                  text='Перевод величин длины')
        self.Label_length.grid(row=3, column=0, columnspan=5, stick='we')

        length = ('световой год', 'а.е.', 'миля', 'ярд',
                  'фут', 'дюйм', 'километр', 'метр', 'сантиметр', 'милиметр')

        lengthValue.trace('w', size_check)
        self.entry_length = Entry(self.mainPart, justify=RIGHT,
                                  font=('Comic Sans', 15), width=8,
                                  textvariable=lengthValue)
        self.entry_length.grid(row=4, column=0)
        self.entry_length.insert(0, '0')

        self.combo_length1 = ttk.Combobox(self.mainPart, values=length)
        self.combo_length1.current(0)
        self.combo_length1.set('выберите значение>')
        self.combo_length1.grid(row=4, column=1, stick='wens')

        self.run_length = Button(self.mainPart, text='->',
                                 bd=3, font=('Comic Sans', 10),
                                 fg='red', bg='yellow',
                                 command=lambda: self.get_value(
                                   [[1, 63241, 5878625373184,
                                     10346380656803154,
                                     31039141970409428,
                                     3.7246970364491386e+17,
                                     9460730472581, 9460730472580760,
                                     9.46073047258076e+17,
                                     9.46073047258076e+18],
                                    [0.00001581, 1, 92955807, 163602220801,
                                     490806662402, 5889679948819,
                                     149597871, 149597870700,
                                     14959787070000, 149597870700000],
                                    [0.0000000000001701, 0.00000001076, 1,
                                     1760, 5280, 63360, 1.609, 1609, 160934,
                                     1609344],
                                    [9.665e-17, 0.000000000006112, 0.0005682,
                                     1, 3, 36, 0.0009144, 0.9144, 91.44,
                                     914.4],
                                    [3.222e-17, 0.000000000002037, 0.0001894,
                                     1/3, 1, 12, 0.0003048, 0.3048, 30.48,
                                     304.8],
                                    [2.685e-18, 0.0000000000001698,
                                     0.00001578, 0.02778, 0.08333, 1,
                                     0.0000254, 0.0254, 2.54, 25.4],
                                    [0.0000000000001057, 0.000000006685,
                                     0.6214, 1094, 3281, 39370, 1, 1000,
                                     100000, 1000000],
                                    [1.057e-16, 0.000000000006685,
                                     0.0006214, 1.094, 3.281,
                                     39.37, 0.001, 1, 100, 1000],
                                    [1.057e-18, 0.00000000000006685,
                                     0.000006214, 0.01094, 0.03281,
                                     0.3937, 0.00001, 0.01, 1, 10],
                                    [1.057e-19, 0.000000000000006685,
                                     0.0000006214, 0.001094, 0.003281,
                                     0.03937, 0.000001, 0.001, 0.1, 1]],
                                   length, self.combo_length1,
                                   self.combo_length2, self.entry_length,
                                   self.outry_length, 'long'))
        self.run_length.grid(row=4, column=2, stick='wens')

        self.outry_length = Entry(self.mainPart, justify=RIGHT,
                                  font=('Comic Sans', 15), width=25)
        self.outry_length.insert(0, '0')
        self.outry_length['state'] = DISABLED
        self.outry_length.grid(row=4, column=3, stick='we')

        self.combo_length2 = ttk.Combobox(self.mainPart, values=length)
        self.combo_length2.current(0)
        self.combo_length2.set('выберите значение>')
        self.combo_length2.grid(row=4, column=4, stick='wens')

        # Создаем переводчик величин массы
        self.Label_weigth = Label(self.mainPart, font=("Courier", 18),
                                  text='Перевод величин массы')
        self.Label_weigth.grid(row=3, column=6, columnspan=5, stick='we')

        weigth = ('тонна', 'килограмм', 'грамм', 'фунт', 'унция', 'пуд',
                  'а.е.м')

        weigthValue.trace('w', size_check)
        self.entry_weigth = Entry(self.mainPart, justify=RIGHT,
                                  font=('Comic Sans', 15), width=8,
                                  textvariable=weigthValue)
        self.entry_weigth.grid(row=4, column=6)
        self.entry_weigth.insert(0, '0')

        self.combo_weigth1 = ttk.Combobox(self.mainPart, values=weigth)
        self.combo_weigth1.current(0)
        self.combo_weigth1.set('выберите значение>')
        self.combo_weigth1.grid(row=4, column=7, stick='wens')

        self.run_weigth = Button(self.mainPart, text='->',
                                 bd=3, font=('Comic Sans', 10),
                                 fg='red', bg='yellow',
                                 command=lambda: self.get_value(
                                   [[1, 1000, 100000000, 2205, 35274, 55.37,
                                     6.022e+29],
                                    [0.001, 1, 1000, 2.205, 35.27, 0.06105,
                                     6.022e+26],
                                    [0.000001, 0.001, 1, 0.002205, 0.03527,
                                     0.00006105, 6.022e+23],
                                    [0.0004536, 0.4536, 453.6, 1, 16, 0.0277,
                                     2.732e+26],
                                    [0.00002835, 0.02835, 28.35, 0.0625, 1,
                                     0.00173, 1.707e+25],
                                    [0.01638, 16.38, 16380, 36.11, 577.8, 1,
                                     9.864e+27],
                                    [1.661e-30, 1.661e-27, 1.661e-24,
                                     3.661e-27, 5.857e-26, 1.01378e-28, 1]],
                                   weigth, self.combo_weigth1,
                                   self.combo_weigth2, self.entry_weigth,
                                   self.outry_weigth, 'long'))
        self.run_weigth.grid(row=4, column=8, stick='wens')

        self.outry_weigth = Entry(self.mainPart, justify=RIGHT,
                                  font=('Comic Sans', 15), width=25)
        self.outry_weigth.insert(0, '0')
        self.outry_weigth['state'] = DISABLED
        self.outry_weigth.grid(row=4, column=9, stick='we')

        self.combo_weigth2 = ttk.Combobox(self.mainPart, values=weigth)
        self.combo_weigth2.current(0)
        self.combo_weigth2.set('выберите значение>')
        self.combo_weigth2.grid(row=4, column=10, stick='wens')

        self.mainPart.grid_rowconfigure(5, minsize=80)

        # Создаем переводчик величин объёма
        self.Label_volume = Label(self.mainPart, font=("Courier", 18),
                                  text='Перевод величин объёма')
        self.Label_volume.grid(row=6, column=0, columnspan=5, stick='we')

        volume = ('кубический метр', 'кубический сантиметр',
                  'кубический милиметр', 'баррель', 'литр', 'милилитр')

        volumeValue.trace('w', size_check)
        self.entry_volume = Entry(self.mainPart, justify=RIGHT,
                                  font=('Comic Sans', 15), width=8,
                                  textvariable=volumeValue)
        self.entry_volume.grid(row=7, column=0)
        self.entry_volume.insert(0, '0')

        self.combo_volume1 = ttk.Combobox(self.mainPart, values=volume)
        self.combo_volume1.current(0)
        self.combo_volume1.set('выберите значение>')
        self.combo_volume1.grid(row=7, column=1, stick='wens')

        self.run_volume = Button(self.mainPart, text='->',
                                 bd=3, font=('Comic Sans', 10),
                                 fg='red', bg='yellow',
                                 command=lambda: self.get_value(
                                  [[1, 1000000, 1000000000, 6.29, 1000,
                                    1000000],
                                   [0.000001, 1, 1000, 0.00000629, 0.001, 1],
                                   [0.000000001, 0.001, 1, 0.00000000629,
                                    0.000001, 0.001],
                                   [0.159, 158987, 158987295, 1, 159, 158987],
                                   [0.001, 1000, 1000000, 0.00629, 1, 1000],
                                   [0.000001, 1, 1000, 0.00000629, 0.001, 1]],
                                  volume, self.combo_volume1,
                                  self.combo_volume2, self.entry_volume,
                                  self.outry_volume, 'normal+'))
        self.run_volume.grid(row=7, column=2, stick='wens')

        self.outry_volume = Entry(self.mainPart, justify=RIGHT,
                                  font=('Comic Sans', 15), width=25)
        self.outry_volume.insert(0, '0')
        self.outry_volume['state'] = DISABLED
        self.outry_volume.grid(row=7, column=3, stick='we')

        self.combo_volume2 = ttk.Combobox(self.mainPart, values=volume)
        self.combo_volume2.current(0)
        self.combo_volume2.set('выберите значение>')
        self.combo_volume2.grid(row=7, column=4, stick='wens')

        # Создаем переводчик величин площади
        self.Label_area = Label(self.mainPart, font=("Courier", 18),
                                text='Перевод величин площади')
        self.Label_area.grid(row=6, column=6, columnspan=5, stick='we')

        area = ('квадратный метр', 'квадратный сантиметр',
                'квадратный милиметр', 'ар', 'гектар')

        areaValue.trace('w', size_check)
        self.entry_area = Entry(self.mainPart, justify=RIGHT,
                                font=('Comic Sans', 15), width=8,
                                textvariable=areaValue)
        self.entry_area.grid(row=7, column=6)
        self.entry_area.insert(0, '0')

        self.combo_area1 = ttk.Combobox(self.mainPart, values=area)
        self.combo_area1.current(0)
        self.combo_area1.set('выберите значение>')
        self.combo_area1.grid(row=7, column=7, stick='wens')

        self.run_area = Button(self.mainPart, text='->',
                               bd=3, font=('Comic Sans', 10),
                               fg='red', bg='yellow',
                               command=lambda: self.get_value(
                                  [[1, 10000, 1000000, 0.01, 0.0001],
                                   [0.0001, 1, 100, 0.000001, 0.00000001],
                                   [0.000001, 0.01, 1, 0.00000001,
                                    0.0000000001],
                                   [100, 1000000, 100000000, 1, 0.01],
                                   [10000, 100000000, 10000000000, 100, 1]],
                                  area, self.combo_area1, self.combo_area2,
                                  self.entry_area, self.outry_area,
                                  'normal+'))
        self.run_area.grid(row=7, column=8, stick='wens')

        self.outry_area = Entry(self.mainPart, justify=RIGHT,
                                font=('Comic Sans', 15), width=25)
        self.outry_area.insert(0, '0')
        self.outry_area['state'] = DISABLED
        self.outry_area.grid(row=7, column=9, stick='we')

        self.combo_area2 = ttk.Combobox(self.mainPart, values=area)
        self.combo_area2.current(0)
        self.combo_area2.set('выберите значение>')
        self.combo_area2.grid(row=7, column=10, stick='wens')

        self.mainPart.grid_rowconfigure(8, minsize=80)

        # Создаем переводчик величин скорости
        self.Label_speed = Label(self.mainPart, font=("Courier", 18),
                                 text='Перевод величин скорости')
        self.Label_speed.grid(row=9, column=0, columnspan=5, stick='we')

        speed = ('километр в час', 'метр в секунду', 'миля в час', 'узел',
                 'скорость светав вакууме')

        speedValue.trace('w', size_check)
        self.entry_speed = Entry(self.mainPart, justify=RIGHT,
                                 font=('Comic Sans', 15), width=8,
                                 textvariable=speedValue)
        self.entry_speed.grid(row=10, column=0)
        self.entry_speed.insert(0, '0')

        self.combo_speed1 = ttk.Combobox(self.mainPart, values=speed)
        self.combo_speed1.current(0)
        self.combo_speed1.set('выберите значение>')
        self.combo_speed1.grid(row=10, column=1, stick='wens')

        self.run_speed = Button(self.mainPart, text='->',
                                bd=3, font=('Comic Sans', 10),
                                fg='red', bg='yellow',
                                command=lambda: self.get_value(
                                     [[1, 1/3.6, 0.6214, 0.54,
                                       0.0000000009266],
                                      [3.6, 1, 2.237, 1.944, 0.000000003336],
                                      [1.609, 0.447, 1, 0.869, 0.00000000149],
                                      [1.852, 0.5144, 1.151, 1,
                                       0.000000001716],
                                      [1079252850, 299792454, 670616643,
                                       582749904, 1]], speed,
                                     self.combo_speed1, self.combo_speed2,
                                     self.entry_speed, self.outry_speed,
                                     'normal+'))

        self.run_speed.grid(row=10, column=2, stick='wens')

        self.outry_speed = Entry(self.mainPart, justify=RIGHT,
                                 font=('Comic Sans', 15), width=25)
        self.outry_speed.insert(0, '0')
        self.outry_speed['state'] = DISABLED
        self.outry_speed.grid(row=10, column=3, stick='we')

        self.combo_speed2 = ttk.Combobox(self.mainPart, values=speed)
        self.combo_speed2.current(0)
        self.combo_speed2.set('выберите значение>')
        self.combo_speed2.grid(row=10, column=4, stick='wens')

        # Создаем переводчик величин температуры
        self.Label_temp = Label(self.mainPart, font=("Courier", 18),
                                text='Перевод величин температуры')
        self.Label_temp.grid(row=9, column=6, columnspan=5, stick='we')

        temp = ('градус Цельсия', 'градус Фаренгейта', 'Кельвин')

        tempValue.trace('w', size_check)
        self.entry_temp = Entry(self.mainPart, justify=RIGHT,
                                font=('Comic Sans', 15), width=8,
                                textvariable=tempValue)
        self.entry_temp.grid(row=10, column=6)
        self.entry_temp.insert(0, '0')

        self.combo_temp1 = ttk.Combobox(self.mainPart, values=temp)
        self.combo_temp1.current(0)
        self.combo_temp1.set('выберите значение>')
        self.combo_temp1.grid(row=10, column=7, stick='wens')

        self.run_temp = Button(self.mainPart, text='->',
                               bd=3, font=('Comic Sans', 10),
                               fg='red', bg='yellow',
                               command=lambda: self.temp_convers(
                                   temp,
                                   self.combo_temp1,
                                   self.combo_temp2,
                                   self.entry_temp,
                                   self.outry_temp))
        self.run_temp.grid(row=10, column=8, stick='wens')

        self.outry_temp = Entry(self.mainPart, justify=RIGHT,
                                font=('Comic Sans', 15), width=25)
        self.outry_temp.insert(0, '0')
        self.outry_temp['state'] = DISABLED
        self.outry_temp.grid(row=10, column=9, stick='we')

        self.combo_temp2 = ttk.Combobox(self.mainPart, values=temp)
        self.combo_temp2.current(0)
        self.combo_temp2.set('выберите значение>')
        self.combo_temp2.grid(row=10, column=10, stick='wens')

        self.mainPart.grid_rowconfigure(11, minsize=80)

        # Создаем переводчик величин энергии
        self.Label_energy = Label(self.mainPart, font=("Courier", 18),
                                  text='Перевод величин энергии')
        self.Label_energy.grid(row=12, column=0, columnspan=5, stick='we')

        energy = ('джоуль', 'калория', 'килокалория')

        energyValue.trace('w', size_check)
        self.entry_energy = Entry(self.mainPart, justify=RIGHT,
                                  font=('Comic Sans', 15), width=8,
                                  textvariable=energyValue)
        self.entry_energy.grid(row=13, column=0)
        self.entry_energy.insert(0, '0')

        self.combo_energy1 = ttk.Combobox(self.mainPart, values=energy)
        self.combo_energy1.current(0)
        self.combo_energy1.set('выберите значение>')
        self.combo_energy1.grid(row=13, column=1, stick='wens')

        self.run_energy = Button(self.mainPart, text='->',
                                 bd=3, font=('Comic Sans', 10),
                                 fg='red', bg='yellow',
                                 command=lambda: self.get_value(
                                    [[1, 0.2388, 0.0002388],
                                     [4.187, 1, 0.001],
                                     [4187, 1000, 1]], energy,
                                    self.combo_energy1, self.combo_energy2,
                                    self.entry_energy, self.outry_energy,
                                    'normal'))

        self.run_energy.grid(row=13, column=2, stick='wens')

        self.outry_energy = Entry(self.mainPart, justify=RIGHT,
                                  font=('Comic Sans', 15), width=25)
        self.outry_energy.insert(0, '0')
        self.outry_energy['state'] = DISABLED
        self.outry_energy.grid(row=13, column=3, stick='we')

        self.combo_energy2 = ttk.Combobox(self.mainPart, values=energy)
        self.combo_energy2.current(0)
        self.combo_energy2.set('выберите значение>')
        self.combo_energy2.grid(row=13, column=4, stick='wens')

        # Вывод поля и фрейма
        self.mainPart.pack()

        # Изменение парметров окна
        self.parent.resizable(width=False, height=False)
        self.parent.attributes('-fullscreen', True)
        # Изменение цвета приложения
        for wid in self.parent.winfo_children():
            wid.configure(bg='#00ace6')
        self.parent["bg"] = '#00ace6'
        self.back["bg"] = "#e0e0e0"

    # Возврат назад
    def returnBack(self):
        self.parent.destroy()

    # Выполнение перевода величины
    def get_value(self, koeff, names, combo_name1, combo_name2, entry_name,
                  outry_name, round):
        value1 = combo_name1.get()
        value2 = combo_name2.get()
        num = entry_name.get()
        namesDigit = {
            'год': 0,
            'месяц': 1,
            'неделя': 2,
            'сутки': 3,
            'час': 4,
            'минута': 5,
            'секунда': 6,
            'милисекунда': 7,

            'атмосфера': 0,
            'бар': 1,
            'мм.рт.ст': 2,
            'паскаль': 3,

            'световой год': 0,
            'а.е.': 1,
            'миля': 2,
            'ярд': 3,
            'фут': 4,
            'дюйм': 5,
            'километр': 6,
            'метр': 7,
            'сантиметр': 8,
            'милиметр': 9,

            'тонна': 0,
            'килограмм': 1,
            'грамм': 2,
            'фунт': 3,
            'унция': 4,
            'пуд': 5,
            'а.е.м': 6,

            'кубический метр': 0,
            'кубический сантиметр': 1,
            'кубический милиметр': 2,
            'баррель': 3,
            'литр': 4,
            'милилитр': 5,

            'квадратный метр': 0,
            'квадратный сантиметр': 1,
            'квадратный милиметр': 2,
            'ар': 3,
            'гектар': 4,

            'километр в час': 0,
            'метр в секунду': 1,
            'миля в час': 2,
            'узел': 3,
            'скорость светав вакууме': 4,

            'джоуль': 0,
            'калория': 1,
            'килокалория': 2,
        }
        if (value1 in names) and (value2 in names):
            try:
                float(num)
                if round == 'normal':
                    result = str(float('{:.7f}'.format((float(num) *
                                 koeff[namesDigit[value1]][namesDigit[value2]]
                                 ))))
                elif round == 'long':
                    result = str(float('{:.22f}'.format((float(num) *
                                 koeff[namesDigit[value1]][namesDigit[value2]]
                                 ))))
                elif round == 'normal+':
                    result = str(float('{:.11f}'.format((float(num) *
                                 koeff[namesDigit[value1]][namesDigit[value2]]
                                 ))))
                if len(result) > 2:
                    if (result[-1] == '0') and (result[-2] == '.'):
                        res = int(float(result))
                    else:
                        if int(float(result)) == float(result):
                            res = int(float(result))
                        else:
                            res = float(result)
                else:
                    res = int(float(result))
                if ((value1 == 'а.е.м') or (value2 == 'а.е.м')) and \
                        (float(num) >= 10):
                    res = ('{:e}'.format(res))
                outry_name['state'] = NORMAL
                outry_name.delete(0, 'end')
                outry_name.insert(0, res)
                outry_name['state'] = DISABLED
            except ValueError:
                messagebox.showerror(
                    'Ошибка',
                    'Можно вводить только числа или десятичные дроби')
                self.parent.attributes('-topmost', True)
                self.parent.update()
                self.parent.attributes('-topmost', False)
                self.parent.update()

    def temp_convers(self, names, combo_name1, combo_name2, entry_name,
                     outry_name):
        value1 = combo_name1.get()
        value2 = combo_name2.get()
        num = entry_name.get()
        if (value1 in names) and (value2 in names):
            try:
                float(num)
                if value1 == 'градус Цельсия':
                    if value2 == 'градус Цельсия':
                        result = str(float(num))
                    elif value2 == 'градус Фаренгейта':
                        result = str(float(num)*9/5 + 32)
                    elif value2 == 'Кельвин':
                        result = str(float(num) + 273.15)
                elif value1 == 'градус Фаренгейта':
                    if value2 == 'градус Цельсия':
                        result = str((float(num) - 32)*5/9)
                    elif value2 == 'градус Фаренгейта':
                        result = str(float(num))
                    elif value2 == 'Кельвин':
                        result = str((float(num) - 32)*5/9 + 273.15)
                elif value1 == 'Кельвин':
                    if value2 == 'градус Цельсия':
                        result = str(float(num) - 273.15)
                    elif value2 == 'градус Фаренгейта':
                        result = str((float(num) - 273.15)*9/5 + 32)
                    elif value2 == 'Кельвин':
                        result = str(float(num))
                if len(result) > 2:
                    if (result[-1] == '0') and (result[-2] == '.'):
                        res = int(float(result))
                    else:
                        res = float(result)
                else:
                    res = int(float(result))
                try:
                    int(str(res))
                except ValueError:
                    res = ('{:.2f}'.format(res))
                outry_name['state'] = NORMAL
                outry_name.delete(0, 'end')
                outry_name.insert(0, res)
                outry_name['state'] = DISABLED
            except ValueError:
                messagebox.showerror(
                    'Ошибка',
                    'Можно вводить только числа или десятичные дроби')
                self.parent.attributes('-topmost', True)
                self.parent.update()
                self.parent.attributes('-topmost', False)
                self.parent.upаdate()
