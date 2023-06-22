megabyte = int(input("Ingrese la cantidad de megabytes a convertir: "))

bits = megabyte * 8388608
bytes = megabyte * 1048576 
kb = megabyte * 1024 
GB = 0.000976563 * megabyte

print(megabyte, "megabyte", " es igual a ", bits, " bits " )
print(megabyte, "megabyte", " es igual a ", bytes, " bytes " )
print(megabyte, "megabyte", " es igual a ", kb, " kb " )
print(megabyte, "megabyte", " es igual a ", GB, " GB " )

