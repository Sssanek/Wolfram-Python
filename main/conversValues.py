from tkinter import StringVar


class values:
    # Создание переменных для величин переводчиков
    def __init__(self):
        self.timeValue = StringVar()
        self.barValue = StringVar()
        self.lengthValue = StringVar()
        self.weigthValue = StringVar()
        self.volumeValue = StringVar()
        self.areaValue = StringVar()
        self.speedValue = StringVar()
        self.tempValue = StringVar()
        self.energyValue = StringVar()

    # Ограничение ввода величин до 8 символов
    def size_check(self, *args):
        for name in (self.timeValue, self.barValue, self.lengthValue,
                     self.weigthValue, self.volumeValue, self.areaValue,
                     self.speedValue, self.tempValue, self.energyValue):
            value = name.get()
            if len(value) > 1:
                if ((value[0] == '0') and (value[1] == '0')) or ((
                        value[0] == '0') and (value[1] != '.')):
                    name.set(value[1:])
            if len(value) > 8:
                name.set(value[:8])
