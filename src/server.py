import datetime
import os
import shutil
import toml

ROOT_DIR = os.path.dirname(os.path.abspath('minecraft_pseudoserver.py'))
def create(name):
    path = 'stand_in'
    with open('servers/servers.toml', 'r') as f:
        config = toml.load(f)
        if not config['servers'][f'servers.{name}']:
            with open('data.toml', 'w') as f:
                config['servers'][f'servers.{name}']
                config['servers'][f'servers.{name}']['name'] = name
                config['servers'][f'servers.{name}']['path'] = path
                config['servers'][f'servers.{name}']['last_update'] = datetime.datetime.timestamp()

def update_remote(name):   

    commit_message = f'SYNC: {datetime.datetime.now()} | by {os.getlogin()}'    
    with open('servers/servers.toml', 'r') as f:
        config = toml.load(f)
    name = config[name]['name']
    path = config[name]['path']
    date = datetime.datetime.now()
    dst = os.path.join(ROOT_DIR,'backups',name)
    copy(path,dst)
    server = os.path.join(ROOT_DIR,'servers',os.path.basename(path))
    copy(path,server)

    with open('servers/servers.toml', 'w') as f:
        config[name]['last_update'] = f'{date.timestamp()}' 
        toml.dump(config, f)



    os.system(f'git add .\\servers\\{os.path.basename(path)}\ .\\backups\\*')
    os.system(f'git commit -m "{commit_message}"')
    os.system('git push')


def update_local(name):
    with open('servers/servers.toml', 'r') as f:
        config = toml.load(f)
    name = config[name]['name'] 
    path = config[name]['path']

    os.system('git pull')
    server = os.path.join(ROOT_DIR,'servers',os.path.basename(path))
    print(server,"\n",path)
    copy(server,path)
    

def copy(src_path,dst_path):
    if os.path.exists(dst_path):
        shutil.rmtree(dst_path)
    shutil.copytree(src_path, dst_path)        