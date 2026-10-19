import os

def getValidInt(prompt, min = 0, max = 100):
    while True:
        P_Input = int(input(prompt))
        if P_Input >= min and max >= P_Input:
            return P_Input


def getValidResponse(prompt, validResponses: list):
    ValidResponses = [response.lower() for response in validResponses]
    while True:
        Response = input(prompt).strip().lower()

        if Response in ValidResponses:
            return Response


def getNonEmptyString(prompt):
    while True:
        Response = input(prompt).strip()
        if len(Response) <= 0:
            continue
        else:
            return(Response)

def clearScreen():
    os.system("cls")


def pause(message = "Press Enter to continue..."):
    Action = input(message)


def printNumberedList(items):
    if not items:
        print("No Items to Display")
    else:
        for index, item in enumerate(items, start = 1):
            print(f"{index}. {item}")

def filiterByLength(items, minLength, maxLength):
    filtered_list = [ item for item in items if len(item) <= maxLength and len(item) >= minLength]
    return filtered_list

def analyzeNumbers(numbers):
    pos_nums = [ nums for nums in numbers if nums > 0] 
    pos_ammount = len(pos_nums)
    neg_nums = [neg_num for neg_num in numbers if neg_num < 0]
    neg_ammount = len(neg_nums)
    zeros = [ number for number in numbers if number == 0]
    zero_ammount = len(zeros)
    return pos_nums,pos_ammount,neg_ammount, zero_ammount 

if __name__ == "__main__":
    getValidInt()
    getValidResponse()
    clearScreen()
    getNonEmptyString()
    pause()
    printNumberedList()
    filiterByLength()
    analyzeNumbers()