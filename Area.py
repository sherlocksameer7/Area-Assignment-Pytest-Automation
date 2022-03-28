def Area_Rectangle(l, b):
    return l * b


def Peri_Rectangle(l, b):
    return 2 * (l + b)


def Area_circle(r):
    return 3.14 * r * r


def Area_Sqr(s):
    return s * s


def Area_Triangle(h, b):
    return 0.5 * h * b


if __name__ == "__main__":


    while True:

        print("1.Area of Rectangle: ")
        print("2.Perimeter of Rectangle: ")
        print("3.Area of Circle: ")
        print("4.Area of Square: ")
        print("5.Area of Triangle: ")
        print("6.Exit: ")


        choice = int(input("Select any Option : "))

        if choice == 1:
            l = int(input("Enter the length of the rectangle: "))
            b = int(input("Enter the breadth of the rectangle: "))
            result = Area_Rectangle(l, b)
            print("Area of rectangle is: ", result)


        elif choice == 2:
            l = int(input("Enter the length of the rectangle: "))
            b = int(input("Enter the breadth of the rectangle: "))
            answer = Peri_Rectangle(l, b)
            print("perimeter of rectangle is: ", answer)


        elif choice == 3:
            r = int(input("Enter the radius: "))
            result = Area_circle(r)
            print("Area of circle is: ", result)


        elif choice == 4:
            s = int(input("Enter the side of square: "))
            result = Area_Sqr(s)
            print("Area of square is: ", result)


        elif choice == 5:
            h = int(input("Enter the height of triangle: "))
            b = int(input("Enter the base of triangle: "))
            result = Area_Triangle(h, b)
            print("Area of triangle is: ", result)


        elif choice == 6:
            break


        else:
            print("Invalid Option ! ")