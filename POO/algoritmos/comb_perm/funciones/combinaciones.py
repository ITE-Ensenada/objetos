def combinaciones(elementos, r):
    resultados = []
    combinacion_actual = [0] * r
    combina_recursivo(elementos, resultados, combinacion_actual, 0, 0, r)
    return resultados

def combina_recursivo(elementos, resultados, combinacion_actual, indice_elemento, indice_combinacion, r):
    if indice_combinacion == r:
        resultados.append(combinacion_actual.copy())
        return
    
    if indice_elemento >= len(elementos):
        return
    
    combinacion_actual[indice_combinacion] = elementos[indice_elemento]
    combina_recursivo(elementos, resultados, combinacion_actual, indice_elemento + 1, indice_combinacion + 1, r)
    combina_recursivo(elementos, resultados, combinacion_actual, indice_elemento + 1, indice_combinacion, r)

