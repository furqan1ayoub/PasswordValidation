#area of a triangle (1/2 × base × height)
# but i will make it with using->functions-> reusable code piece for reducinig code redunacny

def calcAreaTriange(base,height):
    calculation = (base*height) * 1/2
    return calculation
base = int(input("Enter the base of the Triangle:- "))
height = int(input("Enter the height of the Triangle:- "))
area = calcAreaTriange(base,height)
print(area)


#can call it anywhere
#like
print(calcAreaTriange(3,97))