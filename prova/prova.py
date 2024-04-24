"""
Sei un detective esperto nel mondo dei testi e un caso sconcertante è arrivato sulla tua scrivania. Due stringhe, s e t, sono i tuoi sospettati. 
La tua missione: determinare se s si nasconde in bella vista all'interno di t, ma con una svolta!

Qual è il problema?

Non puoi semplicemente confrontare le stringhe lettera per lettera. Immagina che s sia un personaggio subdolo che cerca di confondersi tra la folla (t). 
Potrebbero camuffarsi nascondendosi tra altri personaggi, ma non cambiano mai il loro ordine! 
Quindi, "ace" può intrufolarsi in "abcde" (rimuove semplicemente "b" e "d"), ma "aec" non funzionerebbe (l'ordine cambia).

Scrivi una funzione di interruzione del codice che prenda la stringa s (il carattere subdolo) e t (la folla) come input. 
Se è possibile trovare s in agguato all'interno di t mantenendo il suo travestimento (ordine), restituisce True. 
Altrimenti restituisce False. Dimostra le tue abilità da detective e svela la verità nascosta!


#def is_subsequence(s: str, t: str) -> bool:
    # elimina pass e inserisci il tuo codice
    
s:str = "ari"
t:str = "aercokij"
x = list(s)
y = list(t)

sospetto: list = [i in y for i in x]
print(sospetto)

"""

def is_disguised(s, t):
    i = 0
    for l in t:
        if i < len(s) and l == s[i]:
            i += 1
    return i == len(s)
is_disguised(s = "abert", t = "alberto")


"""
Hai il compito di indagare su un caso di numeri mancanti! 
Ti viene fornito un elenco di numeri univoci (nums) da 1 a n, dove n è la lunghezza dell'elenco. Sembra però che ci sia un problema: mancano alcuni numeri!

La tua missione è scrivere una funzione che prenda come input questo elenco di numeri (nums) potenzialmente incompleti.
Questo elenco rappresenta i numeri esistenti, ma alcuni numeri tra 1 e n potrebbero mancare.

La funzione restituisce una nuova lista contenente tutti i numeri mancanti da 1 a n che non sono presenti nella lista originale.


print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))

[5, 6]

def find_disappeared_number(nums:list[int]) -> list[int]:
    # Calcola la lunghezza dell'elenco dei numeri
    n:int = len(nums)
    
    # Crea un set dei numeri presenti nell'elenco nums
    present_numbers = set(nums)
    
    # Inizializza una lista per contenere i numeri mancanti
    find_disappeared_number:list = []
    
    # Itera attraverso tutti i numeri da 1 a n
    for numero in range(1, n+1):
        # Se il numero non è presente nell'elenco, lo aggiunge alla lista dei numeri mancanti
        if numero not in present_numbers:
            find_disappeared_number.append(numero)
    
    # Restituisce la lista dei numeri mancanti
    return find_disappeared_number

# Esempio di utilizzo della funzione
nums = [1, 2, 4, 6, 7]
print(find_disappeared_number(nums))  # Output: [3, 5]
"""

#Scrivi una funzione prime_factors(n: int) -> list[int] che trova i fattori primi di un numero n dato in input
"""
def prime_factors(n: int) -> list[int]:
    factors = []
    divisor = 2
    
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1
        
    return factors

# Esempio di utilizzo:
number = 84
print("Fattori primi di", number, ":", prime_factors(number))

"""
def prime_factors(n: int) -> list[int]:
    factors = []  # Inizializziamo una lista vuota per memorizzare i fattori primi
    divisor = 2   # Inizializziamo il divisore a 2, il primo numero primo
    
    # Avviamo un ciclo while che continua finché il numero n è maggiore di 1
    while n > 1:
        # Verifichiamo se il numero è divisibile per il divisore corrente
        if n % divisor == 0:
            # Se il numero è divisibile, aggiungiamo il divisore alla lista dei fattori primi
            factors.append(divisor)
            # Dividiamo il numero per il divisore e assegnamo il risultato a n
            n //= divisor
        else:
            # Se il numero non è divisibile per il divisore corrente, incrementiamo il divisore
            divisor += 1
    
    # Una volta che n è diventato 1, tutti i fattori primi sono stati trovati, restituiamo la lista dei fattori primi
    return factors




