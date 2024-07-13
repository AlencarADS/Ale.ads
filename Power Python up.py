# Passo a passo
# Passo 1 - Entrar no sistema
# passo 2 - Fazer o loguin 
# passo 3 - importar base de dados
# passo 4 - cadastrar o produto
# passo 5 - repetir até acabar a lista de produtos

import pyautogui
import time
  
# pyautogui.click - clicar com mouse
# pyautogui.write - escrever um texto
# pyautogui.press - apertar 1 tecla
# pyautogui.hotkey - combinação de teclas
# pyautogui.scroll - rolar a tela para cima ou para baixo


pyautogui.PAUSE = 0.8


# Passo 1 - entrar no sistema
# abrir o navegador


pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


# entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)


# Passo 2 - Fazer o loguin 
pyautogui.click(x=802, y=465)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("amantecod@gmail.com")
pyautogui.press("tab")
#campo de senha
pyautogui.write("amantecod")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# passo 3 - importar base de dados
import pandas 


tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Passo 4 - cadastrar um produto

# para cada linha da minha tabela:
for linha in tabela.index:
    #Codigo
    pyautogui.click(x=772, y=335)
    codigo = str(tabela.loc[linha,"codigo"])
    pyautogui.write(codigo)

    #Marca
    pyautogui.press("tab")
    marca = str(tabela.loc[linha,"marca"])
    pyautogui.write(marca)

    #Tipo
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha,"tipo"])
    pyautogui.write(tipo)

    #Categoria
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)

    #Preço
    pyautogui.press("tab")
    preco = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco)

    #custo
    pyautogui.press("tab")
    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
        
    #OBS
    time.sleep(0.3)
    
    pyautogui.click(x=831, y=756)
    obs = str(tabela.loc[linha,"obs"])
    if obs !="nan":
        pyautogui.write(obs)
   

    # enviar o cadastro 

    



