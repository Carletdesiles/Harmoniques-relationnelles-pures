from sympy import symbols, Mod, pi, sin, pprint

# Distances symboliques (exemple triangle)
R12, R13, R23 = symbols('R12 R13 R23', positive=True, real=True)

# Phases fixes (distance détermine la phase)
phi12 = Mod(R12, 2*pi)
phi13 = Mod(R13, 2*pi)
phi23 = Mod(R23, 2*pi)

# Harmonique globale : produit sur les paires
H = (1 + sin(phi12)**2) * (1 + sin(phi13)**2) * (1 + sin(phi23)**2)

print("Expression symbolique de H :")
pprint(H)

# Test numérique 1 : distances éloignées
valeurs = {R12: 5.0, R13: 4.0, R23: 3.0}
print("\nH avec distances éloignées :", H.subs(valeurs).evalf())

# Test numérique 2 : un fort rapprochement
valeurs_proche = {R12: 0.01, R13: 4.0, R23: 3.0}
print("H avec rapprochement R12 très petit :", H.subs(valeurs_proche).evalf())
