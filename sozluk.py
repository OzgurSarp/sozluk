miimler = {
    "LOL": "komik birşeye verilen cevap",
    "NAH": "asla demek",
}
kelime = input("anlamadığın bir kelime yaz (hepsi büyük harflerle): ")

if kelime in miimler.keys():
    print(miimler[kelime])
else:
    print("kelimeniz eşleşmiyor.")
