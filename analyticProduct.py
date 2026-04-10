import pandas as pd
class Product:
    def __init__(self) -> None: #pega o dataframe limpo e chama a classe Alt2 de alter
        from dataframe import DF
        from alter import Alt2
        app = DF()
        self.df = app.all_df()
        self.data = Alt2()
        
    
    def group(self) -> None: #agrupa por produtos
        
        self.analytic = self.data.group({"values": ["name_product"], "name": ["vendas", "Faturamento"]})
        self.analytic = self.analytic.sort_values(by="Faturamento", ascending=False)
        
    def outlier(self) ->None: #detecta produtos outliers
        self.analytic = self.data.outlier(self.analytic, "Faturamento")
        
    def state(self) -> None: #retorna o estado que mais comprou cada produto
        self.analytic = self.data.max({"value": "name_product", "column": "state","op": "quantity", "name": "max_state"}, self.analytic)
    
        
    def analytic_Products(self) -> pd.DataFrame: #chama os metodos e retorna um dataframe que agrupa por produtos
        self.group()
        self.state()
        self.outlier()
        
        return self.analytic
    
   
    


        