from class_monster import *
# Setup
name = 'Paul'
skills = ['scary', 'hairy', 'loud']
monster1 = Monster(name, skills)

# Testing scare_attack()

print('checking if monster can scare_attack properly')
print(monster1.scare_attack() == 'RAAAHHHH (╯°□°)╯')