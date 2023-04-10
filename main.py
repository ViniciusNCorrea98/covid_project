from tkinter import *
from tkinter import ttk
##https://api.covidtracking.com/v1/us/daily.json##

from PIL import Image
import requests

import string
import json
import datetime

co0 = "#000000"
co1 = "#cc1d4e"
co2 = "#feffff"
co3 = "#0074eb"
co4 = "#435e5a"
co5 = "#59b356"
co6 = "#d9d9d9"

janela = Tk()

janela.resizable(width=False, height=False)
janela.geometry('835x360')
janela.title('')
janela.configure(bg=co6)

app_nome_frame = Frame(janela, width= 840, height=50, bg=co2, relief="flat")
app_nome_frame.grid(row=0, column=0, columnspan=3,sticky=NSEW)


frame_dados_infectados = Frame(janela, width= 220, height=100, bg=co2, relief="flat")
frame_dados_infectados.grid(row=1, column=0, sticky=NW, pady=5, padx=5)

frame_dados_recuperados = Frame(janela, width= 220, height=100, bg=co2, relief="flat")
frame_dados_recuperados.grid(row=1, column=1, sticky=NW, pady=5, padx= 5)

frame_dados_mortes = Frame(janela, width= 220, height=100, bg=co2, relief="flat")
frame_dados_mortes.grid(row=1, column=2, sticky=NW, pady=5, padx=5)

select_country = Frame(janela, width= 840, height=50, bg=co6, relief="flat")
select_country.grid(row=2, column=0, columnspan=3,sticky="n", pady=10)




app_nome = Label(app_nome_frame, text='COVID-19', width=20, height=1, pady=20, relief='flat', anchor=CENTER, font=("Tahoma 25 bold"), bg=co2, fg=co0)
app_nome.grid(row=0, column=0, pady=5)

######################### Chamando a API ############################


response = requests.get("https://api.covidtracking.com/v1/us/daily.json")
info = response
info = json.loads(info.text)

######################### Set Default ############################
infectados = info[0]['positive']
mortes = info[0]['death']
recuperados = info[0]['pending']
data = datetime.date.today()

######################### criando infectados ########################

label_infectados = Label(frame_dados_infectados, text='Infectados', width=20, height=1, pady=7, padx=0,  relief='flat', anchor=NW, font=("Courier 15 bold"), bg=co2, fg=co0)
label_infectados.grid(row=0, column=0, pady=1, padx=13)

mostrar_infectados = Label(frame_dados_infectados, text=infectados, width=12, height=1, pady=7, padx=0,  relief='flat', anchor=NW, font=("Courier 25 bold"), bg=co2, fg=co0)
mostrar_infectados.grid(row=1, column=0, pady=1)

mostrar_infos = Label(frame_dados_infectados, text=str(data), width=25, height=1, pady=7, padx=0,  relief='flat', anchor=NW, font=("Courier 11 bold"), bg=co2, fg=co0)
mostrar_infos.grid(row=2, column=0, pady=1)

mostrar_infos = Label(frame_dados_infectados, text='Total de casos ativos de covid-19', width=33, height=1, pady=7, padx=0,  relief='flat', anchor=NW, font=("Courier 8 bold"), bg=co2, fg=co0)
mostrar_infos.grid(row=3, column=0, pady=1, padx=13)

mostrar_azul = Label(frame_dados_infectados, text='', width=33, height=1, pady=7, padx=0,  relief='flat', anchor=NW, font=("Courier 1 bold"), bg=co3, fg=co0)
mostrar_azul.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)


######################### criando rescuperados ########################


label_recuperados = Label(frame_dados_recuperados, text='Recuperados', width=20, height=1, pady=7, padx=0,  relief='flat', anchor=NW, font=("Courier 15 bold"), bg=co2, fg=co0)
label_recuperados.grid(row=0, column=0, pady=1, padx=13)

mostrar_recuperados = Label(frame_dados_recuperados, text=recuperados, width=12, height=1, pady=7, padx=0,  relief='flat', anchor=NW, font=("Courier 25 bold"), bg=co2, fg=co0)
mostrar_recuperados.grid(row=1, column=0, pady=1)

mostrar_infos = Label(frame_dados_recuperados, text=str(data), width=25, height=1, pady=7, padx=0,  relief='flat', anchor=NW, font=("Courier 11 bold"), bg=co2, fg=co0)
mostrar_infos.grid(row=2, column=0, pady=1)

