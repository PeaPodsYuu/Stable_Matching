from Structure.Clients.User import User
from Structure.Clients.Project import Project
from Structure.Data.Proficiencies import get_closest_proficiency


def match(users: [User], projects: [Project]):
    for project in projects:
        desirability = {}
        for user in users:
            if project in user.get_desired_projects():
                a = []
                desirability[user] = -30 * len(user.get_in_projects())

        desired_proficiencies = project.get_proficiencies()

        for user, value in desirability.items():
            proficiencies = user.get_proficiencies()
            for proficiency, val in proficiencies.items():
                desirability[user] += get_closest_proficiency(desired_proficiencies, [proficiency, val])

        desirability = sorted(desirability.items(), key=lambda x: x[1], reverse=True)

        while project.get_wanted_users() > 0:
            print(f"\n{desirability[0][0].get_name()} : {desirability[0][1]}\n")
            project.add_user(desirability[0][0])
            desirability.pop(0)
