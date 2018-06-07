import pygame
import sys
pygame.init()
import time

Lives = 3
Answered = 0
Levels = 0
Score = Answered + Lives + Levels

print ('Welcome brave traveller, so you think you have what is takes to solve my riddles?')
time.sleep(4)
print ('Im sure you already know the rules of my infamous game...')
time.sleep(4)
print ('But I will repeat them out of the kindness in my heart')
time.sleep(4)
print ('I ask riddles accompanied by 4 options')
time.sleep(4)
print ('In order to select an option, type the letter (in upper case) beside the option')
time.sleep(5)
print ('If you solve enough riddles, you will progress to the next level, with a total of 4 levels')
time.sleep(5)
print ('You get three lives, you lose one live everytime you get one wrong, you lose when you reach zero lives.')
time.sleep(6)
print ('Your final score will be based on how many questions you got right and how many lives you have left.')
time.sleep(5)
print ('Enough banter, lets begin!')
time.sleep(4)
# introduction, explaining rules

first_level_first_question = str(input('How many cats can be put in an empty pool? A: none B: 1 C: 50'))
if first_level_first_question == 'B':
  print ('Correct! Once you put a cat in a pool, it will not be empty anymore.')
  Answered = Answered + 1
else:
  print ('Incorrect! Once you put a cat in a pool, it will not be empty anymore.')
  Lives = Lives - 1
  if Lives == 0:
    print ('Game Over')
    pygame.quit()

first_level_second_question = str(input('What starts with e, ends with e, and has a letter inside? A: envelope B: eagle C: office'))
if first_level_second_question == 'A':
  print ('Correct! first and last letter of envelope is e and they often contain letters.')
  Answered = Answered + 1
else:
  print ('Incorrect! first and last letter of envelope is e and they often contain letters.')
  Lives = Lives - 1
  if Lives == 0:
    print ('Game Over')
    pygame.quit()

first_level_third_question = str(input('What gets wet when you become dry? A: towel, B: fan, C: human'))
if first_level_third_question == 'A':
  print ('Correct! towel soaks water, making you dry.')
  Answered = Answered + 1
else:
  print ('Incorrect! towel soaks water, making you dry.')
  Lives = Lives - 1
  if Lives == 0:
    print ('Game Over')
    pygame.quit()

print ('Congratulations! Not many manage to finish the first level.')
time.sleep(4)
print ('I admit, you do posses some skill.')
time.sleep(3)
print ('Guess I will have to use 50 percent of my true power.')
time.sleep(3)
print ('Please continue to entertain me')
time.sleeo(3)
Levels = Levels + 1

second_level_first_question = str(input('I travel all around the world, but always stay in my corner, what am I? A: Canada B: Stamp C: mailman'))
if second_level_first_question == 'B':
  print ('Correct! postal stamps go in the corner of envolepes.')
  Answered = Answered + 1
else:
  print ('Incorrect! postal stamps go in the corner of envolepes.')
  Lives = Lives - 1
  if Lives == 0:
    print ('Game Over')
    pygame.quit()
  
second_level_second_question = str(input('What disappears as soon as you say their name? A: Ghost B: Ivan C: Silence'))
if second_level_second_question == 'C':
  print ('Correct! As soon as you talk, it is no longer silent')
  Answered = Answered + 1
else:
  print ('Incorrect! As soon as you talk, it is no longer silent')
  Lives = Lives - 1
  if Lives == 0:
    print ('Game Over')
    pygame.quit()

second_level_third_question = str(input('How many letters are in alphabet? A: 8 B: 11 C:26'))
if second_level_third_question == 'A':
  print ('Correct! There are 8 letters in the word alphabet')
  Answered = Answered + 1
else:
  print ('Incorrect! There are 8 letters in the word alphabet')
  Lives = Lives - 1
  if Lives == 0:
    print ('Game Over')
    pygame.quit()

print ('Not many manage to pass the second level...')
time.sleep(3)
print ('Please forgive my arrogance, I will give you the respect you deserve')
time.sleep(4)
print ('My best riddles are coming your way')
time.sleep(3)
Levels = Levels + 1

third_level_first_question = str(input('What do you call a bear without an ear? A: Bear B: Disabled C: B'))
if third_level_first_question == 'A':
  print ('Correct! A human without an ear is still refered to as a human')
  Answered = Answered + 1
else:
  print ('Incorrect! A human without an ear is still refered to as a human')
  Lives = Lives - 1
  if Lives == 0:
    print ('Game Over')
    pygame.quit()
  
third_level_second_question = str(input('What do you break before you use it? A: Ivan B: egg C: batteries'))
if third_level_second_question == 'B':
  print ('Correct! You must discard the egg shell in order to use an egg.')
  Answered = Answered + 1
else:
  print ('Incorrect! You must discard the egg shell in order to use an egg.')
  Lives = Lives - 1
  if Lives == 0:
    print ('Game Over')
    pygame.quit()
  
third_level_third_question = str(input('This belongs to you, but it is used by everyone, what is it? A: Oxygen B: Name C: Assistance'))
if third_level_third_question == 'B':
  print ('Correct! your name is yours, but people use it to call your attention')
  Answered = Answered + 1
else:
  print ('Incorrect! your name is yours, but people use it to call your attention')
  Lives = Lives - 1
  if Lives == 0:
    print ('Game Over')
    pygame.quit()
  
print ('Congratulations, you are the only mortal to have completed my riddles.')
time.sleep(3)
print (Score)
