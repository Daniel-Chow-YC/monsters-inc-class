class Monster():

    def __init__(self, name, skills):
        self.name = name
        self.skills = []

    def sleep(self):
        return 'zzzzzzzz...'

    def eat(self, food):
        return f"Nom, nom {food} is good."

    def scare_attack(self):
        return "RAAAHHHH (╯°□°)╯"

    def add_skills(self, skills):
        self.skills.append(skills)

