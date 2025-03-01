number = int(input("Asal sayı olup olmadığı hesaplanacak sayıyı giriniz:"))

def asal_mi(number):
    counter = 0
    for i in range(2,number):
        if number % i == 0:
            counter += 1
            i += 1
       
    if counter == 0:
        return f"{number} sayısı asal bir sayıdır."
    else:
        return f"{number} sayısı asal bir sayı değildir."

print(asal_mi(number))


