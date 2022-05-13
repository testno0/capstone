import sys
from difflib import SequenceMatcher as SM
from os import path
from time import sleep

from function import System
from bin.code_email import Email
from misc.colors import colors as C
from face_recog import face_recognition

# repo link is the link of this repository https://github.com/testno0/repo
# although leave it blank as first, no one touchers the parameters
def main():
    """initiate the system, use try, except, else block to catch errors
    and to organize the procedures based on the cases the system gives."""

    HOME_ = path.expanduser("~")

    #with open(f"{HOME_}/.att_sys/user_info") as info:
        #source = info.readlines()

    #receiver_email = source[0].rstrip().strip() 
    #school_name = source[3].rstrip().strip()
    #sys_initiate = System(HOME_, "https://github.com/testno0/repo", receiver_email)

    try:
        pass
        """    print(f"{C.GREEN+C.BOLD}> Fetching data.{C.END}")
        if not path.exists(f"{HOME_}/repo"):
            print(
                f"{C.GREEN+C.BOLD}> The repository is not setup. Setting up the repository.{C.END}"
            )
            student_data, teacher_data = sys_initiate.setup(school_name)        
        else:
            student_data, teacher_data = sys_initiate.get_data()"""
    except ConnectionError: # add other exceptions later
        raise SystemExit(f"{C.RED+C.BOLD}> Connection Error.{C.END}")
    except KeyboardInterrupt:
        raise SystemExit(f"{C.RED+C.BOLD}> Keyboard Interrupt.{C.END}")
    except SystemError:
        raise SystemExit(f"{C.RED+C.BOLD}> System Error.{C.END}")
    else:
        # notify the user
        print(f"{C.GREEN+C.BOLD}> System ready.{C.END}", end="\r")

        sleep(5) # init free time
        sys.stdout.write("\033[K") # remove the messages
       
        email = Email("jaaaderang@gmail.com", "tello")
        while True:
            cardID = sys.argv[0]            
 
            if face_recognition():                        
                print(f"{C.GREEN+C.BOLD}> Student recognized.{C.END}")
                email.send(
                    "student true",
                    "hello",
                    "hello"
                )
            else:
                print(f"{C.RED+C.BOLD}> Error.{C.END}")
                # leave at blank first
                email.send(
                    "student true",
                    "hello",
                    "hello"
                )
 
            continue