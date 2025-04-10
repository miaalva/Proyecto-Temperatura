def obtener_temperatura(dia):
    input_str = input (f"Ingrese la temperatura del dia {dia}:")
    # Validamos que la entrada sea un valida
    try:
        temperatura = float(input_str)
        return temperatura
    except ValueError:
        print("Ingresar un número válido")
        return None
    
def calcular_promedio(semana):
    # Calculamos el promedio de una lista de números
    if len(semana) == 0:
        return 0
    return sum(semana) / len(semana)

def encontrar_max_min(semana):
    # Encontramos el máx y mín de una lista de números
    if len(semana) == 0:
        return None, None, None, None
    maximo = max(semana)
    minimo = min(semana)
    indice_maximo = semana.index(maximo)
    indice_minimo = semana.index(minimo)
    return maximo, minimo, indice_maximo, indice_minimo

def encontrar_temperaturas_por_sobre_el_promedio(semana, promedio):
    # Separamos las temperaturas mayores del promedio
    return [temp for temp in semana if temp > promedio]
        
def validar_temperatura_bajo_valor(temperatura, valor):
    # Validamos que la temperatura sea menor que el valor dado
    if temperatura < valor:
        print(f"La temperatura {temperatura:.2f} grados Celsius es menor que el valor de {valor:.2f} grados Celsius.")

def validar_temperatura_sobre_valor(temperatura, valor):
    # Validamos que la temperatura sea mayor que el valor dado
    if temperatura > valor:
        print(f"La temperatura {temperatura:.2f} grados Celsius es mayor que el valor de {valor:.2f} grados Celsius.")

def dia_de_la_semana(dia):
    # Colocamos el día de la semana
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return dias[dia] if 0 <= dia <= 6 else None

def main():
    temperaturas = []
    valor_maxima = 40.0
    valor_minima = 0.0

    for i in range(7):
        while True:
            nombre_dia = dia_de_la_semana(i)
            temperatura = obtener_temperatura(nombre_dia)
            if temperatura is not None:
                # Validar si la temperatura supera el valor dado
                validar_temperatura_sobre_valor(temperatura, valor_alerta_maxima)
                validar_temperatura_bajo_valor(temperatura, valor_alerta_minima)
                temperaturas.append(temperatura)
                break
            
    # Calculando el promedio
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio de la semana es: {promedio:.2f} grados Celsius")
    
    # Encontrando el máximo y mínimo de la semana
    maximo, minimo, indice_maximo, indice_minimo = encontrar_max_min(temperaturas)
    nombre_dia_maximo = dia_de_la_semana(indice_maximo)
    nombre_dia_minimo = dia_de_la_semana(indice_minimo)     
    print(f"La temperatura máxima de la semana es: {maximo:.2f} grados Celsius (día {nombre_dia_maximo})")
    print(f"La temperatura mínima de la semana es: {minimo:.2f} grados Celsius (día {nombre_dia_minimo})")
    
    # Encontrando las temperaturas por encima del promedio
    temperaturas_sobre_promedio = encontrar_temperaturas_por_sobre_el_promedio(temperaturas, promedio)  
    print(f"Las temperaturas por encima del promedio son: {temperaturas_sobre_promedio}")
    
   (main)