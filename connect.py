import pandas as pd
class Connect:
    
        
    def __init__(self) -> None:#esse metodo conecta com o banco de dados(supabase)
        import os
        from dotenv import load_dotenv
        import psycopg
        load_dotenv()  

        self.con = psycopg.connect(
            host=os.getenv("DB_HOST"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )

        self.cur = self.con.cursor()
        
    def dataframe(self) -> None: #esse metodo converte o banco em dataframe
        
        self.df = pd.read_sql("""
                              select C.id_client, C.name, C.state, P.name_product, P.price, O.quantity, (P.price * O.quantity) as total, O.created_at from orders O
inner join clientes C   
on O.id_client = C.id_client
inner join products P
on P.name_product = O.product
                              """, self.con)
        
    
        
        
    def data(self) -> pd.DataFrame:#esse retorna o dataframe
        self.dataframe()
        return self.df
    

        
    
    
    
    
    