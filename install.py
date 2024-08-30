#### APP QUE INSTALA O SISTEMA NO PC
import subprocess
import os
import zipfile
import logging
import time
# Importações de bibliotecas de terceiros
import requests
import subprocess

# Variáveis globais
url_starter_zip = 'https://github.com/smedsarandi/starter/raw/main/dist/starter_exe.zip'
arquivo_exe = 'starter.exe'
arquivo_zip_destino = 'c:/Windows/Temp/starter_exe.zip'
arquivo_exe_destino = 'c:/Windows/Temp/starter_exe.exe'

logging.basicConfig(level=logging.INFO, filename="c:/Windows/Temp/starter.log", format="%(asctime)s - %(levelname)s - %(message)s")

def starter_download(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(arquivo_zip_destino, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        logging.info('Arquivo baixado')
        
        with zipfile.ZipFile(arquivo_zip_destino, 'r') as zip_ref:
            logging.info('Extraindo arquivo zip')
            zip_ref.extractall('c:/Windows/Temp')
        
        time.sleep(5)
        os.remove(arquivo_zip_destino)
    else:
        logging.error(f"Erro ao baixar o arquivo: Status code {response.status_code}")


def create_task():
    try:
        subprocess.Popen('schtasks /create /sc ONLOGON /ru System /tr c:\\Windows\\Temp\\starter.exe /tn Microsoft\\Windows\\starter\\starter', shell=True)

    except Exception as e:
        print(f'Tarefa starter NÃO foi criada: {e}')
