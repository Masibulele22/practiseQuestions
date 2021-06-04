first_score = float(input(("Hey there Mochacho! Please typein your first score: ")))
second_score = float(input(("Good going! Please typein your second score: ")))
third_score = float(input(("Almost there... Now please typein your third score: ")))

score_total = first_score + second_score + third_score
score_average = score_total/3
print("Cool beans! Your score average is: " + str(score_average) + "!")
