def lenght_of_last_word(s: str) -> int:
 """
 Data una stringa s che contiene parole e spazi, 
 restituire la lunghezza dell'ultima parola

 Esempio1:
 s= "Hello World" -> resituire 5
 Spiegazione: L'utima parola è "WORLD" che ha lunghezza 5

 """
 l = s.split()[-1]
 return(len(l))
print(lenght_of_last_word("Forza             Roma      "))

"""
//////////Oppure///////
s: str = ''.join(reversed(s))
i: int = 0
curr_len: int = 0
while i < len(s):
    if s[i] != " ":
        curr_len +=1
    else:
        break
    i += 1
return curr_len

"""