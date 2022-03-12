print("şifreleme  yada  deşifreleme ? \n"
      "şifreleme 1\n"
      "deşifreleme 2\n")

secim=int(input("seçiminiz ?\n"))
cıktı=("")
def key_1(a,b,x):
    y=(a*x)+b

    return y
def key_2(a,b,x):
    y=(x-b)/(a+1)
    return y
if secim==1:
    girilen_metin = input("affine şifreleme için metin giriniz:\n")
    girilen_metin.encode('UTF-8')
    anahtar_ilk_input = input("affine şifreleme için a değeri giriniz\n")
    print("a inputu =" + anahtar_ilk_input)
    anahtar_ikinci_input = input("affine şifreleme için b değeri giriniz\n")
    print("b inputu =" + anahtar_ikinci_input)
    a = int(anahtar_ilk_input)
    b = int(anahtar_ikinci_input)
    metin_uzunlugu = len(girilen_metin)
    for i in range(0, metin_uzunlugu):
        # print(ord(girilen_metin[i]))
        j = girilen_metin[i]
        print(j)
        print(ord(j))

        print(chr(ord(j)))
        x = int(ord(j) - 96)
        # print("******************")
        # print(x)
        # print(key(a,b,x))
        k=chr(abs((int(key_1(a,b,x)))+96))

        print(k.isascii())
        print(type(k))
        print(" k ascii karşılığı {} ".format(ord(k)))
        cıktı = cıktı + k
        # print(k)
        print("*****************")
    print("------------------------")
    print(cıktı)
elif secim==2:
    girilen_metin = input("affine deşifreleme için metin giriniz:\n")
    girilen_metin.encode('UTF-8')
    anahtar_ilk_input = input("affine deşifreleme için a değeri giriniz\n")
    print("a inputu =" + anahtar_ilk_input)
    anahtar_ikinci_input = input("affine deşifreleme için b değeri giriniz\n")
    print("b inputu =" + anahtar_ikinci_input)
    a = int(anahtar_ilk_input)
    b = int(anahtar_ikinci_input)
    metin_uzunlugu = len(girilen_metin)
    for i in range(0, metin_uzunlugu):
        # print(ord(girilen_metin[i]))
        j = girilen_metin[i]
        print(j)
        print(ord(j))

        print(chr(ord(j)))
        x = int(ord(j) - 96)
        # print("******************")
        # print(x)
        # print(key(a,b,x))

        k = chr(abs((int(key_2(a, b, x))) + 97))
        print(k.isascii())
        #print(type(k))
        print(" k ascii karşılığı {} ".format(ord(k)))
        cıktı = cıktı + k
        # print(k)
        print("*****************")
    print("------------------------")
    print(cıktı)
else:
    print("hatalı seçim")

