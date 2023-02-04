from collections import namedtuple
import requests

Course = namedtuple("Course", "sectionType, sectionNum units instructor days time building final status")
schedule = {}
courseDict = {}

def getClassInfo():
    userInput = input().split()
    department = userInput[0]
    courseNumber = userInput[1]
    term = userInput[2]
    year = userInput[3]

    response = requests.get("https://api.peterportal.org/rest/v0/schedule/soc?term={}%20{}&department={}&courseNumber={}".format(year, term, department, courseNumber)).json()

    sections = response["schools"][0]["departments"][0]["courses"][0]["sections"]
    courses = response["schools"][0]["departments"][0]["courses"][0]

    name = courses["courseTitle"]
    num = courses["courseNumber"]
    dept = courses["deptCode"]

    courseDict.clear()
    
    print("{} {} - {}".format(dept, num, name))
    print()

    for i in range(len(sections)):
        printInfo(sections, i, courseDict)    
 
    x = input("Enter a course code: ")
    printCourse(x, courseDict[x])

def printCourse(sectionCode, course):
    print("Course Code: {}".format(sectionCode))
    print("Section: {} {}".format(course.sectionType, course.sectionNum))
    print("Units: {}".format(course.units))
    print("Instructor: {}".format(course.instructor))
    print("Days: {}".format(course.days))
    print("Time: {}".format(course.time))
    print("Building: {}".format(course.building))

    if course.sectionType == "Lec":
        print("Final Exam: {}".format(c.final))

    print("Status: {}".format(course.status))
    print()

def printInfo(sections, i, courseDict):
    sectionCode = sections[i]["sectionCode"]
    sectionType = sections[i]["sectionType"]
    sectionNum = sections[i]["sectionNum"]
    units = sections[i]["units"]
    instructor = sections[i]["instructors"][0]
    days = sections[i]["meetings"][0]["days"] 
    time = sections[i]["meetings"][0]["time"]
    building = sections[i]["meetings"][0]["bldg"]
    final = sections[i]["finalExam"]
    status = sections[i]["status"]
    
    c = Course(sectionType, sectionNum, units, instructor, days, time, building, final, status)
    result = ""

    result += "Course Code: {}".format(sectionCode)
    result += "Section: {} {}".format(c.sectionType, c.sectionNum)
    result += "Units: {}".format(c.units)
    result += "Instructor: {}".format(c.instructor)
    result += "Days: {}".format(c.days)
    result += "Time: {}".format(c.time)
    result += "Building: {}".format(c.building)

    print("Course Code: {}".format(sectionCode))
    print("Section: {} {}".format(c.sectionType, c.sectionNum))
    print("Units: {}".format(c.units))
    print("Instructor: {}".format(c.instructor))
    print("Days: {}".format(c.days))
    print("Time: {}".format(c.time))
    print("Building: {}".format(c.building))

    if c.sectionType == "Lec":
        print("Final Exam: {}".format(c.final))

    print("Status: {}".format(c.status))
    print()

    courseDict[sectionCode] = c

def addClass(sectionCode):
    for i in range(len(schedule)):
        

    schedule[sectionCode] = courseDict[sectionCode]
    

getClassInfo()

#serInput2 = input()
#if userInput2 == sectionCode:
    # print("Course Code: {}".format(sectionCode))
    # print("Section: {} {}".format(sectionType, sectionNum))
    # print("Units: {}".format(units))
    # print("Instructor: {}".format(instructor))
    # print("Days: {}".format(days))
    # print("Time: {}".format(time))
    # print("Building: {}".format(building))
    # if sectionType != "Dis":
    #     print("Final Exam: {}".format(final))
    # print("Status: {}".format(status))
    # print()