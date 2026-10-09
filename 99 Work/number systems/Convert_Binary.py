def conv_num_to_base(num,Binary_Base):
    binary = []
    remaining_num = num
    while True:
        if num < Binary_Base:
                    binary.append(num)
                    break
        binary.append(num%Binary_Base)
        remaining_num = num//Binary_Base
        num = remaining_num
    binary.reverse()
    print(binary)
    return binary
def get_input_1():
   num = int(input("Number you want Converted: "))
   Binary_Base = int(input("Base: ")) 
   return num,Binary_Base
def return_to_number(deci,base2):
   deci_list = [int(nums)for nums in deci] #splits the input into a list
   deci_list.reverse()
   total = 0
   for power,digit in enumerate(deci_list): #enumerate it gives the index positon which allowys it to give the correct power to multiple by
       value = digit * (base2 ** power)
       total += value
   print(f"Total: {total}")
def get_input_2():
    base2 = int(input("What base are you solving with: "))
    deci = (input("What deci are you solving: "))
    return base2,deci



while True:
    print("A. To Deci")
    print("B. From Deci to Number")
    print("Q. Quit")
    action = input("Action: ").strip().capitalize()
    if action == "A":
        num,Binary_Base = get_input_1()
        conv_num_to_base(num,Binary_Base)
        action=input("Would you like to convert it to a base 10 (Y/N): ").strip().capitalize()
        if action == "Y":
            base2 = 10
            binary = conv_num_to_base(num,Binary_Base)
            deci = [int(nums) for nums in binary]
            return_to_number(deci,base2)
        elif action == "N":
            break
        else:
            print("Enter a Valid Input")
    elif action == "B":
        base2,deci = get_input_2()
        return_to_number(deci,base2)
    elif action == "Q":
        print("Goodbye")
        break
