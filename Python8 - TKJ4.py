list_kosong = []
list_interger = [1, 2, 3, 10 ,100, 250]
list_string = ["naufal", "abyan", "icak", "jamil"]
list_mix = [20, "arya", True, "prasetyo"]

print("Data sebelum diubah:", list_string)
list_string[0] =  "fathuddin"
print("Data setelah diubah:", list_string)

print("Data sebelum diubah:", list_string)
list_string[1] = "rendra"
print("Data setelah diubah:", list_string)

print("Data sebelum diubah:", list_mix)
list_mix[0] = "desta"
print("Data setelah diubah:", list_mix)

print("Data sebelum diubah:", list_mix)
list_mix[1] = "wicaksono"
print("Data setelah diubah:", list_mix)

print("Data sebelum diubah:", list_mix)
list_mix[2] = "false"
print("Data setelah diubah:", list_mix)

print("Data sebelum diubah:", list_mix)
list_mix[3] = "akmal"
print("Data setelah diubah:", list_mix)

for i in list_string:
    print(i)

print("\n")
for a in list_interger:
      print(a)

print("\n")
for x in list_mix:
    print(x)


    
