from tkinter import *
from main.styledWidgets import HoverButton, EntryWithPlaceholder
from main.RandomOperations import one_ravn, one_norm, one_log, one_beta
from main.RandomOperations import one_exp, one_gauss
from main.RandomExport import export_ravn, export_norm, export_log
from main.RandomExport import export_beta, export_exp, export_gauss


class RandomGenerator(Frame):
    def __init__(self, parent):
        # Объявление переменных
        self.parent = parent
        self.font30 = ("Courier", 30)
        self.font20 = ("Courier", 20)
        self.dimensions = 'three'
        self.push_color = '#cf34eb'
        self.bg_color = '#00ace6'
        self.width = 22
        # Основной фрейм
        self.mainPart = Frame(self.parent)

        # Кнопка возврата назад
        self.back = HoverButton(
            self.parent,
            font=("Courier", 18),
            text='Назад',
            activebackground='#00ff00',
            command=self.return_back
        )
        self.back.pack(anchor=NW, padx=20, pady=20)
        # равномерное распределение (соответствующие виджеты)
        self.l_ravn = Label(
            self.mainPart,
            text="Равномерное распределение\na <= n <= b",
            font=self.font20,
            bg=self.bg_color
        )
        self.a_ravn = EntryWithPlaceholder(
            self.mainPart,
            'Левая граница (a)',
            font=self.font20,
            width=self.width
        )
        self.b_ravn = EntryWithPlaceholder(
            self.mainPart,
            'Правая граница (b)',
            font=self.font20,
            width=self.width
        )
        self.gen_ravn = HoverButton(
            self.mainPart,
            font=self.font20,
            text='Сгенерировать значение',
            activebackground=self.push_color,
            command=lambda: self.generate_ravn()
        )
        self.export_ravn = HoverButton(
            self.mainPart,
            font=self.font20,
            text='Выгрузить данные\nв формате csv',
            activebackground=self.push_color,
            command=lambda: self.ravn_to_csv()
        )
        # нормальное распределение (соответствующие виджеты)
        self.l_norm = Label(
            self.mainPart,
            text='Нормальное распределение',
            font=self.font20,
            bg=self.bg_color
        )
        self.mu_norm = EntryWithPlaceholder(
            self.mainPart,
            'Cреднее значение (mu)',
            font=self.font20,
            width=self.width,
        )
        self.sigma_norm = EntryWithPlaceholder(
            self.mainPart,
            'Стандартное отклонение (sigma)',
            font=self.font20,
            width=self.width
        )
        self.gen_norm = HoverButton(
            self.mainPart,
            font=self.font20,
            text='Сгенерировать значение',
            activebackground=self.push_color,
            command=lambda: self.generate_norm()
        )
        self.export_norm = HoverButton(
            self.mainPart,
            font=self.font20,
            text='Выгрузить данные\nв формате csv',
            activebackground=self.push_color,
            command=lambda: self.norm_to_csv()
        )
        # логарифм нормального распределения (соответствующие виджеты)
        self.l_lognorm = Label(
            self.mainPart,
            text='Логарифм нормального распределения',
            font=self.font20,
            bg=self.bg_color
        )
        self.mu_lognorm = EntryWithPlaceholder(
            self.mainPart,
            'Cреднее значение (mu)',
            font=self.font20,
            width=self.width,
        )
        self.sigma_lognorm = EntryWithPlaceholder(
            self.mainPart,
            'Стандартное отклонение (sigma)',
            font=self.font20,
            width=self.width
        )
        self.gen_lognorm = HoverButton(
            self.mainPart,
            font=self.font20,
            text='Сгенерировать значение',
            activebackground=self.push_color,
            command=lambda: self.generate_log()
        )
        self.export_lognorm = HoverButton(
            self.mainPart,
            font=self.font20,
            text='Выгрузить данные\nв формате csv',
            activebackground=self.push_color,
            command=lambda: self.log_to_csv()
        )
        # бета распределение (соответствующие виджеты)
        self.l_beta = Label(
            self.mainPart,
            text='Бета распределение (от 0 до 1)',
            font=self.font20,
            bg=self.bg_color
        )
        self.alpha_beta = EntryWithPlaceholder(
            self.mainPart,
            'alpha>0',
            font=self.font20,
            width=self.width,
        )
        self.beta_beta = EntryWithPlaceholder(
            self.mainPart,
            'beta>0',
            font=self.font20,
            width=self.width
        )
        self.gen_beta = HoverButton(
            self.mainPart,
            font=self.font20,
            text='Сгенерировать значение',
            activebackground=self.push_color,
            command=lambda: self.generate_beta()
        )
        self.export_beta = HoverButton(
            self.mainPart,
            font=self.font20,
            text='Выгрузить данные\nв формате csv',
            activebackground=self.push_color,
            command=lambda: self.beta_to_csv()
        )
        # экспоненциальное распределение (соответствующие виджеты)
        self.l_exp = Label(
            self.mainPart,
            text='Экспоненциальное распределение\n(от 0 до +∞, если λ>0 '
                 'и\nот 0 до -∞, если λ<0)',
            font=self.font20,
            bg=self.bg_color
        )
        self.lambd_exp = EntryWithPlaceholder(
            self.mainPart,
            'λ=1/среднее желаемое',
            font=self.font20,
            width=self.width,
        )
        self.gen_exp = HoverButton(
            self.mainPart,
            font=self.font20,
            text='Сгенерировать значение',
            activebackground=self.push_color,
            command=lambda: self.generate_exp()
        )
        self.export_exp = HoverButton(
            self.mainPart,
            font=self.font20,
            text='Выгрузить данные\nв формате csv',
            activebackground=self.push_color,
            command=lambda: self.exp_to_csv()
        )
        # распределение Гаусса (соответствующие виджеты)
        self.l_gauss = Label(
            self.mainPart,
            text='Распределение Гаусса',
            font=self.font20,
            bg=self.bg_color
        )
        self.x_gauss = EntryWithPlaceholder(
            self.mainPart,
            'значение',
            font=self.font20,
            width=self.width,
        )
        self.dx_gauss = EntryWithPlaceholder(
            self.mainPart,
            'стандартное отклонение',
            font=self.font20,
            width=self.width
        )
        self.gen_gauss = HoverButton(
            self.mainPart,
            font=self.font20,
            text='Сгенерировать значение',
            activebackground=self.push_color,
            command=lambda: self.generate_gauss()
        )
        self.export_gauss = HoverButton(
            self.mainPart,
            font=self.font20,
            text='Выгрузить данные\nв формате csv',
            activebackground=self.push_color,
            command=lambda: self.gauss_to_csv()
        )
        # вся информация про выгрузку csv (соответствующие виджеты)
        self.csv_info = Label(
            self.mainPart,
            text='Данные для выгрузки в csv:',
            font=self.font30,
            bg=self.bg_color
        )
        self.l_cols = Label(
            self.mainPart,
            text='Размерность(столбцы):',
            font=self.font30,
            bg=self.bg_color
        )
        self.l_rows = Label(
            self.mainPart,
            text='Объем(строки):',
            font=self.font30,
            bg=self.bg_color
        )
        self.num_cols = EntryWithPlaceholder(
            self.mainPart,
            'n',
            font=self.font30,
            width=6
        )
        self.num_rows = EntryWithPlaceholder(
            self.mainPart,
            'm',
            font=self.font30,
            width=6
        )
        self.result = Label(
            self.mainPart,
            text='Результат',
            font=self.font30,
            bg="light green"
        )
        # ставлю основной фрейм, чтобы далее работать на нем
        self.mainPart.pack()
        # размещаю сетку элементов на фрейме
        # размещаю равномерное распределение
        self.l_ravn.grid(row=0, column=0, padx=10, pady=10)
        self.a_ravn.grid(row=0, column=1, padx=10, pady=10)
        self.b_ravn.grid(row=0, column=2, padx=10, pady=10)
        self.gen_ravn.grid(row=0, column=3, padx=10, pady=10)
        self.export_ravn.grid(row=0, column=4, padx=10, pady=10)
        # размещаю нормальное распределение
        self.l_norm.grid(row=1, column=0, padx=10, pady=10)
        self.mu_norm.grid(row=1, column=1, padx=10, pady=10)
        self.sigma_norm.grid(row=1, column=2, padx=10, pady=10)
        self.gen_norm.grid(row=1, column=3, padx=10, pady=10)
        self.export_norm.grid(row=1, column=4, padx=10, pady=10)
        # размещаю логарифм нормального распредления
        self.l_lognorm.grid(row=2, column=0, padx=10, pady=10)
        self.mu_lognorm.grid(row=2, column=1, padx=10, pady=10)
        self.sigma_lognorm.grid(row=2, column=2, padx=10, pady=10)
        self.gen_lognorm.grid(row=2, column=3, padx=10, pady=10)
        self.export_lognorm.grid(row=2, column=4, padx=10, pady=10)
        # размещаю бета-распределение
        self.l_beta.grid(row=3, column=0, padx=10, pady=10)
        self.alpha_beta.grid(row=3, column=1, padx=10, pady=10)
        self.beta_beta.grid(row=3, column=2, padx=10, pady=10)
        self.gen_beta.grid(row=3, column=3, padx=10, pady=10)
        self.export_beta.grid(row=3, column=4, padx=10, pady=10)
        # размещаю экспоненциальное распределение
        self.l_exp.grid(row=4, column=0, padx=10, pady=10)
        self.lambd_exp.grid(row=4, column=1, padx=10, pady=10)
        self.gen_exp.grid(row=4, column=3, padx=10, pady=10)
        self.export_exp.grid(row=4, column=4, padx=10, pady=10)
        # размещаю распределение Гаусса
        self.l_gauss.grid(row=5, column=0, padx=10, pady=10)
        self.x_gauss.grid(row=5, column=1, padx=10, pady=10)
        self.dx_gauss.grid(row=5, column=2, padx=10, pady=10)
        self.gen_gauss.grid(row=5, column=3, padx=10, pady=10)
        self.export_gauss.grid(row=5, column=4, padx=10, pady=10)
        # размещаю все что связано с csv
        self.csv_info.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        self.l_cols.grid(row=7, column=0, pady=10)
        self.l_rows.grid(row=8, column=0, pady=10)
        self.num_cols.grid(row=7, column=1, pady=10)
        self.num_rows.grid(row=8, column=1, pady=10)
        self.result.grid(row=7, column=3, padx=10, pady=10, columnspan=2,
                         rowspan=2)
        # Изменение парметров окна
        self.parent.resizable(width=False, height=False)
        self.parent.attributes('-fullscreen', True)
        # Изменение цвета приложения
        for wid in self.parent.winfo_children():
            wid.configure(bg=self.bg_color)
        self.parent["bg"] = self.bg_color
        self.back["bg"] = "#e0e0e0"

    # Возврат назад
    def return_back(self):
        self.parent.destroy()

    # функции для вызова логических функций из другого файла
    def generate_ravn(self):
        self.result['text'] = one_ravn(self.a_ravn.get(),
                                       self.b_ravn.get())

    def generate_norm(self):
        self.result['text'] = one_norm(self.mu_norm.get(),
                                       self.sigma_norm.get())

    def generate_log(self):
        self.result['text'] = one_log(self.mu_lognorm.get(),
                                      self.sigma_lognorm.get())

    def generate_beta(self):
        self.result['text'] = one_beta(self.alpha_beta.get(),
                                       self.beta_beta.get())

    def generate_exp(self):
        self.result['text'] = one_exp(self.lambd_exp.get())

    def generate_gauss(self):
        self.result['text'] = one_gauss(self.x_gauss.get(),
                                        self.dx_gauss.get())

    # экспорт рандомных чисел происходит через отдельное окошко
    def ravn_to_csv(self):
        self.result['text'] = export_ravn(self.num_rows.get(),
                                          self.num_cols.get(),
                                          self.a_ravn.get(),
                                          self.b_ravn.get())
        # возвращаем обратно на окно приложения
        self.mainPart.focus_set()

    def norm_to_csv(self):
        self.result['text'] = export_norm(self.num_rows.get(),
                                          self.num_cols.get(),
                                          self.mu_norm.get(),
                                          self.sigma_norm.get())
        self.mainPart.focus_set()

    def log_to_csv(self):
        self.result['text'] = export_log(self.num_rows.get(),
                                         self.num_cols.get(),
                                         self.mu_lognorm.get(),
                                         self.sigma_lognorm.get())
        self.mainPart.focus_set()

    def beta_to_csv(self):
        self.result['text'] = export_beta(self.num_rows.get(),
                                          self.num_cols.get(),
                                          self.alpha_beta.get(),
                                          self.beta_beta.get())
        self.mainPart.focus_set()

    def exp_to_csv(self):
        self.result['text'] = export_exp(self.num_rows.get(),
                                         self.num_cols.get(),
                                         self.lambd_exp.get())
        self.mainPart.focus_set()

    def gauss_to_csv(self):
        self.result['text'] = export_gauss(self.num_rows.get(),
                                           self.num_cols.get(),
                                           self.x_gauss.get(),
                                           self.dx_gauss.get())
        self.mainPart.focus_set()
