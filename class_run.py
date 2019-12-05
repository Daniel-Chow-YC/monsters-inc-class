from class_monster import *

name1 = 'Mike Wazowski'
skills1 = ['green', 'one eye', 'round']
monster1 = Monster(name1, skills1)

name2 = 'James P. Sullivan'
skills2 = ['blue', 'big', 'furry']
monster2 = Monster(name2, skills2)

print(monster1.skills)
monster1.add_skills('scary')
print(monster1.skills)

print(monster2.eat('chicken'))
print(monster2.scare_attack())