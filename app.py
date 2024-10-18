# importar a biblioteca de automação
# há necessidade de instalação 'pip install pyautogui'
# instalação do cx Freeze pip install cx_Freeze
# comando para gerar o executável: cx_Freeze app.py --target-dir nome-pasta
 
"""Podemos usar também o PyInstaller. 
Passo 1: Instalar o PyInstaller
Primeiro, você precisa ter o PyInstaller instalado. Abra o terminal ou o prompt de comando e execute:
pip install pyinstaller

Passo 2: Navegar até o diretório do seu script
Mude para o diretório onde seu script Python está localizado. Por exemplo:

cd caminho/para/seu/script
Passo 3: Criar o executável
Execute o seguinte comando, substituindo seu_script.py pelo nome do seu arquivo:

pyinstaller --onefile seu_script.py
A opção --onefile cria um único arquivo executável.

Passo 4: Encontrar o executável
Após a execução, o PyInstaller criará uma pasta chamada dist. Dentro dessa pasta, você encontrará o executável do seu script.

Passo 5: Testar o executável
Execute o arquivo gerado para garantir que tudo funcione como esperado."""

import pyautogui as auto

auto.PAUSE = 0.5

auto.press("win")
auto.write("edge")
auto.press("enter")
auto.write("python.org")
auto.press("enter")
auto.hotkey("alt","space")
auto.press("x")
auto.hotkey("ctrl", "t")
auto.write("google.com.br")
auto.press("enter")
auto.write("Logo Python")
auto.press("enter")

for i  in range(14):
    auto.press("tab")

auto.press("enter")