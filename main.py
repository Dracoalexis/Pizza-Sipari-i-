# Bir pizza sipariş sistemi yazmanız isteniyor. Kullanıcıdan pizza boyutu, içindekiler ve ekstraları seçmesi isteniyor. Sipariş tamamlandığında,
# kullanıcıya toplam tutarı gösteriliyor. Sizden istenen, bu pizza sipariş sistemini Python dilinde yazmanız.

print("""Pizzacıya hoşgeldiniz! Menümüz aşağıda belirtilmiştir.

    Pizza Çeşitleri:
    1- Kaşarlı Pizza = 30
    2- Bol Malzemos Pizza = 60
    3- Vegan Pizza = 50
    4- Sosis Salam Pizza = 40
    
    Pizza Boyutları:
    1- Küçük Boy Pizza = 40
    2- Orta Boy Pizza = 50
    3- Büyük Boy Pizza = 60

    Extralar: 
    1- Dondurma = 20
    2- Patates Kızartması = 30
    3- Kola = 20
    4- Meyve Suyu = 15
    5- Ayran = 10
    6- Milkshake = 20

""")

def boyut_alma(bakiye):

    boyut = input("Pizzanızın boyutunun numarasını giriniz.")

    if boyut == "1":
        bakiye += 40

    elif boyut == "2":
        bakiye += 50

    elif boyut == "3":
        bakiye += 60

    else:
        print("Geçersiz numara girdiniz.")
        return boyut_alma()

    return bakiye

def extralar(bakiye):

    while True:
        extra = input("Extra eklemek istediğiniz ürünün numarasını giriniz. Çıkmak için q'ya basınız.")

        if extra == "1":
            bakiye += 20

        elif extra == "2":
            bakiye += 30

        elif extra == "3":
            bakiye += 20

        elif extra == "4":
            bakiye += 15

        elif extra == "5":
            bakiye += 10

        elif extra == "6":
            bakiye += 20

        elif extra == "Q" or extra == "q":
            break

        else:
            print()
            print("Geçersiz numara girdiniz.")
            print()

    return bakiye



def main():
    bakiye = 0

    çeşit = input("Seçtiğiniz pizza çeşidinin numarasını giriniz.")

    if çeşit == "1":
        bakiye += 30
        print()
        a = boyut_alma(bakiye)
        print()
        b = extralar(a)
        print()
        print("Borcunuz şu kadardır: {}".format(b))

    elif çeşit == "2":
        bakiye += 60
        print()
        a = boyut_alma(bakiye)
        print()
        b = extralar(a)
        print()
        print("Borcunuz şu kadardır: {}".format(b))

    elif çeşit == "3":
        bakiye += 50
        print()
        a = boyut_alma(bakiye)
        print()
        b = extralar(a)
        print()
        print("Borcunuz şu kadardır: {}".format(b))

    elif çeşit == "4":
        bakiye += 40
        print()
        a = boyut_alma(bakiye)
        print()
        b = extralar(a)
        print()
        print("Borcunuz şu kadardır: {}".format(b))

    else:
        print("Yanlış numara girdiniz.")
        return main()

main()