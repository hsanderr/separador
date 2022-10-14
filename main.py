"""
Henrique Sander Lourenco
This code replace commas in arquivo_dados.txt with semicolons
and saves it to resultado.txt
"""

# read arquivo_dados.txt file
with open('arquivo_dados.txt', 'r') as file:
    # get file data as string
    string = file.read()
    
    # cast string to list, for strings are immutable
    lista = list(string)

    # variable to check if comma is between quotation marks
    numAspas = 0

    # loop through list elements
    for i, char in enumerate(lista):

        # if char is a quotation mark and previous one isn't a backslash,
        # increment numAspas
        if char == '"' and lista[i - 1] != "\\":
            numAspas += 1

        # if numAspas is even, char isn't between quotation marks    
        if numAspas % 2 == 0:
            if char == ",":
                lista[i] = ";"

# join list items into a string 
resultado = ''.join(lista)

# write results to resultado.txt
with open('resultado.txt', 'w') as file:
    file.write(resultado)