import pandas as pd
class Alt2:
    def __init__(self)->None:  #esse metodo chama o arquivo onde retorna o dataframe
        from dataframe import DF
        app = DF()
        self.df = app.all_df()
        
    def group(self,value:dict) -> pd.DataFrame: #aqui o metodo serve pra agrupar valores de coluna que foi passado nos parametros, que espera um dict assim: {"values": coluna(s) que vc vai agrupar, "name":caso vc queira alterar o nome das colunas}
        if not "values" in list(value.keys()):
            raise Exception("key erro")
        if "created_at" in value["values"]:
            self.df["mes"] = self.df["created_at"].dt.to_period("M")
            value["values"][list(value["values"]).index("created_at")] = "mes"       
        
        if len(value["values"]) == 1:
         val = value["values"][0]
        else:
            val = value["values"]
                    
        df = self.df.groupby(val, as_index=False).agg(
                quantidade=("quantity", "sum"),
                faturamento=("total", "sum")
            )
        
        if len(value.keys()) == 2:
            if (len(value["name"]) > 2) or (len(value["name"]) < 2) or (not "name" in value.keys()):
                raise Exception("error name")
            
            
            name_1 = value["name"][0]
            name_2 = value["name"][1]
            df = df.rename(columns={
                "quantidade": name_1, 
                "faturamento": name_2
            }
                
            )
            
        elif len(value.keys()) > 2:
            raise Exception("Key error")
        
             
        return df 
    
    def outlier(self, df:pd.DataFrame, column:str) -> pd.DataFrame:#esse metodo serve pra detectar outlier de uma coluna especifa
        import numpy as np                                         # df = dataframe, column = coluna pra indentificar outlier
        q1 = np.percentile(df[column], 25)
        q3 = np.percentile(df[column], 75)
        iqr = q3 - q1
        limit_inf = q1 - (iqr * 1.5)
        limit_sup =  q3 + (iqr * 1.5)
        con = [
            df[column] > limit_sup,
            df[column] < limit_inf
        ]
        values = ["high", "lower"]
        df["outlier"] = np.select(con, values, default="mean")
        return df
    
    def max(self, value:dict, df:pd.DataFrame) -> pd.DataFrame: #esse metodo serve pra vc pegar o valor maximo do valor da caluna que voce quer e criar uma nova coluna.
                                                                # df=dataframe
                                                                #  value= {"value": colunas que voce quer pegar o valor, "column":coluna que voce quer que junte no df original, "op":coluna que voce quer fazer a operação, "name":caso voce queira mudar o nome da nova coluna}
        if (not "value" in list(value.keys())) or (not "column" in list(value.keys())) or  (not "op" in list(value.keys())) or (len(value.keys())<3) or (len(value.keys())>4) or ( not value["value"] in list(df.columns)):
                raise ValueError(f"{value} invalid")
            
    
        df_value = self.df.groupby([value["value"], value["column"]], as_index=False)[value["op"]].sum()
        idx = df_value.groupby(value["value"])[value["op"]].idxmax()
        df_max = df_value.loc[idx, [value["value"], value["column"]]]
        
        df = df.merge(
            df_max,
            on=value["value"],
            how="left"
        )
        
        if "name" in value.keys():
            df = df.rename(columns={
               value["column"]: value["name"]
            })
            
        return df
        
        
        
        
        
        