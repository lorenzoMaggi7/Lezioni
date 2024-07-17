
# # Codificatori Messaggio
# Si crei una classe astratta chiamata CodificatoreMessaggio che ha un solo metodo astratto codifica(testoInChiaro), dove testoInChiaro sarà il messaggio da codificare. Il metodo restituirà il messaggio codificato.

# Si crei una classe astratta chiamata DecodificatoreMessaggio che abbia un solo metodo decodifica(testoCodificato), dove testoCodificato sarà il messaggio da decodificare. Il metodo ritornerà il messaggio decodificato.

# Si crei una classe CifratoreAScorrimento che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio. Il costruttore dovrebbe ricevere un numero intero chiamato chiave. Si definisca il metodo codifica(testoInChiaro) così che ogni lettera del testo sia spostata dal valore contenuto in chiave.
# Per esempio, se chiave è uguale a 3, la lettera 'a' sarà sostituita da 'd', la lettera 'b' sarà sostituita da 'e', la lettera 'c' sarà sostituita da 'f' e così via.

#      Suggerimento: si potrebbe definire un metodo privato sposta_carattere(c) che restituisca la codifica di un singolo carattere c da concatenare agli altri per costruire il messaggio codificato nel metodo codifica(testoInChiaro).


# Si crei una classe CifratoreACombinazione che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio. Il costruttore dovrebbe ricevere un numero intero chiamato n. Si definisca il metodo codifica(testoInChiaro) così che il messaggio sia combinato n volte. Per eseguire una singola combinazione, si divide il messaggio a metà e poi si prendono i caratteri da ognuna delle metà in modo alternato. Per esempio, se il messaggio è 'abcdefghi', le metà sono 'abcde' e 'fghi' (nel caso in cui la lunghezza del testo da decifrare sia un numero dispari, la prima metà deve essere più lunga della seconda metà). Il messaggio combinato è 'afbgchdie'.

#     Suggerimento: si potrebbe definire un metodo privato combinazione(testo) che esegue la combinazione del testo e ritorni il testo cifrato da usare nel metodo codifica(testoInChiaro).


# Si scriva il metodo decodifica(testoCodificato) per ognuna delle classi CifrarioAScorrimento e CifrarioACombinazione.

#     Suggerimento: definire il metodo privato decodifica_carattere() per la classe CifrarioAScorrimento che compie un'azione inversa al metodo sposta_carattere().

#     Suggerimento: definire il metodo privato decodifica_combinazione() per la classe CifrarioACombinazione che compie un'azione inversa al metodo combinazione().


# Infine, si implementi anche un metodo per leggere il testo da cifrare da un file e un metodo per scrivere il testo cifrato su un file per entrambe le classi CifratoreAScorrimento e CifratoreACombinazione.

# ### Test tramite codice driver:
# Test del Cifratore a Scorrimento:
# - Inizializzazione: Viene creato un oggetto CifratoreAScorrimento con una chiave di scorrimento di 3.
# - Lettura del testo: Il testo in chiaro viene letto da un file.
# - Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a scorrimento.
# - Scrittura del testo codificato: Il testo codificato viene scritto su un file.
# - Stampa del testo codificato: Il testo codificato viene stampato.
# - Decodifica: Il testo codificato viene decodificato.
# - Stampa del testo decodificato: Il testo decodificato viene stampato.

# Test del Cifratore a Combinazione:
# - Inizializzazione: Viene creato un oggetto CifratoreACombinazione con 3 combinazioni.
# - Lettura del testo: Il testo in chiaro viene letto da un file.
# - Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a combinazione.
# - Scrittura del testo codificato: Il testo codificato viene scritto su un file.
# - Stampa del testo codificato: Il testo codificato viene stampato.
# - Decodifica: Il testo codificato viene decodificato.
# - Stampa del testo decodifica

from abc import ABC, abstractmethod

