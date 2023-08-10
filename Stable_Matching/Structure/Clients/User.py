from Structure.Data.Proficiencies import Proficiency, ProficiencyLevel


class User:
    def __init__(self, name: str,
                 proficiencies: {Proficiency: ProficiencyLevel},
                 desired_projects):
        self.name = name
        self.proficiencies = proficiencies
        self.desired_projects = desired_projects
        self.in_projects = []

    def add_user_to_project(self, project):
        self.in_projects.append(project)

    def get_name(self):
        return self.name

    def get_proficiencies(self):
        return self.proficiencies

    def get_desired_projects(self):
        return self.desired_projects

    def get_in_projects(self):
        return self.in_projects