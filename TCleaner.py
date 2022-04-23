import os ; import time ; from art import *
print(text2art("TCleaner" , font="Block"))
time.sleep(1.5)
print("Warning : when you use TCleaner all your history is will remove ! Do you want remove all Terminal History ")
print(os.system("rm .bash_history ; clear ; history -c"))
print(os.system("sudo rm .bash_history;clear;history -c"))
