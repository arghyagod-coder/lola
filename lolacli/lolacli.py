import click
import requests
import os
import subprocess as sb


def run(command):
    sb.run(command, shell=True)


apps = '''
gimp
da-vinci-resolve
wine
libreoffice-full
krita
brave-browser
brave-beta
brave-nightly
edge-beta
firefox
chrome
lutris
g-drive
blender
python3
miniconda
anaconda
pip3
java-development-kit-11
java-development-kit-14-oracle
vscode
atom-editor
thonny
sublimetext
g++
clang
gcc 
pycharm-community
intellij-community
thunderbird
evolution
kazam
golang
r-lang
rstudio
virtualbox
scribus
plank-dock
calibre
chromium
zoom
dropbox
vlc
skype
gparted
minecraft
audacity
audacious
htop
dos-box
desmume
vim
kate
gedit
jedit
kate
emacs
telegram
signal
g-earth
steam
codeblocks
netbeans
lazarus-pascal
geany
dconf
spyder
terminator
kdenlive
obs
simple-screen-recorder
geogebra
etcher
cheese
spotify
discord
tuxpaint
stellarium
pinta
mypaint
shotwell
nodejs
'''


@click.group()
@click.version_option('0.2.1', prog_name='Lola')
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
                f"https://raw.githubusercontent.com/arghyagod-coder/lola/master/lolacli/scripts/{file}.sh").text

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
