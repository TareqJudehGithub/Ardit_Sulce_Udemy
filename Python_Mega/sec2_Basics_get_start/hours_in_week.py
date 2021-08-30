# write a program that calculates hours in a week
def hours_in_week(week):
     days = 7
     hours = 24
     return f"There are {(days * hours) * week} hours in {week} week(s)."


print(hours_in_week(1))