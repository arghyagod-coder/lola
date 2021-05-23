from runfile import rn as run

apps=[]
with open('apps.txt') as f:
    apps = f.readlines()

for app in apps:
    app = app.replace('\n', '')
    app = app.replace(' ', '')
    run(f'touch {app}.sh')