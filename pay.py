def pay():
  start = int(input("O'yin o'ynashni hohlaysizmi? Ha (1) yoki Yo'q (0): "))
  if start == 1:
    print("1 - o'yin, sonlarni so'zga aylantirib beradi")
    print("2 - o'yin, sonlarni so'zga aylantirib beradi (pro) :)")
    print("3 - o'yin, berilgan songacha bo'lgan harbir raqamgacha yozip so'ng 1 ga qaytadi")
    while True:
      start = int(input("(To'xtatgani '0' ni kiriting) Boshlagani o'yin raqamini kiriting: "))
      if start == 1:
        import son_soz
      elif start == 2:
        import son_soz2

      elif start == 2:
        import son
  
pay() 