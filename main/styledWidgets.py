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
            self.config(show='')


# Измененная кнопка
class HoverButton(Button):
    def __init__(self, master, description=False, descriptionText='', **kw):
        Button.__init__(self, master=master, overrelief=GROOVE, **kw)
        self.defaultBackground = self["background"]
        self.description = description
        if self.description:
            self.toolTip = ToolTip(self)
        self.descriptionText = descriptionText
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']
        if self.description:
            self.toolTip.showtip(self.descriptionText)

    def on_leave(self, e):
        self['background'] = self.defaultBackground
        if self.description:
            self.toolTip.hidetip()


# Создание виджета с описанием
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None

    def showtip(self, text):
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 187
        y = y + cy + self.widget.winfo_rooty() + 127
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "20", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
