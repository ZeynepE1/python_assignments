a = input("Bir sayı giriniz:").strip()
if a.isdigit():
    b=int(a)
    if b >= 2:
        if b ==2:
            print("sayı asal")
        else:
         for i in range(2,b):
            if b % i == 0:
                 print("sayı asal değildir")
                 break
            else:
                 print("sayı asaldır.")
                 break         
    else:
      print("2'den büyük sayı giriniz!!")
else:
  print("harf girme")