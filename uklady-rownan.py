#base
print("{ a1 x + b1 y = c1\n{ a2 x + b2 y = c2")

#first row
a1 = int(input("a1 = "))
b1 = int(input("b1 = "))
c1 = int(input("c1 = "))

print("\n{", a1, "x +", b1, "y = ", c1, "\n{ a2 x + b2 y = c2\n")

#second row
a2 = int(input("a2 = "))
b2 = int(input("b2 = "))
c2 = int(input("c2 = "))

#filled and solved
print("Solution\n==========\n{", a1, "x +", b1, "y =", c1, "\n{", a2, "x +", b2, "y =", c2)

#W calc
W = a1 * b2 - a2 * b1

print("\n    |", a1, " ", b1, "|", "\nW = |       | = ", a1, "*", b2, "-", a2, "*", b1, "=", W, "\n    |", a2, " ", b2, "|")

#Wx calc
Wx = c1 * b2 - c2 * b1

print("\n     |", c1, " ", b1, "|", "\nWx = |       | = ", c1, "*", b2, "-", c2, "*", b1, "=", Wx, "\n     |", c2, " ", b2, "|")

#Wy calc
Wy = a1 * c2 - a2 * c1

print("\n     |", a1, " ", c1, "|", "\nWy = |       | = ", a1, "*", c2, "-", a2, "*", c1, "=", Wy, "\n     |", a2, " ", c2, "|")

#x calc
if W != 0:
    x = Wx / W
else:
    x = 0


print("\nx = Wx / W =", Wx, "/", W, "=", x)

#y calc
if W != 0:
    y = Wy / W
else:
    y = 0

print("y = Wy / W =", Wy, "/", W, "=", y)

#final print
print("\n{", a1, "*", x, "+", b1, "*", y, "=", c1, "\n{", a2, "*", x, "+", b2, "*", y, "=", c2, "\n\nx =", x, "\ny =", y, "\n==========")

#types
if W != 0:
    print("Układ oznaczony")
if W == 0 and Wx == 0 and Wy == 0:
    print("Układ nieoznaczony")
if W == 0 and Wx != 0 or W == 0 and Wy != 0:
    print("Układ sprzeczny")