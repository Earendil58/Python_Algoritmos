kg = float(input('Ingrese su peso, en kg: '))
altura = float(input('Ingrese su altura, en mts: '))

IMC = round((kg / (altura) ** 2),2)

print(f'Su indice de masa corporal es de: {IMC}')

if IMC <= 16:
    print('Necesita asistencia de un médico, los riesgos para su salud son muy altos')

elif 16 < IMC <= 17:
    print('Usted tiene infrapeso, aliméntese más')

elif 17 < IMC <= 18:
    print('Usted tiene bajo peso, aliméntese mejor')

elif 18 < IMC <= 26:
    print('Usted tiene un peso saludable, continúe así!')

elif 26 < IMC < 30:
    print('Tiene sobrepeso de grado I, hoy es un buen día para empezar a hacer ejercicios')

elif 30 < IMC <= 35:
    print('Tiene obesidad de grado II, necesita el apoyo de un plan nutricional')

elif 35 < IMC <= 40:
    print('Tiene obesidad grado III (pre-mórbida), consulte con su médico los riesgos para su salud')

elif IMC > 40:
    print('Usted tiene obesidad de grado IV (mórbida), los riesgos para su salud son muy altos, consulte con su médico a la brevedad')
