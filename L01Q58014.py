R = float(input("Enter length of row (feet): "))
E = float(input("Enter amount of space used by end-post assembly (feet): "))
S = float(input("Enter space between vines (feet): "))

V = (R - (2*E)) / S

print("Number of grapevines that can fit in the row: ", int(V))

