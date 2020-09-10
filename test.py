
import subprocess
import os
from subprocess import Popen, PIPE
index1=1

if("nt" is os.name):    
    CREATE_NEW_PROCESS_GROUP = 0x00000200
    DETACHED_PROCESS = 0x00000008
    p = subprocess.Popen(['python3', 'C:\\xampp\\htdocs\\dashboard\\StockWatcher\\runConstant.py ',str(index1)], stdin=PIPE, stdout=PIPE, stderr=PIPE,  creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
else:
    p = subprocess.Popen(['python3', '/var/www/html/darwin/StockWatcher/runConstant.py',str(index1)],shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
print (p.pid)
# prints 29893