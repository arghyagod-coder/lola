import click
import subprocess as sb
from runfile import rn as run

apploc = 'https://raw.githubusercontent.com/arghyagod-coder/lola/blob/master/lola/apps.txt'
apps=[]
with open(apploc) as f:
    apps = f.readlines()
	

@click.group()
@click.version_option('0.1.4', prog_name= 'Lola')
def main():
	'''I am Lola! Your assistant who can help you setup your Linux in an easy way! You can know more about me in https://github.com/arghyagod-coder/lola.

I can help you install apps through terminal, and you need to know almost nothing about the terminal to do so! Just simple prompts will be enough'''
	pass

@main.command('check-apps')
def checkapps():
	for app in apps:
		print(app)

@main.command('install', help= ('Install an app'))
@click.argument('filesl', nargs=-1)
def install(filesl): 
	for files in filesl:
		run(f'cd ~/Downloads; wget https://raw.githubusercontent.com/arghyagod-coder/lola/master/lola/scripts/{files}.sh; bash {files}.sh; rm {files}.sh')
