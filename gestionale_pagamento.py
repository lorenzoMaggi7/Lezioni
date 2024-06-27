class Pagamento:
    def __init__(self) -> None:
        self.__importo: float = None

    def get_importo(self):
        return self.__importo
    
    def set_importo(self, importo: float):
        if isinstance(importo, float) and importo >= 0:
            self.__importo = importo
        else:
            raise ValueError("L'importo deve essere un numero float positivo.")
        
    def dettagliPagamento(self):
        return f"Importo pagamento: €{self.__importo:.2f}"
    
pagamento = Pagamento()
pagamento.set_importo(40.00)
print(pagamento.dettagliPagamento())

class PagamentoContanti(Pagamento):
    def __init__(self) -> None:
        super().__init__()
    
    