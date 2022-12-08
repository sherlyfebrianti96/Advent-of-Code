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


def totalSize(fs: dict, total: int, arrayOfTotalSizes: list):
    for itemKey in list(fs):
        item = fs[itemKey]
        if (isinstance(item, dict)):
            # this is the folder
            # print('folder', itemKey, item)
            total += totalSize(item, 0, arrayOfTotalSizes)
        else:
            # This is the file
            # print('item', itemKey, item)
            total += item

    print('total', total, '\n')
    arrayOfTotalSizes.append(total)
    return total


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

print('\n============\n')
totalSizesOfFolderThatHasLessThan100000 = 0
arrayOfTotalSizes = []
print(totalSize(filesystem.copy(), totalSizesOfFolderThatHasLessThan100000, arrayOfTotalSizes))

print('\n============\n')
print('arrayOfTotalSizes : ', arrayOfTotalSizes)
print('\n============\n')

part1 = [size for size in arrayOfTotalSizes if size <= 100000]
print("Answer for Part 1 : ", sum(part1))
