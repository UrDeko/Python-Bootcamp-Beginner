print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? "))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
num_people = int(input("How many people to spit the bill between? "))

tip_amount = percentage_tip / 100 + 1
final_bill = round(total_bill * tip_amount, 2)
share = "{:.2f}".format(final_bill / num_people)

print(f"Each person should pay: {share}")