# Classi astratte
class CodificatoreMessaggio(ABC):
    @abstractmethod
    def codifica(self, testoInChiaro: str) -> str:
        pass

class DecodificatoreMessaggio(ABC):
    @abstractmethod
    def decodifica(self, testoCodificato: str) -> str:
        pass

# Classe CifratoreAScorrimento
class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, chiave: int):
        self.chiave = chiave

    def codifica(self, testoInChiaro: str) -> str:
        return ''.join(self.sposta_carattere(c) for c in testoInChiaro)

    def sposta_carattere(self, c: str) -> str:
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            return chr((ord(c) - base + self.chiave) % 26 + base)
        return c

    def decodifica(self, testoCodificato: str) -> str:
        return ''.join(self.decodifica_carattere(c) for c in testoCodificato)

    def decodifica_carattere(self, c: str) -> str:
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            return chr((ord(c) - base - self.chiave) % 26 + base)
        return c

    def leggi_da_file(self, nome_file: str) -> str:
        with open(nome_file, 'r') as file:
            return file.read()

    def scrivi_su_file(self, nome_file: str, testo: str):
        with open(nome_file, 'w') as file:
            file.write(testo)

# Classe CifratoreACombinazione
class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, n: int):
        self.n = n

    def codifica(self, testoInChiaro: str) -> str:
        combined = testoInChiaro
        for _ in range(self.n):
            combined = self.combinazione(combined)
        return combined

    def combinazione(self, testo: str) -> str:
        half_len = (len(testo) + 1) // 2
        first_half = testo[:half_len]
        second_half = testo[half_len:]
        combined = ''.join(a + b for a, b in zip(first_half, second_half))
        if len(first_half) > len(second_half):
            combined += first_half[-1]
        return combined

    def decodifica(self, testoCodificato: str) -> str:
        combined = testoCodificato
        for _ in range(self.n):
            combined = self.decodifica_combinazione(combined)
        return combined

    def decodifica_combinazione(self, testo: str) -> str:
        half_len = (len(testo) + 1) // 2
        first_half = testo[:half_len]
        second_half = testo[half_len:]
        decoded = []
        for i in range(len(second_half)):
            decoded.append(first_half[i])
            decoded.append(second_half[i])
        if len(first_half) > len(second_half):
            decoded.append(first_half[-1])
        return ''.join(decoded)

    def leggi_da_file(self, nome_file: str) -> str:
        with open(nome_file, 'r') as file:
            return file.read()

    def scrivi_su_file(self, nome_file: str, testo: str):
        with open(nome_file, 'w') as file:
            file.write(testo)

# Codice di test
def test_cifratore_scorrimento():
    cifratore = CifratoreAScorrimento(3)
    testo_in_chiaro = "hello world"
    cifratore.scrivi_su_file('testo_in_chiaro.txt', testo_in_chiaro)

    testo_letto = cifratore.leggi_da_file('testo_in_chiaro.txt')
    testo_codificato = cifratore.codifica(testo_letto)
    cifratore.scrivi_su_file('testo_codificato.txt', testo_codificato)

    print(f"Testo codificato: {testo_codificato}")

    testo_decodificato = cifratore.decodifica(testo_codificato)
    print(f"Testo decodificato: {testo_decodificato}")

def test_cifratore_combinazione():
    cifratore = CifratoreACombinazione(3)
    testo_in_chiaro = "abcdefghi"
    cifratore.scrivi_su_file('testo_in_chiaro.txt', testo_in_chiaro)

    testo_letto = cifratore.leggi_da_file('testo_in_chiaro.txt')
    testo_codificato = cifratore.codifica(testo_letto)
    cifratore.scrivi_su_file('testo_codificato.txt', testo_codificato)

    print(f"Testo combinato: {testo_codificato}")

    testo_decodificato = cifratore.decodifica(testo_codificato)
    print(f"Testo decodificato: {testo_decodificato}")

# Eseguiamo i test
test_cifratore_scorrimento()
test_cifratore_combinazione()
