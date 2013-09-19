#!/usr/bin/python

import string
import random
from random import choice

# we need to generate CSV data like this:
# ssn,alternate id,health plan,employee ssn,first name,middle name,last name,relationship,zip code,dob,gender,email 1,email 2,eligibility date,organization unit

# Sample PLANS
# BCBSH+, BCHAF, NQ90 are all codes for our 90 Account Plan.
# BCBSMD, BCMDAF, NQ80 are all codes for our 80 Plan.
# BCBSLW, BCLWAF, NQBAS are all codes for our Basic Plan.

# Sample Data:
# 987654321,,BCBSH+,987654322,Billy,A,Jones,EE,20007,1980-10-02,1,,,,NRC
# 123456789,,NONE,123456790,Janet,Q,Riddles,SP,20007,1944-03-09,2,,,,NRC
# 784332210,,BLCWAF,784332211,Bogus,,Utifat,SP,30030,1966-07-09,1,,,,NRC


NUMBER_OF_USERS = 500
OUTPUT_FILE = './user_test_data.csv'

FIRST_NAMES_FILE = './first_names.txt'
LASTNAMES_FILE = './last_names.txt'
DATE_OF_BIRTH = './dates.txt'
PLANS = ['BCBSH+', 'BCHAF', 'NQ90', 'BCBSMD', 'BCMDAF', 'NQ80', 'BCBSLW', 'BCLWAF', 'NQBAS', 'NONE']
RELATIONSHIP = ['EE','EE','EE','SP']
ORGANIZATION_UNIT = ['BCB', 'HAF', 'NQD', 'CSM', 'CMA', 'LLG', 'QDI','DYA', 'USM', 'FEQ', 'JTY', 'IUA', 'QLM', 'YPL', 'BHH']


firstNamesFile = open(FIRST_NAMES_FILE,'r')
lastnamesFile = open(LASTNAMES_FILE,'r')
datesFile = open(DATE_OF_BIRTH,'r')

firstNamesLines = firstNamesFile.readlines()
lastnamesLines = lastnamesFile.readlines()
datesLines = datesFile.readlines()

firstNamesFile.close()
lastnamesFile.close()
datesFile.close()

def getRandomFirstName():
    return choice(firstNamesLines).rstrip()

def getRandomLastName():
    return choice(lastnamesLines).rstrip()

def getRandomSSN():
    return str(random.randint(111111111,999999999))

def getRandomPlan():
    return choice(PLANS)

def getRandomMiddleName():
    return choice(string.ascii_uppercase)

def getRandomRelathioship():
    return choice(RELATIONSHIP)

def getRandomDate():
    return choice(datesLines).rstrip()

def getRandomOU():
    return choice(ORGANIZATION_UNIT)

def getUserData():

    userData = [
        getRandomSSN(),        # ssn
        '',                    # alternate id
        getRandomPlan(),       # health plan
        getRandomSSN(),        # employee ssn
        getRandomFirstName(),  # first name
        choice(string.ascii_uppercase),  # middle name
        getRandomLastName(),     # last name
        getRandomRelathioship(), # relationship
        str(random.randint(11111,22222)), # zip code
        getRandomDate(),  # dob
        str(random.randint(1,2)),  # gender
        '', # email 1
        '', # email 2
        '', # eligibility date
        getRandomOU()# organization unit
    ]

    return userData

def generateData():
    dataHeaders = 'ssn,alternate id,health plan,employee ssn,first name,middle name,last name,relationship,zip code,dob,gender,email 1,email 2,eligibility date,organization unit\n'
    userDataFile = open(OUTPUT_FILE,'w')
    userDataFile.write(dataHeaders)
    for index in range(0,NUMBER_OF_USERS):
        userDataFile.write(",".join(getUserData()) + '\n')
    print "data output file: ", OUTPUT_FILE

generateData()

