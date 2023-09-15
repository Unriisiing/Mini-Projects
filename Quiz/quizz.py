print ("Welcome to the QUIZ")

playing = input("Do you want to play ? : ")

if (playing.lower() != "yes"):
    quit()

print ("Okay let's play :) ")
score = 0

answer = (input ("What does MSC stand for ? "))

if answer == "mastere of science" :
    print('Correct ! ')
    score += 1
else:
    
    print('incorrect')
    score -= 1
answer = (input ("What does MSC stand for ? "))

if answer == "mastere of science" :
    print('Correct ! ')
    score += 1
else:
    
    print('incorrect')
    score -= 1

print(score)
