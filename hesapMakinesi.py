number1 = int(input("Birinci sayıyı giriniz:"))
number2 = int(input("İkinci sayıyı giriniz:"))
islem = str(input("Yapılacak işlemi giriniz:"))


def hesap_makinesi(number1,number2,islem):
    if islem == "+":
        print(f"İşlem sonucu: {number1 + number2}")
    elif islem == "-":
        print(f"İşlem sonucu: {number1 - number2}")
    elif islem == "/":
        if number2 == 0:
            print("Bölme işlemi için ikinci sayı 0 olamaz!")
            return 
        print(f"İşlem sonucu: {number1 / number2}")
    elif islem == "*":
        print(f"İşlem sonucu: {number1 * number2}")
    else:
        print("Geçersiz işlem türü!")

hesap_makinesi(number1,number2,islem)