from tkinter import *


# Измененное поле ввода
class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder=None, hideChar=False, **p):
        super().__init__(master, p)
        self.master = master
        self.hideChar = hideChar

        if placeholder is not None:
            self.placeholder = placeholder
            self.placeholder_color = 'grey'
            self.default_fg_color = self['fg']

            self.bind("<FocusIn>", self.focus_in)
            self.bind("<FocusOut>", self.focus_out)

            self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def focus_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color
            if self.hideChar:
                self.config(show='*')
                self.master.update()

    def focus_out(self, *args):
        if not self.get():
            self.put_placeholder()


# Измененная кнопка
class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self, master=master, overrelief=GROOVE, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground


class App(Frame):
    def __init__(self, parent, db):
        self.parent = parent
        self.db = db
        self.label = Label(text='Ну типа приложение')
        Label(self.parent, text='Themed Label').pack()
        self.label.pack()
