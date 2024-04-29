import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
options = Options()
driver = webdriver.Chrome(service=service)
# Navegar para a página desejada
driver.get('https://downdetector.com')

# Esperar um pouco para garantir que a página tenha carregado completamente
time.sleep(2)

# Encontrar os elementos desejados
exercise_cards = driver.find_elements(By.CSS_SELECTOR, 'body > div.container.px-3.px-md-0 > div:nth-child(3)')

# Criar uma lista para armazenar os dados
dados = []

# Iterar sobre os elementos encontrados e extrair os textos
for exercise_card in exercise_cards:
    # Separar o texto em linhas
    linhas = exercise_card.text.split('\n')
    # Adicionar cada linha separadamente à lista de dados
    for linha in linhas:
        dados.append([linha])

# Encerrar o driver do Selenium
driver.quit()

# Criar o DataFrame com os dados coletados
df = pd.DataFrame(dados, columns=['Dados'])

# Exibir o DataFrame
print(df)

# Exibir os dados em formato de lista
print("Dados_coletados:")
for dado in df['Dados']:
    print(dado)


# Caminho para o arquivo CSV onde os dados serão armazenados
caminho_arquivo_csv = 'dados_coletados.csv'

# Armazenar os dados do DataFrame no arquivo CSV
df.to_csv(caminho_arquivo_csv, index=False)

print(f'Dados armazenados com sucesso em {caminho_arquivo_csv}')