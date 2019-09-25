root_arr = os.path.realpath(__file__).split('/')[:-2]
root = '/'.join(root_arr) 
src_path = root + '/learn/'
sys.path.append(src_path)

from kit import *