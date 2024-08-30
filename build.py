#### AJUDA A FAZER O BUILD DE MANEIRA AUTOMATIZADA

import subprocess, time, shutil

subprocess.run('pyinstaller --onefile --windowed --name install install.py')
time.sleep(10)
subprocess.run('pyinstaller --onefile --windowed --name starter starter.py')
time.sleep(10)
subprocess.run('pyinstaller --onefile --windowed --name starter_exe starter_exe.py')

