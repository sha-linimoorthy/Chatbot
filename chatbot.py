'''
from random import randint


def rand_greet():
    quit_msg=["bye","kanda","see you","quit"]
    greet_scr=["Yo","Hello","vanakkam","namaste","subam"]
    n=randint(0,len(greet_scr))
    return(greet_scr[randint(0,n-1)])
    print(rand_greet())


while True:
    quit_msg=["bye","kanda","see you","quit"]
    msg=input()
    if msg in quit_msg:
        break
    else:
        print(msg)
        '''

from random import randint


def rand_greet():
    quit_msg=["bye","kanda","see you","quit"]
    greet_scr=["Yo","Hello","vanakkam","namaste","subam"]
    n=randint(0,len(greet_scr))
    return(greet_scr[randint(0,n-1)])
print(rand_greet(),"i can do simple calculations")


while True:
    quit_msg=["bye","kanda","see you","quit"]
    greet_scr=["Yo","Hello","vanakkam","namaste","subam"]
    msg=input()
    if msg in quit_msg:
        break
    else:
        if "add" in msg:
            split_msg=msg.split()
            print(int(split_msg[1])+int(split_msg[2]))
        elif (msg) in greet_scr:
            print(msg)
        elif "mul" in msg:
            split_msg=msg.split()
            print(int(split_msg[1])*int(split_msg[2]))
        elif "div" in msg:
            split_msg=msg.split()
            print(int(split_msg[1])/int(split_msg[2]))
        elif "modu" in msg:
            split_msg=msg.split()
            print(int(split_msg[1])%int(split_msg[2]))
        elif "eineq" in msg:
            split_msg=msg.split()
            print(int(split_msg[1])*int(split_msg[2])*int(split_msg[2]))
        elif "sub" in msg:
            split_msg=msg.split()
            print(int(split_msg[1])-int(split_msg[2]))
            





            
