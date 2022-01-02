#
# The School
# Author: Taylor Bell
# 2022.01.01
#


# imports
from faker import Faker
import names
import time
import random
import numpy


# constants
CURRENT_VERSION = 0.01

# range values
credits_range = {'min': 0, 'max': 120, 'step': 1}
age_range = {'min': 18, 'max': 40, 'step': 1}



class Student:
    def __init__(self, name, age, total_credits):
        self.name = name
        self.age = age
        self.total_credits = total_credits


class Professor:
    def __init__(self, name, age, office_location, classes):
        self.name = name
        self.age = age
        self.office_location = office_location
        self.classes = classes


class Course:
    def __init__(self, course_title, credits, course_location):
        self.course_title = course_title
        self.credits = credits
        self.course_location = course_location


def generateStudent():
    student_name = names.get_full_name()

    student_age = round(
        random.choice(
            numpy.arange(
                credits_range['min'],
                credits_range['max'],
                credits_range['step']
            )
        )
    )

    student_credits = round(
        random.choice(
            numpy.arange(
                age_range['min'],
                age_range['max'],
                age_range['step']
            )
        )
    )

    return {
        'student_name': student_name,
        'student_age': student_age,
        'student_credits': student_credits
    }


def generateProfessor():
    prof_name = names.get_full_name()
    return prof_name

def run():

    # print title and version
    print("The School " + str(CURRENT_VERSION))

    # instantiate faker object
    fake = Faker()

    # instantiate students
    newStudent = Student("Taylor", 26, 120)

    # instantiate professors
    prof1 = Professor("Thomas Atchison", 65, "Main Hall 350", [1, 2, 3])
    prof2 = generateProfessor()

    # accessing information
    print(newStudent.name)

    # chance prof1 office location
    prof1.office_location = "Regency Hall 211"
    print(prof1.office_location)

    print(prof2)

if __name__ == '__main__':
    run()

