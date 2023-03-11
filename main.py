"""
COnversor de Moedas (Real, para Dólar e Euro)
    Autor: Júlia Onora da Silva
    Data: 8 de fevereiro de 2022
"""

from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("appFront.kv")


class ConversorMoedasApp(App):
    def build(self):
        return GUI

    def on_start(self):
        self.root.ids["moeda1"].text = f"Dólar à R${self.pegar_cotacao('USD')}"
        self.root.ids["moeda2"].text = f"Euro à R${self.pegar_cotacao('EUR')}"

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao


ConversorMoedasApp().run()
