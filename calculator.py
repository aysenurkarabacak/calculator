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

def main():
    print("Hesap Makinesine Hoş Geldiniz!")
    
    print("Yapmak istediğiniz işlemi seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

    choice = input("Seçiminiz (1/2/3/4): ")

    if choice not in ('1', '2', '3', '4'):
        print("Geçersiz seçim.")
        return

    try:
        num1 = float(input("Birinci sayıyı girin: "))
        num2 = float(input("İkinci sayıyı girin: "))
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        return

    if choice == '1':
        print("Sonuç:", add(num1, num2))
    elif choice == '2':
        print("Sonuç:", subtract(num1, num2))
    elif choice == '3':
        print("Sonuç:", multiply(num1, num2))
    elif choice == '4':
        print("Sonuç:", divide(num1, num2))

if __name__ == "__main__":
    main()
