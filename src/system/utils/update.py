import sys
sys.path.append("..")

import os

from src.bin.access import access
from misc.colors import colors as C


HOME = os.path.expanduser('~')


def update():
    ret = access()
    
    if ret:
        if not os.path.exists(f"{HOME}/repo"):        
            os.system("git clone https://github.com/testno0/repo $HOME/ &> /dev/null")
        else:
            print(f"{C.BOLD+C.GREEN} User system setup passed.{C.END}")
            os.system(f"cd {HOME}/repo/ && git pull")
    else:
        # false phase, pass : #? passing
        os.system("rm -rf {HOME}/repo/")
        
        print(f"""
              {C.BOLD+C.RED}> Verification error, repository was nuked by system for security.{C.END}""")            
        #systemctl poweroff