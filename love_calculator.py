print("Welcome to the Love Calculator!")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()
combined_string = name1 + name2

criteria = "true love"
true_score = 0
love_score = 0

for index, letter in enumerate(criteria):
    if index < criteria.index(' '):
        true_score += combined_string.count(letter)
    if index > criteria.index(' '):
        love_score += combined_string.count(letter)

final_score = int(f"{true_score}{love_score}")
if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go toghether like coke and mentos")
elif final_score >= 40 and final_score <= 50:
    print(f"Your score is {final_score}, you are alright toghether")
else:
    print(f"Your score is {final_score}")



