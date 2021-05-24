import subprocess


def rn(command):
    subprocess.run(command, shell=True)
def strun(command):
    global output
    standard = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
    output= standard.stdout.decode()
    output = output.replace('\n', '')