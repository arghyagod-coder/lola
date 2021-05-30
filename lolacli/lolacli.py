
import click
import requests
import os
import subprocess as sb


def run(command):
    sb.run(command, shell=True)


apps = '''
crystal -------------- Crystal language support
nim ------------------ Nim Language Support
gimp ----------------- Professional Photo Edition Software
wine ----------------- Run Windows apps/games on Linux with WINE
libreoffice-full ----- Complete Office Suite
krita ---------------- Bring your artistic skills to life with Krita
brave-browser -------- Brave Browser- Fast, Light and Secure
brave-beta ----------- Brave Browser BETA- Regular updates and Bug Fixes
brave-nightly -------- Brave Nightly- Nightly Updates and Bug Fixes
edge-beta ------------ MS Edge for Linux- Regular Updates 
firefox -------------- Firefox Web Browser- Security at top
chrome --------------- Google Chrome Browser, the No.1 Browser in market
lutris --------------- Open Source Gaming Platform for Linux
g-drive -------------- Google Drive Client for Linux
blender -------------- Open Source 3D Creation Suite
python3 -------------- Python 3.8 for Linux
miniconda ------------ Miniconda- Light and Powerful
anaconda ------------- Anaconda- Powerful Tool for DS, DL and ML learners
pip3 ----------------- Pip3 package manager for Linux
java-development-kit-11 --- JDK 11 for Linux
java-development-kit-14-oracle --- JDK 14 Oracle Edition for Linux
vscode --------------- Visual Studio Code Text Editor
atom-editor ---------- Atom Code Editor 
thonny --------------- Thonny Python Beginner's IDE
sublimetext3 --------- Sublime Text 3- A powerful yet lightweight Editor
sublimetext4 --------- Sublime Text 4
g++ ------------------ G++ Compiler for C/CPP
clang ---------------- CLang Compiler for C
gcc ------------------ GCC Compiler for C
pycharm-community ---- PyCharm Community Edition
intellij-community --- IntelliJ IDEA Community Edition
thunderbird ---------- Thunderbird Mail Client from Moz://a
evolution ------------ A lightweight yet reliable Mail Client
kazam ---------------- Light Screen Recorder for Linux
golang --------------- Go Language for Linux
r-lang --------------- R Language for linux
rstudio -------------- Best IDE for R Programming
virtualbox ----------- Make and Manage Virtual Machines with Vbox
scribus -------------- Professional DTP Software
plank-dock ----------- Plank Dock for Desktop Linux
calibre -------------- Free E-Book Suite
chromium ------------- Chromium Browser- A Light Browser like Chrome by GOOGLE
zoom ----------------- Zoom Client for Conferences and Meetings
dropbox -------------- Cloud Storage Client
vlc ------------------ No. 1 Media Player
skype ---------------- Skype Client for Business Chats, Meetings etc
gparted -------------- Manage your disks and partitions with GParted
minecraft ------------ One of the world's most popular games, officially on Linux
audacity ------------- Professional Audio Edition Software
audacious ------------ Audacious Music Player
htop ----------------- Monitor your resources with htop
dos-box -------------- DOS-BOX Emulator
desmume -------------- DesMume Emulator for NDS and GB Games
vim ------------------ Professional Terminal Text Editor
kate ----------------- Casual Text Editor
gedit ---------------- Casual Text Editor
jedit----------------- Casual Text Editor
emacs ---------------- Featureful Text Editor
telegram ------------- Telegram Client for Linux
signal --------------- Signal client for Linux
g-earth -------------- Google Earth Feature for Linux
steam ---------------- Steam Proton Client for Linux
codeblocks ----------- Code::Blocks editor- Fast and Powerful
netbeans ------------- Netbeans Professional editor for Java, Python etc
lazarus-pascal ------- Pascal IDE 
geany ---------------- Lightweight Text Editor
dconf ---------------- Manage your config files with DConf editor for Linux
spyder --------------- An IDE for Scientists
terminator ----------- Terminal Manager Terminator
kdenlive ------------- Casual Video Edition Software
obs ------------------ Professional Screen Recorder
simple-screen-recorder -- Professional Screen Recorder
geogebra ------------- Applications for dealing with mathematical operations and visualizations
etcher --------------- Professional ISO Disk Image Writer
cheese --------------- Camera App for Linux
spotify -------------- Spotify Client
discord -------------- Discord Client in Linux
tuxpaint ------------- TUX Paint client
stellarium ----------- Visualization Applications for Scientists
pinta ---------------- Draw beautiful images with Pinta
mypaint -------------- Draw beautiful art with MyPaint
shotwell ------------- Shotwell light casual Image Editor
nodejs --------------- NodeJS for Linux
fish-sh -------------- Fish Shell
zsh-sh --------------- Zsh Shell
v-lang --------------- V Language and Compiler
sass ----------------- Language Support SASS through npm
powershell ----------- POWERSHELL for Linux
'''


@click.group()
@click.version_option('0.2.2', prog_name='Lola')
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