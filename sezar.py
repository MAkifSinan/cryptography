print("şifreleme  yada  deşifreleme ? \n"
      "şifreleme 1\n"
      "deşifreleme 2\n")

secim=int(input("seçiminiz ?\n"))
if secim==1:
    girilen_metin=input("sezar şifreleme için metin giriniz:")
    metin_uzunlugu=len(girilen_metin)
    cıktı=("")
    anahtar=5
    print(girilen_metin)
    #print(metin_uzunlugu)
    #print("girilen metin tipi ={}".format(type(girilen_metin)))
    #print(girilen_metin)
    for i in range(0,metin_uzunlugu):
        #print(ord(girilen_metin[i]))
        j=girilen_metin[i]
        #print(j)
        #print(ord(j))
        #print(chr(ord(j)))
        k=chr(ord(j) + anahtar)
        #print(" k veri tipi {} ".format(type(k)))
        cıktı=cıktı + k
        #print(k)
        #print("*****************")
    print("------------------------")
    print(cıktı)

elif secim==2:
    girilen_metin=input("sezar deşifreleme için metin giriniz:")
    metin_uzunlugu=len(girilen_metin)
    cıktı=("")
    anahtar=5
    print(girilen_metin)
    #print(metin_uzunlugu)
    #print("girilen metin tipi ={}".format(type(girilen_metin)))
    #print(girilen_metin)
    for i in range(0,metin_uzunlugu):
        #print(ord(girilen_metin[i]))
        j=girilen_metin[i]
        #print(j)
        #print(ord(j))
        #print(chr(ord(j)))
        k=chr(ord(j) - anahtar)
        #print(" k veri tipi {} ".format(type(k)))
        cıktı=cıktı + k
        #print(k)
        #print("*****************")
    print("------------------------")
    print(cıktı)
else:
    print("hatalı seçim")