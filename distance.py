# This is python program to determine the distance.
x1_and_y1 = input("Enter the values of x1 and y1 in format (x1,y1) ")
x2_and_y2 = input("Enter the values of x2 and y2 in format (x2,y2) ")
comma1 = x1_and_y1.find(",")
comma2 = x2_and_y2.find(",")
x1 = int(x1_and_y1[1:comma1])
y1 = int(x1_and_y1[comma1+1:-1])
x2 = int(x2_and_y2[1:comma2])
y2 = int(x2_and_y2[comma2+1:-1])
distance = ((x2-x1)**2 + (y2-y1)**2)**1/2
round = round(distance,3)
print(f"The distance between these points is:{round}")
# This program is to check the quadrants of point(x1,y1) and (x2,y2).
if x1 > 0 and y1 > 0:
    print("point(x1,y1) is in 1st quadrant")
elif x1 < 0 and y1 > 0:
    print("point(x1,y1) is in second quadrant")
elif x1 < 0 and y1 < 0:
    print("point(x1,y1) is in third quadrant")
elif x1 > 0 and y1 < 0:
    print("point(x1,y1) is in fourth quadrant")
if x2 > 0 and y2 > 0:
    print("point(x2,y2) is in 1st quadrant")
elif x2 < 0 and y2 > 0:
        print("point(x2,y2) is in second quadrant")
elif x2 < 0 and y2 < 0:
        print("point(x2,y2) is in third quadrant")
elif x2 > 0 and y2 < 0:
        print("point(x2,y2) is in fourth quadrant")

