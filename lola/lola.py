import click
import subprocess as sb
from runfile import rn as run

@click.group()
@click.version_option('0.1.4', prog_name= 'Lola')
def main():
	'''I am Lola! Your assistant who can help you setup your Linux in an easy way! You can know more about me in https://github.com/arghyagod-coder/lola.

I can help you install apps through terminal, and you need to know almost nothing about the terminal to do so! Just simple prompts will be enough'''
	pass

@main.command('install', help= ('Install an app'))
@click.argument('files', nargs=1)
def install(files):
    print(files)
    

	
if __name__=='__main__':
	main()

