coleck = int(input("enter mass in kg: "))

r = 6378 * (10**3)
m1 = 5.9742 * (10**24)
G = 6.67300 * (10**(-11))
grav_force = G * m1 * coleck / (r**2)
g = grav_force / coleck
print("acceleration due to gravity is {:<.2f}".format(g))