"""
    Data una lista di numeri interi, riordina i numeri in modo che tutti i numeri pari appaiano prima di tutti i numeri dispari. Restituisce l'elenco riorganizzato.
"""
def even_odd_pattern(nums: list[int]) -> list[int]:
    even:list = []
    odd:list = []
    for numbers in nums:
        if numbers % 2 == 0:
            even.append(numbers)
        else:
            odd.append(numbers)
    return even + odd
nums=[3,5,6,4,1,2]
print(even_odd_pattern(nums))







    






"""
Uno sviluppatore web deve sapere come progettare le dimensioni di una pagina web. Pertanto, data l'area specifica di una pagina Web rettangolare, 
il tuo compito ora è progettare una pagina Web rettangolare, la cui lunghezza L e larghezza W soddisfino i seguenti requisiti:

1. L'area della pagina web rettangolare che hai progettato deve essere uguale all'area di destinazione specificata.
2. La larghezza W non deve essere maggiore della lunghezza L, il che significa L >= W.
3. La differenza tra la lunghezza L e la larghezza W dovrebbe essere la minima possibile.

Restituisce una lista [L, W] dove L e W sono la lunghezza e la larghezza della pagina web che hai progettato in sequenza.

Esempio:

construct_rectangle(4)

L'area target è 4 e tutti i modi possibili per costruirla sono [1,4], [2,2], [4,1].
Ma secondo il requisito 2, [1,4] è illegale; secondo il requisito 3, [4,1] non è ottimale rispetto a [2,2]. Quindi la lunghezza L è 2 e la larghezza W è 2.

def construct_rectangle(area: float) -> list[float]:
    w:float = 4
    l:float = 2
    for area in range(len(area)):
        if l >= w:
            x = list[l,w]
            return x
        elif l < w:
            False
    return area[float]
"""
"""
import math

def design_web_page(area):
    l = math.sqrt(area)
    w = l

    if w > l:
        w = l
    optimal_length = math.ceil(l)
    optimal_width = math.floor(area / optimal_length)

    return [optimal_length, optimal_width]

area_specificata = 798
lunghezza, larghezza = design_web_page(area_specificata)
x:list=[lunghezza,larghezza]
print("Area: ", x)

def construct_rectangle(area):
    # Inizializziamo la lunghezza L e la larghezza W con i valori massimi
    L = area
    W = 1
    
    # Iteriamo da W fino a radice quadrata di area
    for i in range(2, int(area**0.5) + 1):
        # Se i è un divisore di area
        if area % i == 0:
            # Verifichiamo se la differenza tra i e area/i è minima rispetto alla differenza attuale tra L e W
            if abs(i - area//i) < abs(L - W):
                # Aggiorniamo L e W
                L = max(i, area//i)
                W = min(i, area//i)
    
    return [L, W]

# Esempio di utilizzo
print(construct_rectangle(37))  # Output: [2, 2]
"""
"""
def construct_rectangle(area):
    for i in range(int(area**0.5), 0, -1):
        if area % i == 0:
            return [max(i, area // i), min(i, area // i)]


print(construct_rectangle(37))  # Output: [2, 2]
"""
"""
import math

def construct_rectangle(area: float) -> list[float]:
    l:float = math.sqrt(area)
    w:float = 1
    i:float = 1
    if w > l:
        w = l
    elif area % i == 0:
        return [max(i, area // i), min(i, area // i)]
    optimal_l = math.ceil(l)
    optimal_w = math.floor(area / optimal_l)

    return [optimal_l, optimal_w]
"""
import random
import math

def divisors(n):
    result = []
    for i in range(1, n//2 + 1):
        if n % i == 0:
            result.append(i)
    result.append(n)
    return result

def construct_rectangle(area:float) -> list[float]:
    
    min_dist = area - 1
    props = []
    dividers = divisors(area)
    for i in dividers:
        for j in dividers:
            if area == (i*j):
                dist = abs(i - j)
                if dist <= min_dist:
                    min_dist = dist
                    props = [i,j]

    return props


print(construct_rectangle(4))
print(construct_rectangle(37))
print(construct_rectangle(49))
print(construct_rectangle(122122))
