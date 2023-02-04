import requests

def printInfo(sections, i):
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
    
    if sectionType == "Lec":
        courseDict[sectionNum] = []
    else:
        courseDict[sectionNum[0]].append([sectionCode, sectionNum])

    print("Course Code: {}".format(sectionCode))
    print("Section: {} {}".format(sectionType, sectionNum))
    print("Units: {}".format(units))
    print("Instructor: {}".format(instructor))
    print("Days: {}".format(days))
    print("Time: {}".format(time))
    print("Building: {}".format(building))
    if sectionType != "Dis":
        print("Final Exam: {}".format(final))
    print("Status: {}".format(status))
    print()

def main():
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

    courseDict = {}

    print("{} {} - {}".format(dept, num, name))
    print()

for i in range(len(sections)):
    #printInfo(sections)

    """ sectionCode = sections[i]["sectionCode"]
    sectionType = sections[i]["sectionType"]
    sectionNum = sections[i]["sectionNum"]
    units = sections[i]["units"]
    instructor = sections[i]["instructors"][0]
    days = sections[i]["meetings"][0]["days"] 
    time = sections[i]["meetings"][0]["time"]
    building = sections[i]["meetings"][0]["bldg"]
    final = sections[i]["finalExam"]
    maxCapacity = sections[i]["maxCapacity"]
    status = sections[i]["status"]
    totalEnrolled = sections[i]["numCurrentlyEnrolled"]["totalEnrolled"]
    
    if sectionType == "Lec":
        courseDict[sectionNum] = []
    else:
        courseDict[sectionNum[0]].append([sectionCode, sectionNum])

    print("Course Code: {}".format(sectionCode))
    print("Section: {} {}".format(sectionType, sectionNum))
    print("Units: {}".format(units))
    print("Instructor: {}".format(instructor))
    print("Days: {}".format(days))
    print("Time: {}".format(time))
    print("Building: {}".format(building))
    if sectionType != "Dis":
        print("Final Exam: {}".format(final))
    print("Status: {}".format(status))
    print() """
print(courseDict)

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