reader = (open("file/esempio.txt", encoding="utf-8"))

with open("file/esempio.txt", encoding="utf-8") as reader:

    print(reader)


try: 
    reader.readline()
    print("sono nella try")
    raise Exception("eccezione")

except Exception:

    print("sono nella exception")

finally:

    print("sono nella finally")
    reader.close()

class ContexManager:
    def __enter__(self):

        print("ciao sono nell'enter")

        return self
    
    def __exit__(self,exc_type, exc_value, traceback):

        if exc_type is not None:
            print("ECCEZIONE")

        return False
    
with ContexManager() as cm:

    print("ciao")
    print(cm)
