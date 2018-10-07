"""
Compute the area of a room
"""

# Read the input values from the user

#My solution
width=float(input('Enter the width of the room'))
length=float(input('Enter the length of the room'))
area=width*length
print('The area of the room is '+str(area)+'.')

#solution of the book (pattern solution)

length=float(input("Enter the length of room in feet: "))
width=float(input('Enter the width of the room in feet: '))

#compute the area of the room
area=width*length

#Disply the result
print("The area of the room is",area,"square feet")
