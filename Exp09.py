n = int(input("Enter no of people: "))
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
time_slots = ["10AM", "11AM", "2PM", "4PM"]
all_busy = []
for i in range(n):
    print(f"\nEnter busy slots for person {i+1}")
    count = int(input("How many busy slots?\n"))
    busy = []
    for j in range(count):
        day = input("Enter day: ")
        time = input("Enter time: ")
        busy.append((day, time))
    all_busy.append(busy)
place = input("\nEnter meeting place: ")

def schedule_meeting():
    for day in days:
        for time in time_slots:
            avaliable = True
            for person in all_busy:
                if(day, time) in person:
                    avaliable = False
                    break
            if avaliable:
                return day, time
    return None, None
day, time = schedule_meeting()
if day and time:
    print("\nMeeting Schedules Successfully")
    print("Day: ", day)
    print("Time: ", time)
    print("Place: ", place)
else:
    print("\nNo common free slots avaliable.")