class Contributor:
  def __init__(self, name, skills):
    self.name = name
    self.skills = skills
    self.totalSkill = sum(skills.values())
  
  def utilisation_by_project(self, project):
    numerator = sum(self.skills[skill_name] for skill_name in self.skills if skill_name in set(project.roles))
    denominator = self.totalSkill
    return numerator / denominator
