print("hello world!")


playing = input("do u want to play quiz?")

print(playing)

if playing.lower() != "yes": 
    quit()
print ("okay")
score = 0
       
answer = input("What does CPU stand for?")
if answer.lower() == "central processing unit":
    print("Dung roi")
    score += 1
else:
    print("wrong")


answer = input("What does CPU stand for?")
if answer.lower() == "central processing unit":
    print("Dung roi")
    score += 1
else:
    print("wrong")

print ("you got " + str(score) + " question correct!")
print ("you got " + str(((score/4)) * 100) + "% question correct!")


