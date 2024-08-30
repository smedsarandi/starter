#### AJUDA A FAZER O BUILD DE MANEIRA AUTOMATIZADA

import subprocess, time, shutil

subprocess.run('pyinstaller --onefile install.py')
time.sleep(10)
subprocess.run('pyinstaller --onefile starter.py')
time.sleep(10)
subprocess.run('pyinstaller --onefile starter_exe.py')

