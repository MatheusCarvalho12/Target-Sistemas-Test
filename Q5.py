def inverter_string(string):
    # Convertendo a string para uma lista de caracteres
    caracteres = list(string)
    
    # Obtendo o tamanho da string
    tamanho = len(caracteres)
    
    # Invertendo os caracteres
    for i in range(tamanho // 2):
        caracteres[i], caracteres[tamanho - i - 1] = caracteres[tamanho - i - 1], caracteres[i]
    
    # Convertendo a lista de caracteres de volta para uma string
    string_invertida = ''.join(caracteres)
    
    return string_invertida

texto = input("Digite qualquer coisa: ")
texto_invertido = inverter_string(texto)
print("Invertida:", texto_invertido)
