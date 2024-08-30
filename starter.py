#### ESTE É O INICIO DE TUDO, SEMPRE EXECUTARÁ AO INICIALIZAR. ESTE QUE BAIXARÁ O "starter_exe.zip"
# Importações de bibliotecas padrão
import os
import zipfile
import logging
import time
# Importações de bibliotecas de terceiros
import requests
import shutil
import subprocess

# Variáveis globais
url_starter_zip = 'https://github.com/smedsarandi/starter/raw/main/dist/starter_exe.zip'
arquivo_exe = 'starter_exe.exe'
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


def starter_execute():
    try:
        # Executa o arquivo EXE extraído
        subprocess.run([arquivo_exe_destino], check=True)
        logging.info('Arquivo starter.exe executado com sucesso')
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro ao executar o starter.exe: {e}")


starter_download(url=url_starter_zip)
starter_execute()