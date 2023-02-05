from collections import namedtuple
import requests

Course = namedtuple("Course", "sectionType, sectionNum units instructor days time building final status start end")
Time = namedtuple("Time", "hour minute")
schedule = {}
courseDict = {}

def getTermInfo():
    response = requests.get("https://api.peterportal.org/rest/v0/courses/all").json()
    res = []
    for i in range(len(response)):
        if not(response[i]["department"] in res):
            res.append(response[i]["department"])
    return res
    
def getCourseNum(userInput):
    result = set()
    print(userInput)
    department = userInput['department']
    temp = userInput['term'].split()

    if department == "I&C SCI":
        department = "I%26C SCI"
    elif department == "CLT&THY":
        department = "CLT%26THY"
    elif department == "FLM&MDA":
        department = "FLM%26MDA"
    elif department == "GEN&SEX":
        department = "GEN%26SEX"
    elif department == "M&MG":
        department = "M%26MG"
    elif department == "CHC/LAT":
        department = "CHC%2FLAt"
    elif department == "CRM/LAW":
        department = "CRM%2FLAW"                

    quarter = temp[0]
    year = temp[1]
    response = requests.get("https://api.peterportal.org/rest/v0/schedule/soc?term={}%20{}&department={}".format(year, quarter, department)).json()

    for i in range(len(response["schools"][0]["departments"][0]["courses"])):
        result.add(response["schools"][0]["departments"][0]["courses"][i]["courseNumber"])

    return list(result)


    print(res)
    
        #else:
         #   res[response[i]["department"]].append(response[i]["number"])
    
    #print(res)
   

    
    #responseW22 = requests.get("https://api.peterportal.org/rest/v0/schedule/soc?term=2022%20Winter&department=MATH").json() 
    #responseS22 = requests.get("https://api.peterportal.org/rest/v0/schedule/soc?term=2022%20Spring").json()
    #responseF22 = requests.get("https://api.peterportal.org/rest/v0/schedule/soc?term=2022%20Fall").json()
    #responseW23 = requests.get("https://api.peterportal.org/rest/v0/schedule/soc?term=2023%20Winter").json()
    print(len(res))
    for j in range(len(res)):
        responseW22 = requests.get("https://api.peterportal.org/rest/v0/schedule/soc?term=2022%20Winter&department={}".format(res[j])).json() 
        #responseS22 = requests.get("https://api.peterportal.org/rest/v0/schedule/soc?term=2022%20Spring&department={}".format(res[j])).json()
        #responseF22 = requests.get("https://api.peterportal.org/rest/v0/schedule/soc?term=2022%20Fall&department={}".format(res[j])).json()
        #responseW23 = requests.get("https://api.peterportal.org/rest/v0/schedule/soc?term=2023%20Winter&department={}".format(res[j])).json()

        print(responseW22)
        return
        try:
            if len(responseW22["schools"][0]["departments"]) != 0:
                for m in range(len(responseW22["schools"][0]["departments"][0]["courses"])):
                    if not(res[j] in result["Winter 2022"]):
                        result["Winter 2022"][res[j]] = []

                    if not(responseW22["schools"][0]["departments"][0]["courses"][m]["courseNumber"] in result["Winter 2022"][res[j]]):
                        result["Winter 2022"][res[j]].append(responseW22["schools"][0]["departments"][0]["courses"][m]["courseNumber"])
        except:
            print(res[j])
            print()

        #result["Winter 2022"][res[j]] = responseW22["schools"][0]["departments"][0]["courses"]
        #result["Spring 2022"][res[j]] = responseS22["schools"][0]["departments"][0]["courses"]
        #result["Fall 2022"][res[j]] = responseF22["schools"][0]["departments"][0]["courses"]
        #result["Winter 2023"][res[j]] = responseW23["schools"][0]["departments"][0]["courses"]

    print(result)
    return

    

    print(responseW22)
    return

    result["Winter 2022"]["Departments"] = responseW22["schools"][0]["departments"]
    result["Spring 2022"]["Departments"] = responseS22["schools"][0]["departments"]
    result["Fall 2022"]["Departments"] = responseF22["schools"][0]["departments"]
    result["Winter 2023"]["Departments"] = responseW23["schools"][0]["departments"]

    result["Winter 2022"]["Courses"] = responseW22["schools"][0]["courses"]
    result["Spring 2022"]["Courses"] = responseS22["schools"][0]["courses"]
    result["Fall 2022"]["Courses"] = responseF22["schools"][0]["courses"]
    result["Winter 2023"]["Courses"] = responseW23["schools"][0]["courses"]

    return result



