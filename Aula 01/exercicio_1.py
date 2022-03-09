import pyautogui
import pyperclip
import time
import pandas as pd

pyautogui.PAUSE = 1 #pausa de 1 segundo entre cada comando

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('alt','space','x')
pyautogui.hotkey('ctrl','t')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(3) #depois do comando anterior ele espera 3 segundos

pyautogui.click(x=419, y=257, clicks=2)

time.sleep(3)

pyautogui.click(x=440, y=317)
pyautogui.click(x=1163, y=161)
pyautogui.click(x=1006, y=579)

time.sleep(4)

tabela = pd.read_excel(r'C:\Users\1801 Desktop\Downloads\Vendas - Dez.xlsx')

faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()

pyautogui.hotkey('ctrl','t')
pyperclip.copy('https://mail.google.com/')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(5)

pyautogui.click(x=112, y=181)
time.sleep(2)

pyautogui.write('teste@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write('Faturamento da Empresa')
pyautogui.press('tab')
texto = f'''
        Exercício de Python:
        O faturamento de ontem foi de: R$ {faturamento:,.2f}
        A quantidade de produtos foi de: {quantidade}
'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl','v')

pyautogui.hotkey('ctrl','enter')
