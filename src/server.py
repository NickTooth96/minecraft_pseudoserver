import datetime
import toml


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
    print(name)
    with open('servers.toml', 'r') as f:
        config = toml.load(f)

def update_local(name):
    print(name)
        