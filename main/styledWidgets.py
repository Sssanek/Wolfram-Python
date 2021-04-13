from tkinter import *


# Измененное поле ввода c подсказками
class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder=None, hideChar=False, **p):
        super().__init__(master, **p)
        self.master = master
        # Символы для пароля
        self.hideChar = hideChar

        # Если есть подсказка
        if placeholder is not None:
            self.placeholder = placeholder
            self.placeholder_color = 'grey'
            self.default_fg_color = self['fg']

            # Вызов функций при нажатии и отжатии поля ввода
            self.bind("<FocusIn>", self.focus_in)
            self.bind("<FocusOut>", self.focus_out)

            self.put_placeholder()

    # Надпись в поле ввода
    def put_placeholder(self):
        self.delete(0, 'end')
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    # Метод для очистки поля и замены сиволов при надобности
    def focus_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color
            if self.hideChar:
                self.config(show='*')
                self.master.update()

    # Метод для вывода подсказки
    def focus_out(self, *args):
        # Если в поле пусто
        if not self.get():
            self.put_placeholder()
            self.config(show='')


# Измененная кнопка
class HoverButton(Button):
    def __init__(self, master, description=False, descriptionText='', **kw):
        Button.__init__(self, master=master, overrelief=GROOVE, **kw)
        self.defaultBackground = self["background"]
        # Перемення для проверки есть ли пояснение
        self.description = description
        if self.description:
            # Виджет для пояснения
            self.toolTip = ToolTip(self)
        # Текст пояснение
        self.descriptionText = descriptionText
        # Метод при наведии
        self.bind("<Enter>", self.on_enter)
        # Метод при отведении курсора от кнопки
        self.bind("<Leave>", self.on_leave)

    # Пояснение при наведении
    def on_enter(self, e):
        self['background'] = self['activebackground']
        if self.description:
            self.toolTip.showtip(self.descriptionText)

    # Удаление пояснения
    def on_leave(self, e):
        self['background'] = self.defaultBackground
        if self.description:
            self.toolTip.hidetip()


# Создание виджета с описанием
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None

    # Создание текста
    def showtip(self, text):
        self.text = text
        if self.tipwindow or not self.text:
            return
        # Координаты относительно кнопки
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 187
        y = y + cy + self.widget.winfo_rooty() + 127
        # Вывести над всеми окнами
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        # Вывод поля на экран
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "20", "normal"))
        label.pack(ipadx=1)

    # Скрыть описание
    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
