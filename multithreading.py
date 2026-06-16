#multithreading

import threading
import time

def walk_dog(first):
    time.sleep(8)
    print(f"Fininshed Walking {first}")

def take_out_trash():
    time.sleep(2)
    print("Taking out the trash")

def get_mail():
    time.sleep(4)
    print("Getting the mail")

#walk_dog()
#take_out_trash()
#get_mail()

chore1 = threading.Thread(target=walk_dog , args=("Mints",))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

print("All chores Complete")
