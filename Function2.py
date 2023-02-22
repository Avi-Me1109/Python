def calculation (m, v):
    kinetic_energy = 1/2 * m * (v*v)
    print("The kinetic energy in the object is", kinetic_energy)

mass = float(input("Enter mass(kg): "))
velocity = float(input("Enter velocity(m/s): "))

calculation(mass, velocity)