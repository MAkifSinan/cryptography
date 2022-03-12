import string

cikti=("")
all_letters = string.ascii_letters
def harf_sirasi_bulma(x):
    if x in all_letters:
        print("x is here")
        for i in range(0,len(all_letters)):
            if x==all_letters[i]:
                print("x in sırası = {}".format(i))
                sayinin_yeri=i
    else:
        print("harf bulunmamakta")
    return sayinin_yeri+1

def key_1(a,b,x):
    y=(a*x)+b

    return y


#

girilen_metin = input("affine şifreleme için metin giriniz:\n")
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
    x = harf_sirasi_bulma(j)
    # print("******************")
    k = all_letters[int(key_1(a, b, x))]
    print(f"cıktı::{k}")
    cikti = cikti + k
    # print(k)
    print("*****************")
print("------------------------")
print(cikti)