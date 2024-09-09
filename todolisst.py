a=None
listdo=[]
print("TODOLIST @CODESOFT cc%AYUSH RAJ")
while(a!=1):
    file=input("Open existing(o)/create new(n):")
    filename=input("Enter the file name:")+'.txt'
    
    if file.lower()=='o':
        try:
            with open(filename,'r') as f:
                listdo=f.read().splitlines()
                a=1
                print(f"{filename} found")

        except FileNotFoundError:
            print("Error! File not found")

    elif file.lower()=='n':
        # filename=input("Enter thr file name to be created:")
        print(f"{filename} created sucessfully")
        a=1
    
    else:
        print("Invalid choice")


print('''Hey! Welcome to our todolist powered by CODESOFT
      Here are the commands you can use:
      'add- <task>' to add a task
      'remove- <task>' to remove a task
      'show- list' to view your list
      'save- list' to save your list
      'exit- list' to exit(Make sure to save changes before exiting!)''')

operation=None
while(operation!='exit'):
    operation,task=map(str,input(f"Enter your operation or do 'save- {filename}' and 'exit- {filename}' to quit: ").split('-'))
    
    if operation.lower()=='add':
        listdo.append(task)
        print(f"Task '{task}' added successfully")
    
    elif operation.lower()=='remove':
        listdo.remove(task)
        print(f"Task '{task}' removed successfully")
    
    elif operation.lower()=='show':
        for i in range(0,len(listdo)):
            print(i+1,listdo[i])
   
    elif operation.lower()=='exit':
        if(input("confirm exit?? enter 'yes' else 'no': ")=='y'):
            print(f"Succoess! {filename} closed")
            break

        else:
            continue
    
    elif operation.lower()=='save':
        with open(filename, 'w') as f:
            for item in listdo:
                f.write("%s\n" %item)
        print(f"{filename} saved")

    else:
        print("Invalid input")