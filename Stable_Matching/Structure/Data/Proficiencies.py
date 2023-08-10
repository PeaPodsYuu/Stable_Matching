from enum import Enum


class Proficiency(Enum):
    JAVA = "Java"
    PY = "Python"
    CPP = "C++"
    C = "C"
    OOP = "Object Oriented Programming"


class ProficiencyLevel(Enum):
    Beginner = 1
    Intermediate = 4
    Advanced = 7
    Expert = 10


def get_closest_proficiency(wanted_proficiencies: [Proficiency], got_proficiency: {Proficiency, ProficiencyLevel}):
    value = 0
    for wanted_proficiency in wanted_proficiencies:
        match wanted_proficiency:
    
            case Proficiency.CPP:
                if got_proficiency[0] == Proficiency.CPP:
                    value += 10 * got_proficiency[1].value
                elif got_proficiency[0] == Proficiency.C:
                    value += 5 * got_proficiency[1].value
                elif got_proficiency[0] == Proficiency.JAVA:
                    value += 2 * got_proficiency[1].value
                elif got_proficiency[0] == Proficiency.OOP:
                    value += 2 * got_proficiency[1].value
                else:
                    value += 0

            case Proficiency.C:
                if got_proficiency[0] == Proficiency.C:
                    value += 10 * got_proficiency[1].value
                elif got_proficiency[0] == Proficiency.CPP:
                    value += 5 * got_proficiency[1].value
                else:
                    value += 0

            case Proficiency.JAVA:
                if got_proficiency[0] == Proficiency.JAVA:
                    value += 10 * got_proficiency[1].value
                elif got_proficiency[0] == Proficiency.CPP:
                    value += 5 * got_proficiency[1].value
                elif got_proficiency[0] == Proficiency.C:
                    value += 2 * got_proficiency[1].value
                elif got_proficiency[0] == Proficiency.OOP:
                    value += 5 * got_proficiency[1].value
                elif got_proficiency[0] == Proficiency.PY:
                    value += 2 * got_proficiency[1].value
                else:
                    value += 0

            case Proficiency.PY:
                if got_proficiency[0] == Proficiency.PY:
                    value += 10 * got_proficiency[1].value
                elif got_proficiency[0] == Proficiency.OOP:
                    value += 5 * got_proficiency[1].value
                elif got_proficiency[0] == Proficiency.JAVA:
                    value += 3 * got_proficiency[1].value
                else:
                    value += 0

            case Proficiency.OOP:
                if got_proficiency[0] == Proficiency.OOP:
                    value += 10 * got_proficiency[1].value
                elif got_proficiency[0] == Proficiency.CPP:
                    value += 5 * got_proficiency[1].value
                elif got_proficiency[0] == Proficiency.JAVA:
                    value += 7 * got_proficiency[1].value
                elif got_proficiency[0] == Proficiency.PY:
                    value += 4 * got_proficiency[1].value
                else:
                    value += 0
    return value
