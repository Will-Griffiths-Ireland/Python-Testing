from rich.console import Console
from rich.panel import Panel
import os
from rich import print
import time
os.system('cls' if os.name == 'nt' else 'clear')
c = Console()
f = open('logo.txt')
logo = f.read()
i=0
line = ''
for i in range(39):
    line += ' ✩'

index = 8
color = 'rgb('+ str(index) +','+ str(index) +',' + str(index) + ')'
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    c.print(line +'\n', style='yellow')
    c.print(logo, style = color)
    c.print(line +'\n', style='yellow')
    c.print('           A STAR IS A FIXED POINT OF LIGHT BY WHICH TO GUIDE US')
    c.print('           EVERY EVENT TAKES PLACES IN A SINGULAR MOMENT IN SPACE')
    c.print('           THE MANIFEST IS FINAL......')
    print('\n')
    time.sleep(.1)
    index += 10
    color = 'rgb('+ str(index) +','+ str(index) +',' + str(index) + ')'
    if index > 240:
        break

UERI = 'HGY6-GSRF-534R-H7DS'
name = input('Whats your name? : \n')
print('\n')
c.clear()
while len(name) < 20:
    name += ' '

c.print(f'╔════════[ Passport ]═════════╗ ╔═════════════════════════════╗', style="white on blue")
c.print(f'║                             ║ ║                             ║', style="white on blue")
c.print(f'║ Name: {name}  ║ ║ Name: {name}  ║' , style="white on blue")
c.print(f'║ UERI: {UERI}   ║ ║                             ║', style="white on blue")
c.print(f'║                             ║ ║                             ║', style="white on blue")
c.print(f'║                             ║ ║                             ║', style="white on blue")
c.print(f'║                             ║ ║                             ║', style="white on blue")
c.print(f'║                             ║ ║                             ║', style="white on blue")
c.print(f'╚═════════════════════════════╝ ╚═════════════════════════════╝', style="white on blue")


# print('╚╝╬═╩╠╣╦╔╗║')