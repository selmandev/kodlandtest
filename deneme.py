plate_num_dict = {
    "1" : "Adana",
    "26" : "Eskişehir",
    "34" : "İstanbul",
    "24" : "Erzurum",
    "81" : "Düzce"
    }

word = input("Anlamını Bilmediğiniz bir kelime yazın (büyük harfle)")

if word in plate_num_dict.keys():
    print("plaka ili:", plate_num_dict.get(word))
else:
    print("1 ile 81 arasında bir sayı gir.")
