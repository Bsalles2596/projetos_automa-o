## Ler dados de uma planilha
## Inserir em cada célula de cada linha em um campo do sistema

import openpyxl
import pyautogui

workbook = openpyxl.load_workbook('login_senha.xlsx')

dados_user = workbook['dados']

for linha in dados_user.iter_rows(min_row=2):
    ##login
    pyautogui.click(1808,452, duration=1.5)
    pyautogui.write(linha[0].value)
    ##senha
    pyautogui.click(1808,476, duration=1.5)
    pyautogui.write(str(linha[1].value))
    ##salvar
    pyautogui.click(1808,452, duration=1.5)

print('\n================================')    
