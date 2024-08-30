import subprocess, time, shutil

subprocess.run('pyinstaller --onefile install.py')
time.sleep(10)
subprocess.run('pyinstaller --onefile starter.py')
subprocess.run('')
