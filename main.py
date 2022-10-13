# import csv library
import csv

# read file data
with open('arquivo_dados.txt', 'r') as file:
    data = file.read()

# write data to a csv file
with open('arquivo_dados.csv', 'w') as file:
    file.write(data)

"""
open csv file with "," delimiter and create
another csv file with ";" delimiter
"""
with open('arquivo_dados.csv') as arquivo_dados, \
     open('resultado.csv', 'w') as resultado:

    datareader = csv.reader(arquivo_dados, delimiter=',')
    csvwriter = csv.writer(resultado, delimiter=';')
    csvwriter.writerows(datareader)

# read csv file lines with ";" delimiter
with open('resultado.csv', 'r') as file:
    result = file.readlines()
    result = result[:-1] # removes last line, which is empty

# write result to txt file
with open('resultado.txt', 'w') as file:
    file.writelines(result)
