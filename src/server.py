import datetime
import os
import shutil
import toml

ROOT_DIR = os.path.dirname(os.path.abspath('minecraft_pseudoserver.py'))
def create(name):
    path = 'stand_in'
    with open('servers.toml', 'r') as f:
        config = toml.load(f)
        if not config['servers'][f'servers.{name}']:
            with open('data.toml', 'w') as f:
                config['servers'][f'servers.{name}']
                config['servers'][f'servers.{name}']['name'] = name
                config['servers'][f'servers.{name}']['path'] = path
                config['servers'][f'servers.{name}']['last_update'] = datetime.datetime.timestamp()

def update_remote(name):   
    
    with open('servers.toml', 'r') as f:
        config = toml.load(f)
        name = config[name]['name']
        date = datetime.datetime.now()
        path = config[name]['path']
    copy(name,path)
    os.system('git add -u')
    os.system('git status')


def update_local(name):
    print(name)

def copy(name,src_path):
    dst = os.path.join(ROOT_DIR,'backups',name)
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src_path, dst)        