import time
start_time = time.time()
class Dir:
    def __init__(self,dirName) -> None:
        self.dirName = dirName
        self.files = []
        self.dirSize = 0

    def size (self):
        file_sizes = [int(x.split()[0]) for x in self.files]
        self.dirSize = sum(file_sizes)
        
    def addFile (self,file):
        self.files.append(file)
        fileSize = int(file.split()[0])
        self.dirSize += fileSize

def getChildren(dirList:list):
    childList = []
    if type(dirList) is list:
        for _dir in dirList:
            if type(_dir) is list:
                childList.append(_dir[0].dirName)
            else:
                childList.append(_dir.dirName)
    return childList[1:]
    

def addDir(currentDir:str,dirList:list):
    subs = currentDir.split("/")
    # print("*CD = ", currentDir)
    children = getChildren(dirList)
    if type(dirList) is Dir:
        print (dirList.dirName)
    if subs[0] in children:
        # print ('found',subs[0]) 
        if len(subs) > 1:
            cd2 = '/'.join(subs[1:])
            subdir = list(filter(lambda d : d[0].dirName==subs[0] if type(d) is list else d.dirName == subs[0], dirList[1:]))[0]
            addDir(cd2,subdir)
    else:
        # print ('not found',subs[0]) 
        if subs[0].split()[0].isdigit():
                # print ('adding file',subs[0])
                dirList[0].addFile(subs[0])
                # print (' -# folder size ',dirList[0].size())
        else:
            dirList.append([Dir(subs[0])])
        # print(dirList[-1])
        if len(subs) > 1:
            cd2 = '/'.join(subs[1:])
            addDir(cd2,dirList[-1])
            

def printDirList(dirList,levelStart):
    level = levelStart
    if type(dirList) is list:
        for _dir in dirList:
            if type(_dir) is list:
                if level == 0:
                    print ("##",_dir[0].dirName,_dir[0].files,_dir[0].dirSize)
                else: print ("---" * level,_dir[0].dirName,_dir[0].files,_dir[0].dirSize)
                if len(_dir) > 1:
                    level += 1
                    printDirList(_dir[1:],level)
                level = levelStart
            else:
                print ("#",_dir.dirName,_dir.files,_dir.dirSize)

def countFolders(dirList,value):
    # print ('startdir',dirList)
    global folder_sizes
    total_size = dirList[0].dirSize      
    if len(dirList) > 1:
        for _dir in dirList[1:]:
            total_size += countFolders(_dir,value)
    
    dirList[0].dirSize = total_size
    if total_size < value:
        folder_sizes.append(total_size)
    return total_size

def delete_folder(dirList,value):
    global folder_sizes
    size = dirList[0].dirSize   
    if size > value:
                folder_sizes.append(size)   
    if len(dirList) > 1:
        for _dir in dirList[1:]:
            delete_folder(_dir,value)


commands = ""
with open("day7.txt") as file:
    commands = file.read()

root=[Dir('/')]
input:str
CurrentDir:str = ""
for input in commands.splitlines():
    if input == "$ cd ..":
        cdlist = CurrentDir.split('/')
        cdlist.pop()
        CurrentDir = '/'.join(cdlist)
        # print ("..",CurrentDir)
        continue
    elif input == "$ cd /":
        CurrentDir = ""
        # print ("/", CurrentDir)
    elif input.startswith("$ cd"):
        if CurrentDir == "":
            CurrentDir = input.split()[-1]
        else:
            CurrentDir = '/'.join([CurrentDir, input.split()[-1]])
        # print ("cd",CurrentDir)
    
        if not(CurrentDir == ''):
            # print ("\tadding",CurrentDir)
            addDir(CurrentDir,root)

    if input.startswith("dir"):
        if not(CurrentDir == ''):
            cd = CurrentDir + '/' +input.split()[-1]
        else:
            cd = input.split()[-1]
        # print ("\tadding",cd)
        addDir(cd,root)

    if input.split()[0].isdigit():
        if not(CurrentDir == ''):
            cd = CurrentDir + '/' + input
        else:
            cd = input
        # print ("\tadding",cd)
        addDir(cd,root)

print('\n############# data structure ####################')
folder_sizes = []
countFolders(root,100000)
printDirList(root,0)
print ('\nSum of all folders smaler than 100000 = ',sum(folder_sizes))
size_to_free = 30000000 - (70000000 - root[0].dirSize)
print ("Must free up =",size_to_free) #8.876.853
folder_sizes = []
delete_folder(root,size_to_free)
print ("\tsize of folder to delete =",min(folder_sizes))
print("--- %s seconds ---" % (time.time() - start_time))


