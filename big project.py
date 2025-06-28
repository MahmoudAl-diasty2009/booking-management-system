print("Welcome to our city nefertech")
print("You need to Sign Up before you can Login.")

username = input("Please enter a username: ")
print("Note: The password should be 8 characters long with UPPER and lower case letters only (no numbers).")

while True:
    password = input("Enter a password: ")

    if len(password) != 8:
        print("Password must be exactly 8 characters.")
        continue
    if any(c.isdigit() for c in password):
        print("Password should not contain numbers.")
        continue
    if password.isalpha() and any(c.isupper() for c in password) and any(c.islower() for c in password):
        confirm = input("Confirm your password: ")
        if password == confirm:
            print("Successful Registration!")
            break
        else:
            print("Passwords do not match, please try again.")
    else:
        print("Weak password. The password must contain both upper and lower case letters.")

print("\nNow, please log in with the credentials you just created.")

while True:
    login_username = input("Write the user name: ")
    if login_username != username:
        print("User name is wrong. Try again.")
    else:
        break

while True:
    login_password = input("Write the password: ")
    if login_password != password:
        print("Password is wrong. Try again.")
    else:
        break

print("Welcome " + username)

print("************************************************")

services = [
    "1 - إصدار رخصة سيارة أول مرة",
    "2 - تجديد رخصة سيارة",
    "3 - إصدار رخصة قيادة أول مرة",
    "4 - تجديد رخصة قيادة",
    "5 - إصدار بدل فاقد"
]

print("Available services:")
for s in services:
    print(s)

while True:
    service_input = input("Choose the number of the service: ")
    if service_input.isdigit():
        service_num = int(service_input)
        if 1 <= service_num <= 5:
            break
        else:
            print("Choose from 1 to 5:")
    else:
        print("Enter a valid number.")

print("You chose:", services[service_num - 1])

print("************************************************")

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
print("Available days:")
for i, day in enumerate(days, 1):
    print(f"{i} - {day}")

while True:
    day_input = input("Select day number: ")
    if day_input.isdigit():
        day_num = int(day_input)
        if 1 <= day_num <= 5:
            break
        else:
            print("Choose from 1 to 5:")
    else:
        print("Enter a valid number.")

print("You chose:", days[day_num - 1])

print("************************************************")

times = ["9:00", "10:00", "11:00", "12:00", "1:00"]
print("\nAvailable time slots:")
for i, time in enumerate(times, 1):
    print(f"{i} - {time}")

while True:
    time_input = input("Choose time number: ")
    if time_input.isdigit():
        time_num = int(time_input)
        if 1 <= time_num <= 5:
            break
        else:
            print("Choose from 1 to 5:")
    else:
        print("Enter a valid number.")

print("You selected:", times[time_num - 1])

print("************************************************")

while True:
    name = input("Enter your full name (4 parts): ")
    if len(name.strip().split()) == 4:
        break
    else:
        print("Please rewrite your full name (4 names):")

while True:
    Id = input("Enter your ID: ")
    if Id.isdigit() and len(Id) == 14:
        print("ID is valid")
        break
    else:
        print("The ID must be 14 digits. Rewrite it:")

print("************************************************")

print("Booking confirmed!")
print("Name:", name)
print("ID:", Id)
print("Service:", services[service_num - 1])
print("Day:", days[day_num - 1])
print("Time:", times[time_num - 1])

print("************************************************")
do_analysis = input("Would you like to see statistics about the most/least crowded days? (yes/no): ").strip().lower()

if do_analysis == "yes":
    print("\nAnalyzing statistics...")

    services_data = [
        'إصدار رخصة سيارة أول مرة',
        'تجديد رخصة سيارة',
        'إصدار رخصة قيادة أول مرة',
        'تجديد رخصة قيادة',
        'إصدار بدل فاقد'
    ]

    dates = [
        ["13-04-2025", "Sunday",    [4, 6, 7, 8, 1]],
        ["14-04-2025", "Monday",    [2, 1, 8, 6, 4]],
        ["15-04-2025", "Tuesday",   [3, 1, 6, 6, 4]],
        ["16-04-2025", "Wednesday", [1, 6, 9, 8, 3]],
        ["17-04-2025", "Thursday",  [4, 7, 7, 10, 1]]
    ]

    total = 0
    days_stats = []

    for row in dates:
        total += row[2][0]
        days_stats.append((row[1], row[2][0]))

    average = total / len(dates)
    most = max(days_stats, key=lambda x: x[1])
    least = min(days_stats, key=lambda x: x[1])

    print("Statistics for service:", services_data[0])
    print("Average bookings:", average)
    print("Most crowded day:", most[0])
    print("Least crowded day:", least[0])
else:
    print("Statistics skipped.")
