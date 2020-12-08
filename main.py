"""головний модуль додатку
виводить розрахункову таблицю, зберігає результати в файл
показує на екрані первинні дані
"""
from os import system  
from process_data import create_zayavka_list
from data_service import show_zamovlennya, show_dovidnk, get_zamovlennya, get_dovidnk

MAIN_MENU = \
"""
~~~~~~~~~~~~~~~~ ОБРОБКА ЗАЯВОК НА УСТАТКУВАННЯ ~~~~~~~~~~~~~~~~
1 - вивід заявок на екран 
2 - запис заявок в файл
3 - вивід списка накладних
4 - вивід списка клієнтів
0 - завершення роботи
-----------------------------------------------
"""
STOP_MESSAGE = 'Для продовження нажмить <Enter>'

TITLE = "ЗАЯВКА НА ПРОДАЖ УСТАТКУВАННЯ"
HEADER = \
"""
=================================================================
Найменування         |  Номер заказа | Код клієнта | Ціна | Сума    
=================================================================
"""
FOOTER = \
"""
=================================================================
"""


def show_table_on_screen(zayavka_list):
    """Вивід таблиці заявок на екран

    Args:
        zayavka_list ([type]): список заявок
    """
    print(f"\n{TITLE}")
    print(HEADER)
    
    for zayavka in zayavka_list:
        print(f"{zayavka['namet_name']:20}",    
              f"{zayavka['order_number']:^20}", 
              f"{zayavka['kodk_name']:10}",    
              f"{zayavka['kol']:>10}",       
              f"{zayavka['cena']:>10.2f}",   
              f"{zayavka['summa']:>10.2f}",   
              )

print(FOOTER)       
def write_zayavka(zayavka_list):
    """записуємо масив заявок в файл

    Args:
    zayavka_list([type]): Список заявок
    """
    with open('./data/zayavka.txt', "w") as zayavka_file:
        for zayavka in zayavka_list:
            line = \
                zayavka['namet_name'] + ';' +  \
                str(zayavka['order_number']) + ';' + \
                str(zayavka['kodk_number']) + ';' + \
                str(zayavka['kol']) + ';' + \
                str(zayavka['cena']) + ';' + \
                str(zayavka['summa']) + '\n'

            zayavka_file.write(line)
        print("Файл сформовано ...")


while True:
   # Виводить головне меню 
   system('clear')
   print(MAIN_MENU) 
   command_number = input("Введіть номер команди: ")

   if command_number == '0':
        print('\nПрограма завершила роботу')
        exit(0)

   elif command_number == '1':
       zayavka_list = create_zayavka_list()
       show_table_on_screen(zayavka_list)
       input(STOP_MESSAGE)

   elif command_number == '2':
        zayavka_list = create_zayavka_list()
        write_zayavka(zayavka_list)
        input(STOP_MESSAGE)

   elif command_number == '3':
       zamovlennya = get_zamovlennya()
       show_zamovlennya(zamovlennya)
       input(STOP_MESSAGE)

   elif command_number == '4':
       dovidnk = get_dovidnk()
       show_dovidnk(dovidnk)
       input(STOP_MESSAGE)  
                  
