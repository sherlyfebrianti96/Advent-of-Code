# Read the files for the Input
with open('./Day-07.input.txt') as f:
    bulk = f.read()
    # print(bulk)

# Command for each lines
commands = bulk.split('\n')




# Read each folders
# Arrange each folders and files
# and get the total size of each folders
filesystem = {'totalSize': 0, 'content': []}
activeDirectory = []
for command in commands:
    if ('$ cd' in command):
        # It means it is changing the active directory
        dir = command.replace('$ cd ', '')
        match dir:
            case '/':
                activeDirectory = []
                print('activeDirectory : a', activeDirectory)
            case '..':
                activeDirectory.pop()
                print('activeDirectory : a', activeDirectory)
            case other:
                activeDirectory.append(dir)
                print('activeDirectory : a', activeDirectory)
    elif ('$ ls' in command):
        # It means it is showing list of current active directory
        pass
    elif ('dir ' in command):
        # It means there will be a directory inside this current active directory
        dir = command.replace('dir ', '')
        filesystem = getContents(filesystem, activeDirectory, 'dir', dir)
        print('filesystem : ', filesystem)
    else:
        # It means the reset is the files information with it sizes
        pass
