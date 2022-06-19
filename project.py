import math
from contributor import Contributor

class Project:
    def __init__(self, name, duration, score, best_before, roles, levels, initial_contributor_list):
        self.name = name
        self.duration = duration
        self.score = score
        self.best_before = best_before
        self.roles = roles
        self.rolesLength = len(roles)
        self.levels = levels 
        self.assignment = [] 
        self.difficulty = self.calc_difficulty(initial_contributor_list)

    def does_not_have_point(self, current_day):
        return current_day + self.duration > self.best_before + self.score

    def productivity(self, current_day):
        # print(self.score)
        # print(self.difficulty)
        # print(self.duration)
        # print(self.rolesLength)
        # print(self.best_before)
        # print(current_day)
        # print(" ")
        try:
            return self.score / (self.difficulty * self.duration * self.rolesLength * (self.best_before - current_day + 1))
        except ZeroDivisionError:
            return math.inf

    def calc_difficulty(self, initial_contributor_list):
        n = 0
        for i in range (0, len(self.roles)):
            for contributor in initial_contributor_list:
                if contributor.skills.get(self.roles[i], -1) >= self.levels[i]:
                    n += 1
        return n

    def canDo(self, contributors):
        roleDict = {}
        for i, role in enumerate(self.roles):
            cando = []
            candomentee = []
            for con in contributors:
                keys = con.skills.keys()
                if (role in keys):
                    if (con.skills[role] >= self.levels[i]):
                      cando.append(con)
                    elif (con.skills[role] == (self.levels[i] - 1)):
                        candomentee.append(con)
                else:
                    if (self.levels[i] == 1):
                        candomentee.append(con)
            roleDict[role] = (cando, candomentee)
    
        return roleDict

    def assign (self, contributors):
        assignment = []
        roleDict = self.canDo(contributors)
        for i, role in enumerate(self.roles):
            cando = sorted(roleDict[role][0], key = lambda contributor : contributor.utilisation_by_project(self), reverse=True)
            candomentee = roleDict[role][1]
            if (candomentee):
                for candidate in candomentee:
                    if self.alreadythere(assignment, cando):
                        if (candomentee not in assignment):
                            assignment.append(candidate) 
                            break     
            elif (cando):
                for candidate in cando:
                    if candidate not in assignment:
                        assignment.append(candidate)
                        break
                else:
                    return []
            else: 
                return []
        self.assignment = assignment

    
    def alreadythere(self, assignment, cando):
        for con in assignment:
            if (con in cando):
                return True
        return False


