from contributor import Contributor
from project import Project

filename = "b_better_start_small.in.txt"
f = open(filename, "r+")
 
nums = f.readline().split(" ")
numContributors = int(nums[0])
numProjects = int(nums[1])

contributors = []
projects = []

for i in range(0, numContributors):
    myline = f.readline()
    splitLine = myline.split(" ")
    name = splitLine[0] 
    numSkills = int(splitLine[1])
    skills = {} 
    for j in range(0, numSkills):
        myline = f.readline()
        splitLine = myline.split(" ")
        k, v = splitLine[0], int(splitLine[1])
        skills[k] = v
    c = Contributor(name, skills)
    contributors.append(c)
        

for i in range(0, numProjects):
    myline = f.readline()
    splitLine = myline.split(" ")
    name = splitLine[0] 
    duration = int(splitLine[1])
    score = int(splitLine[2])
    bestbefore = int(splitLine[3])
    numRoles = int(splitLine[4])
    roles = []
    levels = []
    for j in range(0, numRoles):
        myline = f.readline()
        splitLine = myline.split(" ")
        k, v = splitLine[0], int(splitLine[1])
        roles.append(k)
        levels.append(v)
    p = Project(name, duration, score, bestbefore, roles, levels, contributors)
    projects.append(p)
