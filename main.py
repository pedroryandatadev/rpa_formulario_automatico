import pyautogui
import time

pyautogui.PAUSE = 1 #Tempo de pausa entre cada comando(segundos de demora de cada comando)

#1.    Abrindo o navegador
pyautogui.press('win')
pyautogui.write('edge') 
time.sleep(2)
pyautogui.press('enter')

#Fazendo a pesquisa no navegador
pyautogui.write('URL do site')
pyautogui.press('enter')

time.sleep(3) #Tempo de espera de um ponto do comando especifico por segundos


#2.    Fazendo login no sistema

pyautogui.click(x=348, y=547)
pyautogui.write('login') #Preencherar o login
pyautogui.press('tab') #Aperta em tab fara pular para o proximo input
pyautogui.write('senha')
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(3) #Tempo de espera de um ponto do comando especifico por segundos


#3.    Importando a base de dados

import pandas as pd

dados = pd.read_csv('base.csv')


#4.    Cadastrar os dados


#Execução em loop para cada linha da tabela
for linha in dados.index: #O index retorna a referencia da celula começando pelo zero

    #Clicando no primeiro input
    pyautogui.click(x=348, y=547)

    #Primeiro cadastro
    campo1 = dados.loc[linha, 'codigo'] #Varivel que pega a base e localiza a informação na "linha" e a coluna de nome "codigo"
    pyautogui.write(str(campo1)) #Cadastrando no input em formato de texto(string) a informação localizada na base
    pyautogui.press('tab')

    #Segundo cadastro
    campo2 = dados.loc[linha, 'nome']
    pyautogui.write(str(campo2))
    pyautogui.press('tab')

    #Terceiro cadastro
    campo3 = dados.loc[linha, 'tipo']
    #Condição se o dado for vazio ele não será usado
    if not pd.isna('tipo'): #O "isna" verifica se a informação e vazia (Especificação pq quando e vazio o python escreve NaN por padrão)
        pyautogui.write(str(campo3))
    pyautogui.press('tab')

    #Quarto cadastro
    campo4 = dados.loc[linha, 'preco']
    pyautogui.write(str(campo4))
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.press('home') #Faz o a rolagem retornar para o inicio da pagina 