import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Hata: Sıfıra bölünemez!"
    return a / b

def percentage(a, b):
    return (a * b) / 100

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Hata: Negatif sayının karekökü alınamaz!"
    return math.sqrt(a)

def main():
    print("Hesap Makinesine Hoş Geldiniz!")
    print("Yapmak istediğiniz işlemi seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Yüzde")
    print("6. Üs alma")
    print("7. Karekök alma")

    choice = input("Seçiminiz (1/2/3/4/5/6/7): ")

    if choice in ['1', '2', '3', '4', '5', '6']:
        a = float(input("Birinci sayıyı girin: "))
        b = float(input("İkinci sayıyı girin: "))
        
        if choice == '1':
            print("Sonuç:", add(a, b))
        elif choice == '2':
            print("Sonuç:", subtract(a, b))
        elif choice == '3':
            print("Sonuç:", multiply(a, b))
        elif choice == '4':
            print("Sonuç:", divide(a, b))
        elif choice == '5':
            print(f"{a}'nin %{b} = {percentage(b, a)}")
        elif choice == '6':
            print(f"{a} ^ {b} = {power(a, b)}")

    elif choice == '7':
        a = float(input("Karekökü alınacak sayıyı girin: "))
        print("Sonuç:", square_root(a))

    else:
        print("Geçersiz seçim!")

main()
