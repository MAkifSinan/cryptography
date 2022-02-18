import googletrans

def anlamli_sozcuk_arama(arananmetin):
    cevirmen = googletrans.Translator()
    dil=cevirmen.detect(arananmetin)
    diltespiti=dil.lang
    print(diltespiti)

    return diltespiti

text="ug|ctškhtgngog{øpvgok"  #deneme amaçlı bir metindir.
ciktilar=['']

girilen_metin=input("sezar şifreleme çözümü istenen metini giriniz:")
metin_uzunlugu=len(girilen_metin)
cikti=("")

print(girilen_metin)
print(metin_uzunlugu)
for u in range(0,25):
    anahtar=u
    for i in range(0,metin_uzunlugu):
        #print(ord(girilen_metin[i]))                   #bu aşamadaki kodlar harf boyutunda değişimi gözlemlemek için kullanılmış kodlardır.
        j=girilen_metin[i]                              #i . nci indeksteki harf j değişkenine eşlenir
        #print(j)
        #print(ord(j))                                  #bu satırlarda j değeri içine atılmış harflerin ascii karşılığını görebilirsiniz
        #print(chr(ord(j)))
        k=chr(ord(j) - anahtar)                         #harfin ascii karşılığına ekleme veya cıkartma yapılarak harf değiştirilmiş - kaydırılmış olur
        #print(" k veri tipi {} ".format(type(k)))
        cikti=cikti + k                                 # harfler toplanarak yeniden sözcük - metin haline getirilir.
        #print("*****************")
        #print(cıktı)
        if len(cikti)>(int(metin_uzunlugu)-1):
            print(cikti)
            ciktilar.append(cikti)
            cikti = ("")                                #butun i değerleri için kod çalışacagından dolayı butun harfler değiştirildiğinde ciktilar listesine yazılır ve cikti değişkeninin içi silinir

    print("------------------------\n")

#print(cıktı)
print("------------------------\n")
print(ciktilar)
ciktisayisi= len(ciktilar)
print(" çıktı sayısı ={}".format(ciktisayisi))
print("***************************************************")
for i in range(1,len(ciktilar)):
    print("kod burada")
    tespitedilen_dil=anlamli_sozcuk_arama(ciktilar[i])
    if tespitedilen_dil=='tr':
        cozulmus_metin=ciktilar[i]
        print("{} metninin çözülmüş hali {} dir".format(girilen_metin,cozulmus_metin))
        exit()
    else:
        print("şifre çözümü başarısızdır")