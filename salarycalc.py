Analyst = (float(300))
Developer = (float(600))
Manager = (float(900))

EmployeeName = str(input("Enter employee's name: "))
print("Employee's name: " + EmployeeName)

Hours = float(input("Enter Hours worked: "))
print(f"Hours worked: {Hours}")

Position = str(input("What is your position? [Analyst, Developer, Manager]: "))
grossSal = .0
match Position:
    case "Analyst":
        grossSal = Hours * Analyst
    case "Developer":
        grossSal = Hours * Developer
    case "Manager":
        grossSal = Hours * Manager
print(grossSal)

Taxed = grossSal * 0.010
ContributeFee = grossSal * 0.005

taxdeduc = grossSal-Taxed
contributax = taxdeduc-ContributeFee

print(f"Gross salary was: {grossSal}")

print(f"Tax deduction fee was: {Taxed}")
print(f"Contribution fee was: {ContributeFee}")

print(f"Yor take home salary is {contributax}")