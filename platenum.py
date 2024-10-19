plate_num_dict = {
    "ADANA" : "01",
    "ADIYAMAN" : "02",
    "AFYON" : "03",
    "AĞRI" : "04",
    "AMASYA" : "05",
    "ANKARA" : "06",
    "ANTALYA" : "07",
    "ARTVİN" : "08",
    "AYDIN" : "09",
    "BALIKESİR" : "10",
    "BİLECİK" : "11",
    "BİNGÖL" : "12",
    "BİTLİS" : "13",
    "BOLU" : "14",
    "BURDUR" : "15",
    "BURSA" : "16",
    "ÇANAKKALE" : "17",
    "ÇANKIRI" : "18",
    "ÇORUM" : "19",
    "DENİZLİ" : "20",
    "ERZİNCAN" : "24",
    "ERZURUM" : "25",
    "ESKİŞEHİR" : "26",
    "İSTANBUL" : "34",
    "DÜZCE" : "81"
    }

word = input("Hepsi büyük harfli bir il ismi girin.")

if word in plate_num_dict.keys():
    print("il plakası:", plate_num_dict.get(word))
else:
    print("Geçerli bir il giriniz.")
