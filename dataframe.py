import pandas as pd
class DF:
    def __init__(self):  #esse metodo chama o arquivo onde faz a conexão com banco(supabase)
        from connect import Connect     
        Con = Connect()       
        self.Df = Con.data()
        
    def clean(self) -> None:  #esse metodo limpa as linhas vazias e remove as colunas que mais de 30% estejam vazias
        
        for c in self.Df.columns:
            if (self.Df[c].isna().mean() * 100) > 30: 
                self.Df = self.Df.drop(columns=[c])
                
        self.Df = self.Df.dropna()
        
        
    def all_df(self) -> pd.DataFrame: #esse metodo retorna o dataframe ja limpo.
        
        self.clean()
        return self.Df
    