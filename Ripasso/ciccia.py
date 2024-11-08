# # Aprire il file binario e leggere il contenuto
# with open('snake.jpg', 'rb') as file_binario:
#     contenuto_binario = file_binario.read()

# # Aprire un file di testo e scrivere i byte come stringhe di numeri
# with open('snake.txt', 'w') as file_testo:
#     for byte in contenuto_binario:
#         file_testo.write(str(byte) + '\n')
# ############################
# LeggiBinario("pitone.jpeg", "pitone.txt")
# ScriviBinario("pitone.txt", "pitone1.jpeg")
 
# E, in modo più coompatto...

def LeggiBinarioHex(pin, pout):
    with open(pin, mode="rb") as fin:
        with open(pout, mode="w") as fou:
            dati = fin.read()
            for v in dati:
                s = hex(v)[2:]
                if len(s) < 2:
                    s = "0" + s
                    fou.write(s)


def ScriviBinarioHex(tin, tou):
    with open(tin, mode="r") as fin:
        with open(tou, mode="wb") as fou:
            nums = fin.read()
            for i in range(0, len(nums) // 2):
                v = int(nums[2 * i] + nums[2 * i + 1], 16)
                a = v.to_bytes()
                fou.write(a)


# esempio
LeggiBinarioHex("snake.jpg", "snake.txt")
ScriviBinarioHex("snake.txt", "snake.jpg")
