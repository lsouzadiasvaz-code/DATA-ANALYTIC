from fastapi import FastAPI
from Menager import AnalyticManager
Data = AnalyticManager()
app = FastAPI()
#aqui são as rotas da minha api para conectar com bi
@app.get("/vendas") #rota do df geral
def vendas():
    Df =  Data.Dataframe()
    return Df.to_dict(orient="records")

@app.get("/products") #rota do df de produtos
def produtos():
    Df =  Data.Product()
    return Df.to_dict(orient="records")

@app.get("/Data") #rota do df de datas
def data():
    Df =  Data.Data()
    return Df.to_dict(orient="records")

@app.get("/clientes") #rota do df de clientes
def client():
    Df =  Data.Clientes()
    return Df.to_dict(orient="records")




