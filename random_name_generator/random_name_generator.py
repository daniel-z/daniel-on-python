#! /usr/bin/python

'''
Random Name Generator
'''

LIST_OF_FULL_NAMES = './full_names.txt'
LIST_OF_FIRST_NAMES = './first_names.txt'
LIST_OF_LAST_NAMES = './last_names.txt'

class firstTimeLoad:
    '''
    This was used to load names and generate the lists from first time
    not needed any more but as sample
    '''
    # load file
    fullNamesFile = open(LIST_OF_FULL_NAMES, 'r')

    print "READING FULL NAMES ..."
    firstNames = []
    lastNames = []

    for line in fullNamesFile:
        (firstName, lastName) = line.split()
        firstNames.append(firstName)
        lastNames.append(lastName)

    fullNamesFile.close()

    fullNamesFile = open(LIST_OF_FULL_NAMES, 'w')
    firstNamesFile = open(LIST_OF_FIRST_NAMES, 'w')
    lastnamesFile = open(LIST_OF_LAST_NAMES, 'w')

    for index, name in enumerate(firstNames):
        fullNamesFile.write(name+','+lastNames[index]+'\n');
        firstNamesFile.write(name+'\n');
        lastnamesFile.write(lastNames[index]+'\n');

    fullNamesFile.close()
    firstNamesFile.close()
    lastnamesFile.close()


# get parameters
    # how much names? default 1000

#for index in
# execute cicle
    #get randomname
    #get randomlastname
    # mix and write on file
        # separated by [,]
        # output filename csv

# get randome number (maximum)
    # min 0 max number in list (actual is 300, but get it from last number in array)

# get random name
    #index = get randome number (max in names)

# get random lastname ()
    #index = get randome number (max in lastnames)


