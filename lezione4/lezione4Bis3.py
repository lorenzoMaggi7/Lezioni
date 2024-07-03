def convert_to_title(col_number: int) -> str:
    """
    Dato un intero col_number,
    restituire il suo corrispondete titolo di colonna come ad esempio compare sul foglio excel

    Esempio1 :
    col_number = 1 -> restituire "A"
    col_number = 2 -> restituire "B"
    col_number = 26 -> restituire "Z"

    Esempio2:
    col_number = 27 -> restituire "AA"
    col_number = 28 -> restituire "AB"

    Esempio3:
    col_nuber = 701 -> restituire "ZY"
    """
    result: str = ""
    while col_number > 0:
        resto: int = (col_number - 1) % 26 #questo mi da il resto
        result = chr(resto + ord('A')) + result
        col_number = (col_number - 1) // 26
    return result
print(convert_to_title(55))


# col_number = 700
# result = ""
#//// iterazione numero 1 //////
# resto = 23
# result = x
# col_number = 26
#///// seconda iterazione ///////
# resto = 25
# result = zx
# col_number = 0