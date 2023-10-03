import os
import time
import toml


access_error = 'ERROR: Access Denied'


def world(world_name,search_path=os.path.expanduser('~')):
    start_time = time.time()
    result = ""
    with open('data.toml', 'r') as f:
        config = toml.load(f)
    
    for possible_path in config['save_location']['paths']:
        result = search(world_name,possible_path)
    if result == "":
        result = search(world_name,search_path)
    run_time = time.time() - start_time
    print(f'--- Execution Time: {run_time:.2f} ---')  
    return result


def search(world_name,search_path):
    
    for subdir, dirs, files in os.walk(search_path):
        for file in files:
            split_tup = os.path.splitext(file)
            file_name = split_tup[0]
            file_extension = split_tup[1]
            if file_extension == '.txt' and "levelname" in file_name:
                level_name = os.path.join(subdir, file)
                if check(level_name,world_name):
                    save_location(level_name)                                      
                    return level_name
    return f'No file matching "{world_name}" found'

def check(file_path, name):
    lines = open(file_path, 'r').readlines()
    if name in lines:
        return True
    return False

def save_location(location):
    with open('data.toml', 'r') as f:
        # possible home dir for saves (only here to potentially save time)
        worlds_directory = os.path.dirname(os.path.dirname(location))
        config = toml.load(f)
        if worlds_directory not in config['save_location']['paths']:
            config['save_location']['paths'].append(worlds_directory)            
            with open('data.toml', 'w') as f:
                toml.dump(config, f)
        print(config['save_location']['paths'])
       
