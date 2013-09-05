#!/usr/bin/python


class ExercisesCatalog:
    def __init__(self, params):
        self.ExercisesObject = params['ExerciseObject']

    def start(self):
        self.printMenu()
        exerciseIndex = raw_input("Please write an exercise number and pres enter: ")

        if exerciseIndex:
            exerciseIndex = int(exerciseIndex)

            if exerciseIndex and exerciseIndex != 0:
                selectedExercise = self.getSelectedExercise(exerciseIndex)
                if selectedExercise:
                    self.executeProgram(self.getSelectedExercise(exerciseIndex))
                else:
                    self.printError("wrong exercise number!!")

                self.start()
        else:
            self.printError("you need to select one exercise!!")
            self.start()
        return

    def printMenu(self):
        print "----------------------------------------------------"
        print "Welcome to the learn python the hard way excercises!"
        print "we have ", self.ExercisesObject.totalNumber(), " exercises available:"
        print "----------------------------------------------------"
        self.listExercises()
        print "----------------------------------------------------"
        print "PRESS 0 TO CLOSE"

    def printError(self, message):
        print "\n"
        print "===== ERROR ====="
        print message
        print "\n ... press enter to continue ..."
        raw_input()

    def executeProgram(self, exercise):
        print "\n\n"
        print "............................."
        print "Executing: " + exercise['name']
        print "............................."
        exercise['instance'].run()
        print "............................."
        print "\n\n"

    def listExercises(self):
        allExercises = self.ExercisesObject.getExercises()
        for index in range(len(allExercises)):
            print (index+1), ".-", allExercises[index]['name']
        return

    def getSelectedExercise(self,exerciseIndex):
        exerciseIndex = exerciseIndex - 1
        allExercises = self.ExercisesObject.getExercises()
        for index in range(len(allExercises)):
            if index == exerciseIndex:
                return allExercises[index]

class Exercises:
    def __init__(self, params):
        self.exercises = []

        for exercise in params['exercises']:
            self.add(exercise)

    def add(self,exercise):
        if exercise and exercise['name'] and exercise['instance']:
            self.exercises.append(exercise)
        else:
            print "every exercise must have 'name' and 'instance' attributes"

    def totalNumber(self):
        return len(self.exercises)

    def getExercises(self):
        return list(self.exercises)

# --------------------
# Exercises
# --------------------

class PercentageCalculator:
    def run(self):
        print "Numbers and Math"
        print "Now we will execute percentage calculator"
        number = float(raw_input("please insert a number and press enter: "))
        percentage = float(raw_input("please insert a percentage and press enter: "))
        resultValue = number * (percentage / 100)
        print "Result: ", resultValue
        raw_input("\n ... press enter to finish ...")

class CustomizedHelloWorld:
    def run(self):
        print "Welcome Stranger!"
        name = raw_input("Can you please insert your name and press enter: ")
        print "Thanks!, Now, you're not an stranger"
        print "\n Welcome " + name + "!!"
        raw_input("\n ... press enter to finish ...")

# --------------------
# Index
# --------------------

exercises = [{
    'name': "Simple Percentage Calculator",
    'instance': PercentageCalculator()
},
{
    'name': "Customized Hello World",
    'instance': CustomizedHelloWorld()
}]


ExerciseObject = Exercises({'exercises' : exercises})
MyCatalog = ExercisesCatalog({'ExerciseObject': ExerciseObject})
MyCatalog.start()

