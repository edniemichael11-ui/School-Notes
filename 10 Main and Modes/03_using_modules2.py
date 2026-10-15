import module_with_main as mm
#from module_with_main import area as area

def main():
    print(__name__)
    num = int(input("Enter a radius of a circle: "))
    print(f" The area of a circle with a radius of {num} is {mm.area(num)}")


if __name__ == "__main__":
    main()
