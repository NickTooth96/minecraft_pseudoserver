import os 


def world():
    user_path = os.path.expanduser('~')
    dir_list = os.listdir(user_path)


    for x in dir_list:
        print(x)
        if os.path.isfile(x):
            print("\t",x)
