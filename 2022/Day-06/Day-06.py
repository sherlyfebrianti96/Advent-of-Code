# Read the files for the Input
with open('./Day-06.input.txt') as f:
    bulk = f.read()
    # print(bulk)

# The input will be only 1 line of text
# Separate each character of that line
packet = list(bulk)

numberOfCharactersInSequence = 4

firstMarker = 0

# On every 4 characters received, check if they are the right sequence
index = 0
while (len(packet) - numberOfCharactersInSequence):
    # Check if the current N character is unique
    currentChars = packet[index:index+numberOfCharactersInSequence]
    uniqueChars = set(currentChars)

    print('\nindex : ', index)
    print('currentChars : ', currentChars)
    print('len(currentChars) : ', len(currentChars))
    print('uniqueChars : ', uniqueChars)
    print('len(uniqueChars) : ', len(uniqueChars))

    # Get first packet's sequence
    if (len(currentChars) == len(uniqueChars)):
        firstMarker = index + numberOfCharactersInSequence
        break

    index += 1

print('\n============\n')
print('firstMarker : ', firstMarker)
# print('firstSequenceCharacters : ', firstSequenceCharacters)
# print('firstPacketSequence after character : ', firstNextPacketSequence)
