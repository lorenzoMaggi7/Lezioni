import os

def CercaStringaInNomeFile(sFiles,sStringa):
    #mettiamo tutto a minuscolo
    sfileLC = sFiles.lower()
    sStringaLC = sStringa.lower()


    #usiamo sFileLower.find() che torna -1 se la parola non c'è e la posizione della parola altrimenti.
    if(sfileLC.find(sStringaLC)>=0):
        return True
    else:
        return False

    #torniamo true oppure false



def CercaStringaIncontenutoFile(sPathfile,sStringa):
    return False


sRoot = input("inserisci directory in cui cercare")
sParola = input ("inserisci la parola da cercare")
sOutDir = input ("inserisci la diractory di output")

iNumFileTrovati = 0
for root, dirs, files in os.walk(sRoot):
    print(f"sto guardando {root} che contiene {len(dirs)} subdir e {len(files)} files")
    for file in files :
        print(f"devo vedere se {file} contiene {sParola}")
        bRet = CercaStringaInNomeFile(file,sParola)
        if bRet == True:
            iNumFileTrovati += 1
        else:
            sFilePathCompleto = os.path.join(root,file)
            bRet = CercaStringaIncontenutoFile()
            if (bRet=True):
                iNumFileTrovati += 1

print(f"ho trovato {iNumFileTrovati} files")