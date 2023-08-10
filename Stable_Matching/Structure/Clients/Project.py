class Project:
    def __init__(self, name: str,
                 proficiencies,
                 wanted_users: int):
        self.name = name
        self.proficiencies = proficiencies
        self.wanted_users = wanted_users
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        self.wanted_users -= 1
        user.add_user_to_project(self)

    def get_name(self):
        return self.name

    def get_proficiencies(self):
        return self.proficiencies

    def get_wanted_users(self):
        return self.wanted_users
    
    def get_users(self):
        return self.users

    def get_users_names(self):
        users = []
        for user in self.users:
            users.append(user.get_name())
        return users