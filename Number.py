def son():
  start = input("Boshlash uchun (1), to'xtatish uchun (0) ni kiriting: ")
  while start:
    qiymat = int(input("Iltimos son kirirting: "))
    if qiymat == 0:
      break
    for son in range(1, qiymat+1):
      for i in range(1, son):
        print(i, end = "")
      print(son, end = "")
      for i in range(1, son):
        print((son - i), end = "")
      print("")
son()