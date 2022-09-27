import random


print("all rights to the owners")

randomSeedGen = random.random()
print ("seed of the day: " +str(randomSeedGen), "-"+str(randomSeedGen))
print("\n")
print("please enter the correct X and Y coordinates")

X_coordinates = float(input("Enter the X coordinates: "))
Y_coordinates = float(input("Enter the Y coordinates: "))
Z_coordinates = float(input("Enter the Z coordinates: "))

def noDecimalInYcoord():            #Updates will be added later
 pass




X_coord_div = float(X_coordinates / 8)
Y_coord_div = int(Y_coordinates / 8)
Z_coord_div = float(Z_coordinates / 8)



print("coordinates to the nether or overworld:")
for coordinates in X_coord_div, Y_coord_div, Z_coord_div:
    print("X: " +str(X_coord_div), "  " "Y: "+str(Y_coord_div),"   " "Z: " +str(Z_coord_div))

