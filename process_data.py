""" формування заявок на устаткування по магазину
"""
from data_service import get_dovidnk, get_zamovlennya


# структура рядка вихідних даних
zayavka = {

    'namet_name'    : '',  # найменування
    'order_number'  : '',  # номер заказа
    'kodk_name'     : '',  # код клієнта
    'kol'           : 0,   # кількість 
    'cena'          : 0.0, # ціна
    'summa'         : 0.0, # сума
}


dovidnk = get_dovidnk()
zamovlennya = get_zamovlennya()


def table_zayavka():  
    """Формування аналізу руху основних засобів
    """
    
    def get_dovidnk_name(dovidnk_code):
        """повертає назву клієнта по його коду

        Args:
            dovidnk_code ([type]): код клієнта

        Returns:
            [type]: назва клієнта
        """
        for dovidnk in dovidnk:
            if dovidnk_code == dovidnk[0]:
                return dovidnk[1]
        return "*** назва не знайдена"
    
    # накопичувач заявок
    zayavka_list = []

    for zamovlennya in zamovlennya:   
        
        # створити робочу копію
        zayavka_work = zayavka.copy()
        
        zayavka_work['namet_name']      = zamovlennya[2]
        zayavka_work['order_number']    = zamovlennya[1]
        zayavka_work['kodk_name']       = zamovlennya[3]
        zayavka_work['kol']             = zamovlennya[4]
        zayavka_work['cena']            = zamovlennya[3]

        zayavka_work['summa']           = zayavka_work['kol'] *  zayavka_work['cena']
    
        zayavka_work['dovidnk_name']  = get_dovidnk_name(zamovlennya[0])

        
        zayavka_list.append(zayavka_work)
        
    return zayavka_list




    


            
     
        

