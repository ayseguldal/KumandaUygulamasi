import random
import time

class Kumanda():
    def __init__(self,tv_durumu="KAPALI",tv_ses=0,tum_kanallar=["Trt"] , kanal="Trt"):
        self.tv_durumu=tv_durumu
        self.tv_ses=tv_ses
        self.tum_kanallar=tum_kanallar
        self.kanal=kanal

    def tv_ac(self):
        if(self.tv_durumu=="AÇIK"):
            print("TELEVİZYON ZATEN AÇIK \n")

        else:
            print("TELEVİZYON AÇILIYOR... \n")
            self.tv_durumu="AÇIK"

    def tv_kapat(self):
        if(self.tv_durumu=="KAPALI"):
            print("TELEVİZYON ZATEN KAPALI \n")
        else:
            print("TELEVİZYON KAPATILIYOR...\n")
            self.tv_durumu="KAPALI"

    def ses_ayarları(self):
        while True:
            işlem=input("Sesi Azalt:'<'\nSesi Arttır:'>' ")

            if(işlem=="<"):
                if(self.tv_ses==0):
                    print("SES TAMAMEN KAPALI. \n")
                else:
                    self.tv_ses -=1
                    print("SES KISILIYOR... \n Ses: ",self.tv_ses)

            elif(işlem==">"):
                if(self.tv_ses==30):
                    print("SES TAMAMEN AÇIK")
                else:
                    self.tv_ses +=1
                    print("SES AÇILIYOR... \n Ses:",self.tv_ses)

            else:
                print("SES GÜNCELLENDİ...")
                break

    def kanal_ekle(self,kanal_ismi):
        print("KANAL EKLENDİ...\n")
        time.sleep(1)
        self.tum_kanallar.append(kanal_ismi)

    def __len__(self):
        return len(self.tum_kanallar)

    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.tum_kanallar)-1)

        self.kanal=self.tum_kanallar[rastgele]

        print("Şu anki Kanal:",self.kanal)


    def __str__(self):
        return "TV DURUMU:{}\nTV SES:{}\nKANAL LİSTESİ:{}\nŞU ANKİ KANAL:{}".format(self.tv_durumu,self.tv_ses,self.tum_kanallar,self.kanal)


kumanda=Kumanda()


print("""TELEVİZYON UYGULAMASI
1.TV Aç
2.TV Kapat
3.Ses Ayarları
4.Kanal Ekle
5.Kanal Sayısını Öğrenme
6.Rastgele Kanal Seçme
7.TV Bilgileri

ÇIKMAK İSTİYORSANIZ 'q' YA BASINIZ...
""")


while True:
    işlem=input("\nYAPACAĞINIZ İŞLEMİ SEÇİNİZ:")

    if(işlem=="q"):
        print("PROGRAM KAPATILIYOR...")
        break
    elif(işlem == "1"):
        kumanda.tv_ac()
    elif(işlem == "2"):
        kumanda.tv_kapat()
    elif(işlem == "3"):
        kumanda.ses_ayarları()

    elif(işlem == "4"):
        eklenen_isimleri=input("Kanal İsimlerini , ile Ayırarak Giriniz:")
        tum_kanallar=eklenen_isimleri.split(",")
        for eklenecekler in tum_kanallar:
            kumanda.kanal_ekle(eklenecekler)

    elif(işlem =="5"):
        print("Kanal Sayısı:",kumanda.__len__())

    elif(işlem =="6"):
        kumanda.rastgele_kanal()

    elif(işlem=="7"):
       print(kumanda)
    else:
        print("GEÇERSİZ İŞLEM!\n")





