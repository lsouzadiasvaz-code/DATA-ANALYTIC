
class Data:
    def __init__(self) -> None: #pega o dataframe limpo e chama a classe Alt2 de alter
        from dataframe import DF
        from alter import Alt2
        app = DF()
        self.df = app.all_df()
        self.data = Alt2()
        
        
    def group(self) -> None: #agrupa por data
        
        self.analytic = self.data.group({"values":["created_at"]})
    
    def outlier(self) -> None: #detecta os outlierspelo fautramento
        self.analytic = self.data.outlier(self.analytic, "faturamento")
        
        
    def product(self) -> None: #retorna o produto que mais vendeu em cada mes
        self.analytic = self.data.max({"value": "mes", "column": "name_product","op": "total", "name": "max_product"}, self.analytic)
          
    def analytic_Data(self): #chama todos os metodos e retornar um dataframe que ve o faturamento por mes e produtos que mais venderam
        self.group()
        self.outlier()
        self.product()
        return self.analytic
    
    

    
   

        