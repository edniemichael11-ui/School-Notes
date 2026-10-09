def get_user_in_withing_range_default_params(min = 1,max = 100):  
   while True:
           t = input(f"Enter a number between {min:int} and {max:int}: ")
           if t.isdigit():
               if int(t) >= min and int(t) < max:
                   print("Good job.")
                   break
           print("Invalid, Try again.")
           return int(t)

userin = 0
while userin != 5:
    userin = get_user_in_withing_range_default_params(max=50)
