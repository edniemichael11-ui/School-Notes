total = 0
week = 0
float(total)

while True:
    savings_goal = (input("Savings Goal: ")).strip()
    savings_goal = float(savings_goal)

    if savings_goal < 0:
        print("Invalid savings goal")
    else:
        weekly_deposit = input("Weekly deposit: ").strip()
        weekly_deposit = float(weekly_deposit)
        if weekly_deposit > 0:
            while total < savings_goal:
                total = total + weekly_deposit
                week+=1
                print(f"Week {week}: $ {total:,.2f}")
            print("Saving goal Reached")
            break
        else:
            print("Invalid Weekly Deposit")
    
            


