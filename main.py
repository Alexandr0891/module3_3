# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#                1.Функция с параметрами по умолчанию:
#          Создаem функцию print_params(a = 1, b = 'строка', c = True),
#          которая принимает три параметра со значениями по умолчанию
def print_params(a=1,b='строка',c=True):
    print(a,b,c)

#     Вызовaem функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params()
print_params(a=55,b=5,c=4)

print_params('n',True,1)
print_params(11,'sms',[12,'mode',True])
print_params(b=25)
print_params(c = [1,2,3])
#               2.Распаковка параметров:
values_list = [ 25,'Moskau',True]  #Создаем список values_list с тремя элементами разных типов
values_dict = {'a' : 45 ,'b' :'Бит','c':False} #Создаём словарь values_dict с тремя ключами, соответствующими
                                               # параметрам функции print_params, и значениями разных типов
#Передаём values_list и values_dict в функцию print_params, используя распаковку параметров
# (* для списка и ** для словаря).
print_params(*values_list)
print_params(**values_dict)
#             3.Распаковка + отдельные параметры:
values_list_2 = [10,'Navigator']
print_params(*values_list_2, 42)