
from input import *
from collections import defaultdict

contributors = set(contributors)
projects = set(projects)
executed_projects = set()

num_executed = 0
current_day = 0
to_break = False
day_to_project_finish = defaultdict(list)
while not to_break:
    completed_projects = day_to_project_finish[current_day - 1]
    for completed_project in completed_projects:
        for contributor_freed in completed_project.assignment:
            contributors.add(contributor_freed)

    sorted_by_productivity = sorted(projects, key = lambda project : project.productivity(current_day), reverse=True)
    projs_counted = 0
    for project in sorted_by_productivity:
        if (not contributors) or (projs_counted == 100):
            break

        project.assign(contributors)
        project_assignment = project.assignment
        if len(project_assignment) > 0:
            # Do this project
            executed_projects.add(project)
            num_executed += 1
            projects.discard(project)
            day_to_project_finish[current_day + project.duration - 1].append(project)
            for assigned_contributor in project.assignment:
                contributors.add(assigned_contributor)

        projs_counted += 1


    current_day += 1
    to_break = True
    for project in projects:
        project_last_day = project.best_before + project.score
        if project_last_day < current_day:
            to_break = False
    
print(num_executed)
for executed_proj in executed_projects:
    print(executed_proj.name)
    print(" ".join(contributor.name for contributor in executed_proj.assignment))