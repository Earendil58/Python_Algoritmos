# Realizar un programa que tome tres números, los ordene de mayor a menor.
# Sobre los valores ordenados diga si el tercero es el resto de la división de los dos primeros.

primer_numero = int(input("Primero numero: "))
segundo_numero = int(input("Segundo numero: "))
tercer_numero = int(input("Tercer numero: "))

mayor = medio = menor = None


if primer_numero > segundo_numero and primer_numero > tercer_numero:
    mayor = primer_numero
    if segundo_numero > tercer_numero:
        menor = tercer_numero
        medio = segundo_numero
    else:
        menor = segundo_numero
        medio = tercer_numero


elif segundo_numero > primer_numero and segundo_numero > tercer_numero:
    mayor = segundo_numero
    if primer_numero > tercer_numero:
        medio = primer_numero
        menor = tercer_numero
    else:
        medio = tercer_numero
        menor = primer_numero

else:
    mayor = tercer_numero
    if primer_numero > segundo_numero:
        medio = segundo_numero
        menor = primer_numero



print(f'''El orden de los números es: 
          Menor: {primer_numero}
          Medio: {segundo_numero}
          Mayor: {tercer_numero}''')


    

