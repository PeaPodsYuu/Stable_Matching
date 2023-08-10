from Structure.Clients.User import User
from Structure.Clients.Project import Project
from Structure.Data.Proficiencies import Proficiency, ProficiencyLevel
from Structure.Matching.Matcher import match

if __name__ == '__main__':
    P1 = Project("Cool_Project",
                 [Proficiency.C],
                 2)
    P2 = Project("Py_Proj",
                 [Proficiency.PY],
                 2)

    A = User("Albert",
             {Proficiency.CPP: ProficiencyLevel.Intermediate,
              Proficiency.C: ProficiencyLevel.Advanced,
              Proficiency.OOP: ProficiencyLevel.Beginner,
              Proficiency.PY: ProficiencyLevel.Beginner},
             [P1, P2])

    B = User("Boris",
             {Proficiency.CPP: ProficiencyLevel.Advanced,
              Proficiency.C: ProficiencyLevel.Advanced,
              Proficiency.OOP: ProficiencyLevel.Intermediate,
              Proficiency.PY: ProficiencyLevel.Beginner},
             [P1, P2])

    C = User("Callie",
             {Proficiency.CPP: ProficiencyLevel.Intermediate,
              Proficiency.C: ProficiencyLevel.Beginner,
              Proficiency.OOP: ProficiencyLevel.Advanced,
              Proficiency.PY: ProficiencyLevel.Expert},
             [P2, P1])

    D = User("Dilbert",
             {Proficiency.CPP: ProficiencyLevel.Advanced,
              Proficiency.C: ProficiencyLevel.Advanced,
              Proficiency.OOP: ProficiencyLevel.Advanced,
              Proficiency.PY: ProficiencyLevel.Beginner},
             [P2, P1])

    E = User("Eugene",
             {Proficiency.CPP: ProficiencyLevel.Intermediate,
              Proficiency.C: ProficiencyLevel.Beginner,
              Proficiency.OOP: ProficiencyLevel.Beginner},
             [P1])

    projects_list = [P1, P2]
    waiting_list = [A, B, C, D, E]

    match(waiting_list, projects_list)

    print(f"{P1.get_name()} : {P1.get_users_names()}\n\n")
    print(f"{P2.get_name()} : {P2.get_users_names()}\n\n")
