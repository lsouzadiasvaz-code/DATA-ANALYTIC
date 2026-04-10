import os
import pandas as pd

     
    
#esse arquivo e um modulo pra converter os dataframes em excel, atualizar, ou ler.


class Archive:
    def __init__(self) -> None:
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.analytic_dir = os.path.join(self.base_dir, "ANALYTIC")
        os.makedirs(self.analytic_dir, exist_ok=True)

    def _file_path(self, name: str) -> str:
        return os.path.join(self.analytic_dir, f"{name}.xlsx")

    def create_excel(self, values: dict) -> None:
        file_path = self._file_path(values["path"])

        if not os.path.exists(file_path):
            

            values["df"].to_excel(file_path, index=False)

    def update_excel(self, values: dict) -> None:
        file_path = self._file_path(values["path"])

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{values['path']}.xlsx not found")

        values["df"].to_excel(file_path, index=False)

    def read_excel(self, values: str):
        if values == "all":
            dfs = {}

            for file_name in os.listdir(self.analytic_dir):
                if file_name.endswith(".xlsx"):
                    name = file_name.replace(".xlsx", "")
                    file_path = os.path.join(self.analytic_dir, file_name)
                    dfs[name] = pd.read_excel(file_path)

            return dfs

        file_path = self._file_path(values)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{values}.xlsx not found")

        return pd.read_excel(file_path)
                
            

            
            
        
    

        
        
            
        
        
            
            
        