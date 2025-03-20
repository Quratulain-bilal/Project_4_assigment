def calculate_energy(mass):
    C = 299792458  # Speed of light in m/s
    return mass * (C ** 2)

def main():
    """ Command-line version of the Mass-Energy Equivalence Calculator """
    try:
        mass = float(input("Enter kilos of mass: "))
        energy = calculate_energy(mass)
        print("e = m * C^2...")
        print(f"m = {mass} kg")
        print(f"C = {299792458} m/s")
        print(f"{energy} joules of energy!")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()


