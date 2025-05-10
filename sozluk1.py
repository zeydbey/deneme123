liste = {
            "KALEM": "Yazmaya yarayan araç ",
            "BLUETOOTH": "Belirli bir uzaklıktan temassız şekilde bağlanmaya yarayan frekans sistemi",
            "MOUSE": "Türkçe anlamı faredir bilgisayarlara bağlanan imleci hareket ettirmeye yarayan araç"
            }




for i in range(2):

    a = input("Anlamını bilmediğiniz kelimeyi giriniz: ")
    
    if a in liste.keys():
        print(liste[a])
    
    else:
        print("Böyle bir sözcük yok ..")
