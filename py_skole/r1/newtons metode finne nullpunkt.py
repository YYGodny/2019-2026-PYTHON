import math

# Initialverdier
x = 10.0  # Initial gjetning
tolerance = 1e-6
max_iterations = 100

for i in range(max_iterations):
    # Definer funksjonen og dens deriverte her
    fx = x**2 - 4*x  # f(x) = x^2 - 4
    fpx = 2*x-4    # f'(x) = 2x
    
    if abs(fx) < tolerance:
        print(f"Nullpunkt funnet: x = {x:.6f}")
        print(f"Antall iterasjoner: {i}")
        print(f"f(x) ved nullpunkt: {fx:.6e}")
        break
    
    if fpx == 0:
        print("Derivert er null. Kan ikke fortsette.")
        break
    
    x = x - fx / fpx
else:
    print("Maks antall iterasjoner nådd uten konvergens.")
    print(f"Siste x-verdi: {x:.6f}")
