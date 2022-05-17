def son_soz2(num):
    birlik = ["", "bir ", "ikki ", "uch ", "to'rt ", "besh ", "olti ", "yetti ", "sakkiz ", "to'qqiz "]
    onlik = ["", "o'n ", "yigirma ", "o'ttiz ", "qirq ", "ellik ", "oltimish ", "yetmish ",
        "sakson ", "to'qson "]
    if num < 0:
      return "minus" + son_soz2(-num) 
      
    if num < 10:
      return birlik[num]
      
    if num < 100:
      return onlik[num // 10] + birlik[int(num % 10)]
      
    if num < 1000:
      return birlik[num // 100] + "yuz " + son_soz2(int(num % 100))
      
    if num < 1000000:
      return son_soz2(num // 1000) + "ming " + son_soz2(int(num % 1000))

    if num < 1000000000:
      return son_soz2(num // 1000000) + "million " + son_soz2(int(num % 1000000))
      
    return son_soz2(num // 1000000000) + "milliartd" + son_soz2(int(num % 1000000000)) 
  
a = int(input("Boshlash uchun uchun (1), to'xtatish uchun (0) ni kiriting: "))
while a:
  son = int(input("Iltimos son kiriting: "))
  if son == 0:
    break
  print(son_soz2(son))
