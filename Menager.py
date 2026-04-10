import pandas as pd
#aqui serve pra chamar todas as outras classes dos outors arquivos
class AnalyticManager:
        
             
        def Data(self) -> pd.DataFrame: #pega o dataframe de data
            from analyticData import Data
            dt = Data()
          
            return dt.analytic_Data()
            
                
            
            
        
        def Product(self) -> pd.DataFrame: #pega o dataframe de produtos
            from analyticProduct import Product
            Pd = Product()
           
            return Pd.analytic_Products()
                
            
        
        def Clientes(self) -> pd.DataFrame: #pega o dataframe de clientes
            from analyticClientes import Clientes
            Cl = Clientes()
           
            return Cl.analytic_Clientes()
                
            
        
        def Dataframe(self) -> pd.DataFrame: #pega o dataframe geral
            from dataframe import DF
            Con = DF() 
            df =  Con.all_df()
            
                
            return df
        
        
                

        
        
        
