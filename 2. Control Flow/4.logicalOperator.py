# and
# or
# not
# In python logical operators are short circuit

high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
