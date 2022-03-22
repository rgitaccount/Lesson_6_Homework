
class Data:
    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value


classes_list = []

with open("MOCK_DATA.txt") as file:
    names = file.read().splitlines()
    for line in names:
        color = line.split('\t')[-1]
        file_name = line.split('\t')[-2]
        email = line.split('\t')[-3]
        full_name = ' '.join(line.split('\t')[0:-3])
        classes_list.append(Data(full_name, email, file_name, color))

attributes = [a for a in dir(Data) if not a.startswith('__')]

for attribute in attributes:
    with open(f"{attribute}.txt", mode="w") as file:
        text = ''
        for row in classes_list:
            text += getattr(row, attribute)+'\n'
        file.write(text)