def getClassInfo(department, courseNumber, term, year):
    #userInput = input().split()
    #department = userInput[0]
    #courseNumber = userInput[1]
    #term = userInput[2]
    #year = userInput[3]

    if department == "I&C SCI":
        department = "I%26C SCI"
    elif department == "CRM/LAW":
        department = "CRM%2FLAW"

    response = requests.get("https://api.peterportal.org/rest/v0/schedule/soc?term={}%20{}&department={}&courseNumber={}".format(year, term, department, courseNumber)).json()

    sections = response["schools"][0]["departments"][0]["courses"][0]["sections"]
    courses = response["schools"][0]["departments"][0]["courses"][0]

    name = courses["courseTitle"]
    num = courses["courseNumber"]
    dept = courses["deptCode"]

    courseDict.clear()
    result = "{} {} - {}\n".format(dept, num, name)

    for i in range(len(sections)):
        result += getSection(sections, i, courseDict)    
 
    return result

def getCourse(sectionCode, course):
    for c in schedule.values():
        if not checkTime(course.start, course.end, c.start, c.end):
            return ""

    result = ""

    result += "Course Code: {}\n".format(sectionCode)
    result += "Section: {} {}\n".format(course.sectionType, course.sectionNum)
    result += "Units: {}\n".format(course.units)
    result += "Instructor: {}\n".format(course.instructor)
    result += "Days: {}\n".format(course.days)
    result += "Time: {}\n".format(course.time)
    result += "Building: {}\n".format(course.building)

    if course.sectionType == "Lec":
        result += "Final Exam: {}\n".format(course.final)
        
    result += "Status: {}\n\n".format(course.status)

    return result

def getSection(sections, i, courseDict):
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
    
    if time[-1] == "p" or "{}{}".format(time[-2], time[-1]) == "pm":
        startHour = int("{}{}".format(time[0], time[1]))
        startMinute = int("{}{}".format(time[3], time[4]))
        
        if time[-1] == "p":
            endHour = int("{}{}".format(time[-6], time[-5])) + 12
            endMinute = int("{}{}".format(time[-3], time[-2]))
        else:
            endHour = int("{}{}".format(time[-7], time[-6])) + 12
            endMinute = int("{}{}".format(time[-4], time[-3]))
        
        if endHour - 12 >= 3:
            startHour += 12
        else:
            if not(10 <= startHour <= 12):
                startHour += 12

        if startHour == 24:
            startHour = 12

        if endHour == 24:
            endHour = 12

        start = round(startHour + (startMinute / 60), 2)
        end = round(endHour + (endMinute / 60), 2)
    else:
        startHour = int("{}{}".format(time[0], time[1]))
        startMinute = int("{}{}".format(time[3], time[4]))
        start = round(startHour + (startMinute / 60), 2)

        if time[-1] == "m":
            endHour = int("{}{}".format(time[-7], time[-6]))
            endMinute = int("{}{}".format(time[-4], time[-3]))
        else:
            endHour = int("{}{}".format(time[-6], time[-5]))
            endMinute = int("{}{}".format(time[-3], time[-2]))
        
        end = round(endHour + (endMinute / 60), 2)

    c = Course(sectionType, sectionNum, units, instructor, days, time, building, final, status, start, end)
    courseDict[sectionCode] = c

    return getCourse(sectionCode, c)
    
def addClass(sectionCode):
    schedule[sectionCode] = courseDict[sectionCode]

def checkTime(start1, end1, start2, end2):
    # Time 1 is what we WANT to add... time 2 is already in schedule
    return not(start2 <= start1 <= end2 or start2 <= end1 <= end2)

def sortByInstructor():
    return sorted()

#print(addClass(1))
#print(getCourseNum("MATH", "Winter 2023"))

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