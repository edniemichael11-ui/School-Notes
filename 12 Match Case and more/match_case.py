def get_day_name_if_else(num: int) -> None:
    """Print the day for a number from 1 (Sunday) to 7 (Saturday)."""
    if num == 1:
        print("Sunday")
    elif num == 2:
        print("Monday")
    elif num == 3:
        print("Tuesday")
    elif num == 4:
        print("Wednesday")
    elif num == 5:
        print("Thursday")
    elif num == 6:
        print("Friday")
    elif num == 7:
        print("Saturday")
    else:
        print("Invalid number.")


def get_day_name_match(num: int) -> None:
    """Print the day for a number from 1 (Sunday) to 7 (Saturday)."""
    match num:
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wednesday")
        case 5:
            print("Thursday")
        case 6:
            print("Friday")
        case 7:
            print("Saturday")
        case _:
            print("Invalid number.")


def is_weekend(day: str) -> bool:
    """Return whether day is a weekend day; raise ValueError for an unknown day."""
    match day:
        case "Saturday":
            return True
        case "Sunday":
            return True
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wednesday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case _:
            raise ValueError(f"{day!r} is not a valid day of the week")


def is_weekend_shorter_match(day: str) -> bool:
    """Check for weekend days with grouped patterns; raise ValueError for unknown days."""
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            raise ValueError(f"{day!r} is not a valid day of the week")


if __name__ == "__main__":
    get_day_name_if_else(1)
    get_day_name_match(1)
    print(is_weekend("Sunday"))
    print(is_weekend("Monday"))
    print(is_weekend_shorter_match("Sunday"))
    print(is_weekend_shorter_match("Monday"))
