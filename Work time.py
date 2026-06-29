def workTime():
    day_time = int(input("Enter time: "))
    day = input("Enter day of week: ")

    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            if day_time >= 10 and day_time <= 18:
                print("OPEN")
            else:
                print("CLOSED")
        case _:
            print("CLOSED")

workTime()