import click
import subprocess as sb 


def run(command):
    sb.run(command, shell=True)

apps='''gimp
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
nodejs'''
	

@click.group()
@click.version_option('0.1.7', prog_name= 'Lola')
def main():
	'''I am Lola! Your assistant who can help you setup your Linux in an easy way! You can know more about me in https://github.com/arghyagod-coder/lola.

I can help you install apps through terminal, and you need to know almost nothing about the terminal to do so! Just simple prompts will be enough'''
	pass

@main.command('check-apps', help='Check the list of supported apps!')
def checkapps():
	print(apps)

@main.command('install', help= ('Install an app'))
@click.argument('filesl', nargs=-1)
def install(filesl): 
	for files in filesl:
		run(f'cd ~/Downloads; wget https://raw.githubusercontent.com/arghyagod-coder/lola/blob/master/lolacli/scripts/{files}.sh; bash {files}.sh; rm {files}.sh')
