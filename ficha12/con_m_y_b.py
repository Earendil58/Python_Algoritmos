# Desarrollar un programa que permita ingresar por teclado, con palabras separadas por un espacio y terminado en punto. En base al texto ingresado, determinar:

# Cuántas palabras tienen una m y una b a partir de la tercer letra.
# Cuántas palabras comienzan con la letra p seguida de cualquier vocal.
# Cuántas palabras comienzan y terminan con el mismo carácter.

def tieneMB(letra):
    if letra == 'm' or letra == 'b':
        return True
    return False

def tieneVocal(letra):
    vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
    if letra in vocales:
        return True
    return False
    
    
def principal():
    posicion_letras = 0
    tiene_m_b_desde_tercera_letra = 0
    anterior = ''
    palabra_comienza_p_sigue_vocal = 0
    cant_palabras = 0
    
    texto = input('Ingrese el texto a analizar: ')
    
    for letra in texto:
        
        if letra == ' ' or letra == '.':
            posicion_letras = 0
            
            
        else:
            posicion_letras += 1
            
            if posicion_letras >= 3 and tieneMB(letra):
                tiene_m_b_desde_tercera_letra += 1
                
            if posicion_letras == 2 and anterior == 'p' and tieneVocal(letra):
                palabra_comienza_p_sigue_vocal += 1
                
                
                
            anterior = letra
                
    
    
    print(f'La cantidad de palabras que tienen "m" o "b" a partir de la tercera letra son: {tiene_m_b_desde_tercera_letra}')
    print(f'La cantidad de palabras que comienzan con "p" y siguen con una vocal, son: {palabra_comienza_p_sigue_vocal}')
    

principal()