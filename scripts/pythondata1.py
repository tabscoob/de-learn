import csv
# este funcion imprime un numero

# def propiedad_variable_integer(valor_numerico):
#     return print("el valor numerico es:",valor_numerico)

# propiedad_variable_integer(20)
with open('/Users/julio.mendez/Downloads/de-learn01.csv') as csv_file:
    resultado = csv.reader(csv_file, delimiter=',')
    line_count = 0
    total_edades=0
    for row in resultado:
        if  line_count == 0:
             print(f'los nombres de las columnas son  {", ".join(row)}')
             line_count += 1
            
        else:
            line_count += 1
            print(f"{row[0]} tiene {row[3]} años y nacio en {row[5]}")
            #sumar las edades para obtener el total combinado de edades
            total_edades+=int(row[3])
            
    print(f"el total de las edades:",total_edades)


        
        



# print(resultado)
# line_count = 0


    # if line_count == 0:
    #     print(f'Column names are {", ".join(row)}')
    #     line_count += 1
    # line_count += 1
# print(f'Processed {line_count} lines.')








