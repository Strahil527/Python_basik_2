def workOrHoliday():
    day_of_week = input("Enter day of week: ")

    match day_of_week:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            print("Working day")
        case "Saturday" | "Sunday":
            print("Holiday")
        case _:
            print("ERROR!")

workOrHoliday()