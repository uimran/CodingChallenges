N = int(raw_input())
mylist=[]
for i in range(N):
    #In order to identify the different parts of the command, split it in a list so that we can make use of the indexes
    command=raw_input().split()
    #At command[0], the string for the command is stored so we will start from command[1] where the number(s) is/are stored
    for j in range(1,len(command)):
        command[j] = int(command[j]) 
    if command[0] == "insert": 
        mylist.insert(command[1],command[2])
    elif command[0] == "print": 
        print mylist
    elif command[0] == "remove": 
        mylist.remove(command[1])
    elif command[0] == "append": 
        mylist.append(command[1])
    elif command[0] == "sort": 
        mylist.sort()
    elif command[0] == "pop": 
        mylist.pop()
    elif command[0] == "reverse": 
        mylist.reverse()
