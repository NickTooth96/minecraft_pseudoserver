import sys
import src.locate as locate
import src.server as server


ERROR_msg = 'Unnamed ERROR'

sys.argv.pop(0)

if '--find' in sys.argv or '-f' in sys.argv:     
    try: 
       index = sys.argv.index('--find') + 1  
    except:
        index = sys.argv.index('-f') + 1        
    if '--path' in sys.argv:
       path = sys.argv[sys.argv.index('--path') + 1]
       world_path = locate.world(sys.argv[index],path)
    else:
        world_path = locate.world(sys.argv[index])
    print(world_path)    
elif '--server' in sys.argv or '-s' in sys.argv:
    server.create('test')
elif '--update' in sys.argv or '-u' in sys.argv:
    try: 
       index = sys.argv.index('--update') + 1  
    except:
        index = sys.argv.index('-u') + 1
    if '--remote' in sys.argv:
        server.update_remote(sys.argv[index])
    elif '--local' in sys.argv:
        server.update_local(sys.argv[index])
else:
  print(ERROR_msg)