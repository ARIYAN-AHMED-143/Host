
from os import system as mina
mina('clear')

def linex():
    print(f'''{white}——————————————————————————————————————''')

A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\x1b[1;33m'
G = '\x1b[38;5;46m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;48m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\x1b[1;34m'
X1 = '\x1b[38;5;14m'
W = '\x1b[38;5;123m'
P = '\x1b[38;5;122m'
T = '\x1b[38;5;86m'
U = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
G0 = '\x1b[38;5;46m'
yellow = '\x1b[38;5;208m'
black = '\x1b[1;30m'
rad = '\x1b[1;31m'
green = '\x1b[38;5;46m'
yelloww = '\x1b[1;33m'
blue = '\x1b[1;34m'
purple = '\x1b[1;35m'
cyan = '\x1b[1;36m'
white = '\x1b[1;37m'
faltu = '\x1b[1;41m'
pvt = '\x1b[1;0m'
G16 = '\x1b[1;92m\x1b[38;5;208m'
G17 = '\x1b[1;92m\x1b[38;5;209m'
G18 = '\x1b[1;92m\x1b[38;5;210m'
logo = f'''\n{G16}┳┓┏┓┏┓┏┓┳┓┏┓  ┳┓┓┏  ┳┓┏┓┓┏┓┳┳┓\n{white}┃┃┣ ┃ ┃┃┃┃┣ ━━┣┫┗┫━━┣┫┣┫┃┫ ┃┣┫\n{G16}┻┛┗┛┗┛┗┛┻┛┗┛  ┻┛┗┛  ┛┗┛┗┛┗┛┻┻┛ \n{white}——————————————————————————————————————   \n{yellow}╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\n{yellow}║{green} [ WORKING ONLY 64-BIT ]{yellow}    ║\n{yellow}╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝       \n{white}——————————————————————————————————————                \n\x1b[1;37m——————————————————————————————————————\x1b[1;97m\n\x1b[1;37m(\x1b[36m●\x1b[1;37m) OWNER  : MAHADI HASAN RAKIB\n\x1b[1;37m(\x1b[36m●\x1b[1;37m) GITHUB : argrakib007\n\x1b[1;37m(\x1b[36m●\x1b[1;37m) TOOL   : DECODE \x1b[38;5;50m[ \x1b[38;5;50mGIFT ]\n\x1b[1;37m(\x1b[36m●\x1b[1;37m) VIRSON : {G}V{black}\\{blue}A\n\x1b[1;37m——————————————————————————————————————\x1b[1;97m\n  '''
print(logo)
open('/data/data/com.termux/files/usr/bin/pycdc')
open('/data/data/com.termux/files/usr/lib/python3.11/minopyc.py', 'r').read()
open('/data/data/com.termux/files/usr/bin/pycdas')
mina('curl -O https://raw.githubusercontent.com/i4mMino/pycdc/main/pycdc')
mina('curl -O https://raw.githubusercontent.com/i4mMino/pycdc/main/pycdas')
mina('curl -O https://raw.githubusercontent.com/i4mMino/pycdc/main/minopyc.py')
mina('mv pycdc /data/data/com.termux/files/usr/bin/')
mina('mv pycdas /data/data/com.termux/files/usr/bin/')
mina('mv minopyc.py /data/data/com.termux/files/usr/lib/python3.11/')
mina('chmod 777 /data/data/com.termux/files/usr/lib/python3.11/minopyc.py')
mina('chmod 777 /data/data/com.termux/files/usr/bin/pycdc')
mina('chmod 777 /data/data/com.termux/files/usr/bin/pycdas')
print(f'''{rad}[{white}=/{rad}] {U}MARSHAL{black}-{U}ZLIB{black}-{U}BASH64{black}-{U}DECODE''')
print(f'''{rad}[{white}=/{rad}] {U}MARSHAL{black}-{U}DECODE''')
linex()
file = input(f'''\n{rad} [{white}=/{rad}] {G16}ENTER YOUR FILE {white}➤{cyan} ''')
open(file)
mina(f'''cp {file} .b.py''')
exit(f'''{rad} [{white}=/{rad}] {G18}VALID OPTION - FILE''')
open(file).read()
mina('pycdc .b.py > .a.py')
files = open('.a.py', 'r').read()
if 'exec(str(chr' in files:
    c = files.split(']')[0] + "]\nprint(''.join([chr(i) for i in _]))"
    files = open('.a.py', 'w').write(c)
    mina('python3 .a.py > .b.py')
mina('mv .a.py .b.py')
print('Please Wait Trying To Decoding , Mide By ➺ \x1b[38;5;121mRAKIB')
file = open('.b.py', 'r').read()
if "(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(b" in file:
    filer = file.split('exec(')[1]
    open('.b.py', 'w').write('import minopyc,marshal\ncode =(' + filer + "\nminopyc.dump_to_pyc(code, '.a.py')")
    mina('python3 .b.py;pycdc .a.py > .b.py')
if "(__import__('marshal').loads(__import__('marshal').loads(__import__('marshal').loads(" in file:
    filer = file.split('exec(')[1]
    open('.b.py', 'w').write('import minopyc,marshal\ncode =(' + filer + "\nminopyc.dump_to_pyc(code, '.a.py')")
    mina('python3 .b.py;pycdc .a.py > .b.py')
if 'exec(_(' in file:
    c = file.split('exec(_(')[1]
    l = 'import marshal,zlib,base64,minopyc\nx = ((' + c + "\ny = x[:: -1]\nb = marshal.loads(zlib.decompress(base64.b64decode(y)))\nminopyc.dump_to_pyc(b,'.a.py') "
    open('.b.py', 'w').write(l)
    mina('python .b.py')
    mina('pycdc .a.py > .b.py')
if 'exec((_)(' in file:
    c = file.split('exec((_)(')[1]
    l = 'import marshal,zlib,base64,minopyc\nx = ((' + c + "\ny = x[:: -1]\nb = marshal.loads(zlib.decompress(base64.b64decode(y)))\nminopyc.dump_to_pyc(b,'.a.py') "
    open('.b.py', 'w').write(l)
    mina('python .b.py')
    mina('pycdc .a.py > .b.py')
if 'exec(marshal.loads' in file:
    filer = file.replace('exec(', 'code=(')
    open('.b.py', 'w').write('import minopyc,marshal\n' + filer + "\nminopyc.dump_to_pyc(code, '.a.py')")
    mina('python3 .b.py;pycdc .a.py > .b.py')
if 'exec((lambda __,' in file:
    filer = file.replace('exec(', 'print(')
    open('.a.py', 'w').write(filer)
    mina('python2 .a.py > .b.py')
c = open('.b.py', 'r').read()
if c == '':
    print('The Tool Can Just Decoded Data')
    save = input('Enter Path To save From : ')
    mina(f'''pycdas .a.py > {save}''')
    mina('rm .a.py;rm .b.py')
if 'WARNING: Decompyle incomplete' in c:
    print('The Tool Can Just Decoded Data')
    save = input('Enter Path To save From : ')
    mina(f'''pycdas .a.py > {save}''')
print('The Tool Decoded')
save = input('Enter Path To save From : ')
open(save, 'w').write(c)
open('.a.py')
mina('rm .a.py')
open('.b.py')
mina('rm .b.py')
exit('DO NE ei')
