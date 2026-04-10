class Clientes:
    def __init__(self) -> None:
        from connect import Connect
        from alter import Alt2
        app = Connect()
        self.df = app.all_df()
        self.data = Alt2()
        
    def analytic_Clientes(self) ->None: #agrupa por clientes e retorna o df
        self.analytic = self.data.group({"values":["id_client", "name"], "name": ["comprado", "gasto"]} )
        self.analytic = self.analytic.sort_values(by="gasto", ascending=False)
        return self.analytic
    
    

