
import click
import requests
import os
import subprocess as sb


def run(command):
    sb.run(command, shell=True)


apps = '''
anaconda ------------- Anaconda- Powerful Tool for DS, DL and ML learners
atom-editor ---------- Atom Code Editor 
audacious ------------ Audacious Music Player
audacity ------------- Professional Audio Edition Software
blender -------------- Open Source 3D Creation Suite
brave-browser -------- Brave Browser- Fast, Light and Secure
brave-beta ----------- Brave Browser BETA- Regular updates and Bug Fixes
brave-nightly -------- Brave Nightly- Nightly Updates and Bug Fixes
calibre -------------- Free E-Book Suite
cheese --------------- Camera App for Linux
chrome --------------- Google Chrome Browser, the No.1 Browser in market
chromium ------------- Chromium Browser- A Light Browser like Chrome by GOOGLE
clang ---------------- CLang Compiler for C
codeblocks ----------- Code::Blocks editor- Fast and Powerful
crystal -------------- Crystal language support
dconf ---------------- Manage your config files with DConf editor for Linux
desmume -------------- DesMume Emulator for NDS and GB Games
discord -------------- Discord Client in Linux
dos-box -------------- DOS-BOX Emulator
dropbox -------------- Cloud Storage Client
edge-beta ------------ MS Edge for Linux- Regular Updates 
emacs ---------------- Featureful Text Editor
etcher --------------- Professional ISO Disk Image Writer
evolution ------------ A lightweight yet reliable Mail Client
firefox -------------- Firefox Web Browser- Security at top
fish-sh -------------- Fish Shell
g-drive -------------- Google Drive Client for Linux
g-earth -------------- Google Earth Feature for Linux
g++ ------------------ G++ Compiler for C/CPP
gcc ------------------ GCC Compiler for C
geany ---------------- Lightweight Text Editor
gedit ---------------- Casual Text Editor
geogebra ------------- Applications for dealing with mathematical operations and visualizations
gimp ----------------- Professional Photo Edition Software
golang --------------- Go Language for Linux
gparted -------------- Manage your disks and partitions with GParted
htop ----------------- Monitor your resources with htop
intellij-community --- IntelliJ IDEA Community Edition
java-development-kit-11 --- JDK 11 for Linux
jedit----------------- Casual Text Editor
kate ----------------- Casual Text Editor
kazam ---------------- Light Screen Recorder for Linux
kdenlive ------------- Casual Video Edition Software
krita ---------------- Bring your artistic skills to life with Krita
lazarus-pascal ------- Pascal IDE 
libreoffice-full ----- Complete Office Suite
lutris --------------- Open Source Gaming Platform for Linux
minecraft ------------ One of the world's most popular games, officially on Linux
miniconda ------------ Miniconda- Light and Powerful
mypaint -------------- Draw beautiful art with MyPaint
nim ------------------ Nim Language Support
nodejs --------------- NodeJS for Linux
obs ------------------ Professional Screen Recorder
pinta ---------------- Draw beautiful images with Pinta
pip3 ----------------- Pip3 package manager for Linux
plank-dock ----------- Plank Dock for Desktop Linux
powershell ----------- POWERSHELL for Linux
pycharm-community ---- PyCharm Community Edition
python3 -------------- Python 3.8 for Linux
r-lang --------------- R Language for linux
rstudio -------------- Best IDE for R Programming
sass ----------------- Language Support SASS through npm
scribus -------------- Professional DTP Software
shotwell ------------- Shotwell light casual Image Editor
signal --------------- Signal client for Linux
simple-screen-recorder -- Professional Screen Recorder
skype ---------------- Skype Client for Business Chats, Meetings etc
spotify -------------- Spotify Client
spyder --------------- An IDE for Scientists
steam ---------------- Steam Proton Client for Linux
stellarium ----------- Visualization Applications for Scientists
sublimetext3 --------- Sublime Text 3- A powerful yet lightweight Editor
sublimetext4 --------- Sublime Text 4
telegram ------------- Telegram Client for Linux
terminator ----------- Terminal Manager Terminator
thonny --------------- Thonny Python Beginner's IDE
thunderbird ---------- Thunderbird Mail Client from Moz://a
tuxpaint ------------- TUX Paint client
v-lang --------------- V Language and Compiler
vim ------------------ Professional Terminal Text Editor
virtualbox ----------- Make and Manage Virtual Machines with Vbox
vlc ------------------ No. 1 Media Player
vscode --------------- Visual Studio Code Text Editor
wine ----------------- Run Windows apps/games on Linux with WINE
zoom ----------------- Zoom Client for Conferences and Meetings
zsh-sh --------------- Zsh Shell
'''


@click.group()
@click.version_option('0.2.3', prog_name='Lola')
def main():
    '''I am Lola! Your assistant who can help you setup your Linux in an easy way! You can know more about me in https://github.com/arghyagod-coder/lola.
I can help you install apps through terminal, and you need to know almost nothing about the terminal to do so! Just simple prompts will be enough'''
    pass


@main.command('list', help='Check the list of supported apps!')
def list():
    print(apps)


@main.command('install', help=('Install an app'))
@click.argument('files', nargs=-1)
def install(files):
    for file in files:
        try:
            # * changing working directory to the downloads dir
            os.chdir(os.path.join(os.path.expanduser("~"), "Downloads"))

            # * requesting the installation script
            resp = requests.get(
                f"https://raw.githubusercontent.com/arghyagod-coder/lola/master/scripts/{file}.sh").text

            # * writing response text into a file
            with open(f"{file}_install.sh", 'w') as f:
                f.write(resp)

            with open(f'{file}_install.sh') as script_file:
                script = script_file.read()
                if script == "404: Not Found":
                    raise FileNotFoundError()

            # * running and then removing the bash script
            run(f"bash {os.path.join(os.getcwd(), file)}_install.sh")
            os.remove(os.path.join(os.getcwd(), f"{file}_install.sh"))

        except FileNotFoundError:
            print('This app is not available to download via lola yet :(')

        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()