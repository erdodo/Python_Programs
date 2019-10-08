print("Vize Notunu Giriniz : ")
vize=input()
vize=float(vize)
print("Final Notunu Giriniz : ")
final=input()
final=float(final)
if(final>100 or vize>100):
    print("Girilen Not 100'den Fazla Olamamaz")
else:
    ort=(vize*0.4)+final*0.6
    if(final<50):
        print("Finalden Kaldınız")
        ort = str(ort)
        print("Ortalamanız : " + ort)
    elif(ort<50):
        print("Ortalamadan Kaldınız")
        ort = str(ort)
        print("Ortalamanız : " + ort)
    else:
        print("Tebrikler Geçtiniz")
        ort = str(ort)
        print("Ortalamanız : " + ort)