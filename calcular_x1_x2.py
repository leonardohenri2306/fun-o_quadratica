print("Vamos calcular as raízes de uma equação do segundo grau.")
print("Mas antes precisaremos de algumas informações.\n")

a = int(input("Digite o valor do coeficiente a: "))
b = int(input("Digite o valor do coeficiente b: "))
c = int(input("Digite o valor do coeficiente c: "))

result = b**2-4*a*c

print("\n\tCalculando delta...\n")
print("Formula de delta b²-4.a.c\n")
print("Lógo %d²-4.%d.%d\n" %(a, b, c))
print("Delta = %d\n" %(result))

if result > 0:
    raízdelta = result**0.5

    print("\tVamos calcular bhaskara, (x¹ +) (x² -)\n")


    print("Formula de bhaskara x = (-b +- √delta) / 2.a\n")

    x1 = (-b + raízdelta)/(2*a)
    print("x¹ (Positivo) = %d\n" %(x1))

    x2 = (-b - raízdelta)/(2*a)
    print("x² (Negativo) = %d" %(x2))

    print("\nTodos os resultados, '100%' corretos. Volte sempre!!!")

else:
    print("\tDelta negativo não existe raiz real, impossivel calcular x¹ x². Volte sempre!!!")
