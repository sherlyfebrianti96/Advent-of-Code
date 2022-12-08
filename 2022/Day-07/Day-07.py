# Read the files for the Input
with open('./Day-07.input.txt') as f:
    bulk = f.read()
    # print(bulk)

# Command for each lines
commands = bulk.split('\n')


def arrangeFolder(fs: dict, activeDirectory: list, newDir: str):
    directories = list(activeDirectory)

    if (len(directories) == 0):
        if (newDir not in fs):
            fs[newDir] = {}
    else:
        currentDir = directories[0]
        return arrangeFolder(fs[currentDir], directories[1:len(directories)], newDir)

    return fs


def arrangeFile(fs: dict, activeDirectory: list, filename: str, filesize: int):
    directories = list(activeDirectory)

    if (len(directories) == 0):
        fs[filename] = filesize
    else:
        currentDir = directories[0]
        return arrangeFile(fs[currentDir], directories[1:len(directories)], filename, filesize)

    return fs


def cleanupFolder(fs: dict, activeDirectory: list):
    directories = list(activeDirectory)

    if (len(activeDirectory) == 0):
        for item in list(fs):
            if (isinstance(fs[item], int)):
                del fs[item]

    else:
        currentDir = directories[0]
        directories.pop(0)
        if (fs[currentDir]):
            return cleanupFolder(fs[currentDir], directories)

    return fs


filesystem = {}

# Read each folders
# Arrange each folders and files
# and get the total size of each folders
activeDirectory = []
for command in commands:
    if ('$ cd' in command):
        # It means it is changing the active directory
        dir = command.replace('$ cd ', '')

        match dir:
            case '/':
                activeDirectory = []
                pass
            case '..':
                activeDirectory.pop()
            case other:
                activeDirectory.append(dir)

        print('\nactiveDirectory : ', activeDirectory)

    elif ('$ ls' in command):
        # It means it is showing list of current active directory
        pass

    elif ('dir ' in command):
        # It means there will be a directory inside this current active directory
        dir = command.replace('dir ', '')

        arrangeFolder(filesystem, activeDirectory, dir)

    else:
        # It means the reset is the files information with it sizes
        fileData = command.split(' ')

        arrangeFile(filesystem, activeDirectory,
                    fileData[1], int(fileData[0]))


print('filesystem : ', filesystem)