mostrar_infos = Label(frame_dados_recuperados, text='Total de casos recuperados de covid-19', width=33, height=1, pady=7, padx=0,  relief='flat', anchor=NW, font=("Courier 8 bold"), bg=co2, fg=co0)
mostrar_infos.grid(row=3, column=0, pady=1, padx=13)

mostrar_verde = Label(frame_dados_recuperados, text='', width=33, height=1, pady=7, padx=0,  relief='flat', anchor=NW, font=("Courier 1 bold"), bg=co5, fg=co0)
mostrar_verde.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)


######################### criando mortes ########################

label_mortes = Label(frame_dados_mortes, text='mortes', width=20, height=1, pady=7, padx=0,  relief='flat', anchor=NW, font=("Courier 15 bold"), bg=co2, fg=co0)
label_mortes.grid(row=0, column=0, pady=1, padx=13)

mostrar_mortes = Label(frame_dados_mortes, text=mortes, width=12, height=1, pady=7, padx=0,  relief='flat', anchor=NW, font=("Courier 25 bold"), bg=co2, fg=co0)
mostrar_mortes.grid(row=1, column=0, pady=1)

mostrar_infos = Label(frame_dados_mortes, text=str(data), width=25, height=1, pady=7, padx=0,  relief='flat', anchor=NW, font=("Courier 11 bold"), bg=co2, fg=co0)
mostrar_infos.grid(row=2, column=0, pady=1)

mostrar_infos = Label(frame_dados_mortes, text='Total de mortes covid-19', width=33, height=1, pady=7, padx=0,  relief='flat', anchor=NW, font=("Courier 8 bold"), bg=co2, fg=co0)
mostrar_infos.grid(row=3, column=0, pady=1, padx=13)

mostrar_vermelho = Label(frame_dados_mortes, text='', width=33, height=1, pady=7, padx=0,  relief='flat', anchor=NW, font=("Courier 1 bold"), bg=co1, fg=co0)
mostrar_vermelho.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)


######################### criando seleção de países ########################

label_pais = Label(select_country, text="Selecione o país", width=13, height=1, pady=7, padx=0, relief='flat', anchor=NW, font=("Ivy 15 bold"), bg=co6, fg=co0)
label_pais.grid(row=0, column=0, pady=1, padx=13)

pais = ["Brasil", "EUA", "Chile", "Peru", "França", "Canada", "Mexico", "Honduras", "Africa do Sul", "Marrocos", "Egito", "Argelia", "Israel", "Arabia Saudita", "Omã", "Qatar", "Kwaitii", "Síria", "Irã", "Iraque", "Turquia", "Tunísia", "Ucrania", "Itália", "Grécia", "Bósnia", "Sérvia", "Bulgária", "Bielorussia", "Estonia", "Lituania", "Letonia", "Russia", "Austria", "Suécia", "Dinamarca", "Suiça", "Portugal", "Noruega", "Islandia", "Inglaterra", "Irlanda", "Irlanda do Norte", "País de Gales", "Escocia", "Andorra", "Albania", "Republica Tcheca", "Mongolia", "China", "Laos", "Sri Lanka", "Taiti", "Australia", "nova Zelandia", "Filipinas", "Malasia", "Japao", "Afegnistao", "Paquistão", "Vietna", "Coreia do Norte", "Guine", "Suriname", "Angola", "Tanzania", "Congo", "Costa do Marfim", "Togo", "Zimbabue", "Madagascar", "Timor Leste", "Taiwan", "Haiti", "Cuba", "El Salvador", "Espanha", "Alemanha", "Croacia"]

combo = ttk.Combobox(select_country, width =15, font=("Ivy 8 bold"))
combo["values"] = (pais)
combo.grid(row=0, column=1, padx=0, pady=13)


def selecionar_pais(eventObject):
    pais_selecionado = combo.get()

    response = requests.get("https://api.covidtracking.com/v1/us/daily.json")
    info = response
    info = json.loads(info.text)

    index = pais.index(pais_selecionado)



    mortes = info[index]['death']
    recuperados = info[index]['pending']
    infectados = info[index]['positive']
    data = info[index]['date']

    mostrar_infectados.configure(text=infectados)
    mostrar_recuperados.configure(text=recuperados)
    mostrar_mortes.configure(text=mortes)


combo.bind("<<ComboboxSelected>>", selecionar_pais)

janela.mainloop()