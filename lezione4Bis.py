def is_palindrome(x:int) -> bool:
 """
 Dato un intero x, restituisci True se x è palindromo, e False altrimenti

 Esempio 1:
 x = 121 -> True
 Spiegazione : 121 si legge come 121 sia da destra che da sinistra

 Esempio 2 : 
 x = -121 -> False
 SPiegazione : da sinistra a destra. eggiamo -121. Da destra a snistra, abbiamo 121-. Perciò, questo numero non è palindromo

 Esempio 3: 
 x = 10 -> False
 Spiegazione: 01 da destra a sinistra. Perciò, non è palindromo
 """
 x = str(x)
 if x == ''.join(reversed(x)) :
    print(True)
 else :
    print(False)
is_palindrome(777)

"""
////ALTRI ESEMPI PER RISOLVERE//////
s:str= str(x)
s1:str = ""
for i in range(len(s),0,-1):
   s1 = s1 + s[i]
return s == s1
///////////////////////
a m o r o m a
0 1 2 3 4 5 6
|           |
 i |       | j
    |   |
      |

i = o -> j = len(s) -1
i = 1 -> j = len(s) -2
i = 2 -> j = len(s) -3
i = 3 -> j = len(s) -4
i = 4 -> j = len(s) -5
i = 5 -> j = len(s) -6

i = n -> j = len(s) - (n+1)

/////////////////////////

s : str = str(x)
i : int = 0
while i < len(s): 
   j = len(s) - (i+1)
   if s[i] == s[j]:
      continue
   else:
      return False
      
//////OPPURE////////
while i < len(s): 
   j = len(s) - (i+1)
   if s[i] != s[j]:
      return False
   i += 1
return True


/////////O ANCHE//////
s: str = str(x)
i  int = 0
s_lenght = len(s)
while i < (s_lenght // 2):
   j = s_lenght - (i+1)
   if s[i] != s[j]:
      return False
   i += 1
return True

"""




 