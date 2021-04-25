a = input("Bir sayı giriniz:").strip()
if a.isdigit():
  x = int(a)
  b = list(str(a))
  #print(b)
  d = len(b)
  c = 0
  for i in b:
    c = c + (pow(int(i),d))
  if c==x:
      print(a,"sayısı Armstrong sayısıdır.")
  else:
      print(a,"sayısı Armstrong sayısı değildir!!!")
else:
 print ("lütfen uygun formatta giriniz!!")