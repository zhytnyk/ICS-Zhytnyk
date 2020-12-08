""" модуль для доступу до вхідних даних
"""

def get_zamovlennya():
    """отримує данні по замовленням

    Returns:
        zamovlennya_list : список замовлень
    """

    from_file = [
 "КНТЕУ;202;10;10",
 "КНЕУ;203;20;10",
 "КНУ;205;30;5",
 "КНТЕУ;207;40;10",
 "КНЕУ;211;20;5",
 "КНУ;204;10;5",
 "КНТЕУ;206;30;5",
 "КНЕУ;210;50;3",
 "КНУ;212;60;4",
 "КНТЕУ;213;70;5",
    ]

    # накопичувач рядків
    zamovlennya_list = []

    for line in from_file:
        line_list = line.split(';')
        zamovlennya_list.append(line_list)

    return zamovlennya_list

def show_zamovlennya(zamovlennya):
    """виводить список замовлень за заданої умови

    Args:
        zamovlennya :  список замовлень
    """
    zamovlennya_code_from = input("з якого кода замовлення?")
    zamovlennya_code_to = input("по який код замовлення?")
    for zamovlennya in zamovlennya:
        if zamovlennya_code_from <= zamovlennya[2] <= zamovlennya_code_to:
             print("Клієнт = {:7} Номер заказу = {:5} Kод : {:5} Kількість = {:10} " .format(zamovlennya[0], zamovlennya[1], zamovlennya[2], zamovlennya[3]))


zamovlennya = get_zamovlennya()
show_zamovlennya(zamovlennya)

""" модуль для доступу до вхідних даних
"""

def get_dovidnk():
    """отримує данні по замовленням

    Returns:
        dovidnk_list : список замовлень
    """

    from_file = [
  "10;План розрахунків підприємств;40",
  "20;ППП УЗПИКС;900",
  "30;ППП УТЕП;900",
  "40;ППП УОС;600",
  "50;ППП УФРО;1245",
  "60;АРМ бухгалтера матеріально-технічного відділу;500",
  "70;АРМ бухгалтера фінансового відділу;500",
  "80;ППП Облік договорів;150",
    ]

    # накопичувач рядків
    dovidnk_list = []

    for line in from_file:
        line_list = line.split(';')
        dovidnk_list.append(line_list)

    return dovidnk_list

def show_dovidnk(dovidnk):
    """виводить список замовлень за заданої умови

    Args:
        dovidnk :  список замовлень
    """
    dovidnk_code_from = input("з якого кода замовлення?")
    dovidnk_code_to = input("по який код замовлення?")
    for dovidnk in dovidnk:
        if dovidnk_code_from <= dovidnk[0] <= dovidnk_code_to:
             print(" Код: {:5} Найменування товару = {:48} Ціна = {:10}  ".format(dovidnk[0], dovidnk[1], dovidnk[2]))

dovidnk = get_dovidnk()
show_dovidnk(dovidnk)