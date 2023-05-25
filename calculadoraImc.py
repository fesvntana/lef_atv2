def calcImc(p, a):
    imc = p / (a * a)
    return imc

def verifyCategory(imc):
    if imc < 18.5:
        return "MAGREZA"
    elif imc <= 24.9:
        return "NORMAL"
    elif imc <= 30:
        return "SOBREPESO"
    else:
        return "OBESIDADE"

p = float(input("Peso (kg): "))
a = float(input("Altura (m): "))

imc = calcImc(p, a)
category = verifyCategory(imc)

print("Índice de Massa Corpórea (IMC) :", round(imc,2))
print("Situação:", category)
