from random import *


class Class():
  def __init__(self, name, sl, stat):
    self.__name = name
    self.__sl = sl
    self.__stat = stat
    
  def getName(self):
    return self.__name
  
  def getLevel(self):
    return self.__sl

  def getStats(self):
    return self.__stat
  
  def changeLevel(self, newsl):
    self.__sl = newsl
  
  def changeStats(self, newstat):
    self.__stat = newstat
  

def randomClass(list, m):
  randClass = list[randint(0, len(list)-1)]
  stats = randClass.getStats()
  newstats = []
  newsl = randClass.getLevel()
  for i in range(5):
    newstats.append(randint(stats[i], 40))
    newsl += newstats[i] - stats[i]
  newstats.append(stats[5])
  if m==1:
    newstats.append(randint(stats[6], 60))
    newstats.append(stats[7])
  elif m==2:
    newstats.append(stats[6])
    newstats.append(randint(stats[7], 40))
  else:
    newstats.append(stats[6])
    newstats.append(stats[7])
  randClass.changeLevel(newsl)
  randClass.changeStats(newstats)
  return randClass


def RandomBuild():
  Warrior = Class('Warrior', 4, [11, 8, 12, 13, 13, 11, 9, 9])
  Knight = Class('Knight', 5, [14, 10, 10, 11, 11, 10, 9, 11])
  Wanderer = Class('Wanderer', 3, [10, 11, 10, 10, 14, 12, 11, 8])
  Thief = Class('Thief', 5, [9, 11, 9, 9, 15, 10, 12, 11])
  Bandit = Class('Bandit', 4, [12, 8, 14, 14, 9, 11, 8, 10])
  Hunter = Class('Hunter', 4, [11, 9, 11, 12, 14, 11, 9, 9])
  Sorcerer = Class('Sorcerer', 3, [8, 15, 8, 9, 11, 8, 15, 8])
  Pyromancer = Class('Pyromancer', 1, [10, 12, 11, 12, 9, 12, 10, 8])
  Cleric = Class('Cleric', 2, [11, 11, 9, 12, 8, 11, 8, 14])
  Deprived = Class('Deprived', 6, [11, 11, 11, 11, 11, 11, 11, 11])
  classes = [Warrior, Knight, Wanderer, Thief, Bandit, Hunter, Sorcerer, Pyromancer, Cleric, Deprived]

  RH = open('rhds1.txt', 'r')
  RH = RH.readlines()
  RH = RH[randint(0, len(RH)-1)]
  LH = open('lhds1.txt', 'r')
  LH = LH.readlines()
  LH = LH[randint(0, len(LH)-1)]
  magic = randint(1, 3)

  randClass = randomClass(classes, magic)

  print('Class: ', randClass.getName())
  print('Level: ', randClass.getLevel())
  print('Stats: ', randClass.getStats())
  print('Right Hand:', RH, end='')
  print('Left Hand:', LH, end='')
  print('Magic: ', end='')
  if magic==1:
    print('Sorceries')
  elif magic==2:
    print('Miracles')
  else:
    print('Pyromancies')
  

if __name__ == '__main__':
  RandomBuild()