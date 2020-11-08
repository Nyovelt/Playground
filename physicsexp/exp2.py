from physexp import *

a = [2.953,
2.953,
2.951,
2.952,
2.953

     ]


print("$2 \\bar{T}=frac15 \\times (", end="")
for i in a:
    print(i, end="+")
print("\b", end="")
print(')=', end="")
print(round(Avg(a), 3), end="$")
print()

print('''$\sigma_{2 \\bar{T}}=\\sqrt{\\frac{\\sum_{i=1} ^ {n}\\left(2 T_{i}-2 \\bar{T}\\right) ^ {2}}{n(n-1)}}=\\sqrt{\\frac{''')
for i in a:
    print("(", i, "-", round(Avg(a), 3), ")^2", end="+")
print("\b")

print("}{n(n-1)}}=", end="")
print(round(standardDeviationOfTheMean(a), 3), end="$")

print()
print("$U_{A}=t_{P} \\cdot \\sigma_{2 \\bar{T}}=2.78 \\times ", end="")
print(standardDeviationOfTheMean(a), end="=")
tmp = standardDeviationOfTheMean(a) * 2.78
print(round(tmp, 3), end="$")


print()
print("$U = \\sqrt{U_A^2 + U_B^2} = \\sqrt{", end="")
print(round(tmp, 3), end="")
print("^2 + 0.0095^2} =", end="")
print(round((round(tmp, 3)**2 + 0.0095**2)**0.5, 3), end="$")

print()
print("故测得的两倍周期$2T = (", end="")
print(round(Avg(a), 3), end="\\pm")
print(round((round(tmp, 3)**2 + 0.0095**2)**0.5, 3), end=")$")
print()
