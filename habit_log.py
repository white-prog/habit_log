def main():
    from datetime import date
    print("Habit Tracker")
    #habits_log
    habits = []
    print("1. Log a habit")
    print("2. View logged habits")
    print("3. Exit")
    while True:
        try:
            choose = int(input("Choose an option: "))
        except:
            raise "Error"
        if choose == 1:
            habit = input("Enter the habit you completed: ")
            habits.append(habit)
            print(f"Habit '{habit}' logged for today.")
        elif choose == 2:
            print("------------------------------")
            print("Habit log")
            print("------------------------------")
            cnt = 1
            for i in habits:
                print(f"{cnt} : {i} (Logged on {date.today()})")
                cnt += 1
            print("------------------------------")
        elif choose == 3:
            print("Thank you!")
            break
        else:
            print("Wrong prompt")
if __name__ == "__main__":
    main()
        
            