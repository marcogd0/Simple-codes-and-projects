import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USD']['bid']
    cotacao_euro = requisicao_dic['EUR']['bid']
    cotacao_btc = requisicao_dic['BTC']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''
    
    texto_cotacoes['text'] = texto

janela = Tk()
janela.title("Cotaçoes")

esquerda = Label(janela, text='')
direita = Label(janela, text='')
esquerda.grid(column=0, row=0)
direita.grid(column=2, row=0)
texto_introdutorio = Label(janela, text='Clique no botão para ver as cotaçoes')
texto_introdutorio.grid(column=1, row=0, padx=10, pady=10)

botao = Button(janela, text='Clique aqui para ver as cotaçoes', command=pegar_cotacoes)
botao.grid(column=1, row=1)

texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=1, row=2)

janela.mainloop()