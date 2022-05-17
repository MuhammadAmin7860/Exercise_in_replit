def son_soz():
  a = int(input("Boshlash uchun uchun (1), to'xtatish uchun (0) ni kiriting: "))
  while a:
    birlik = ["nol", "bir", "ikki", "uch", "to'rt", "besh", "olti", "yetti", "sakkiz", "to'qqiz"]
    onlik = ["", "o'n", "yigirma", "o'ttiz", "qirq", "ellik", "oltimish", "yetmish",
        "sakson", "to'qson"]
    yuzlik = "yuz"
    minglik = "ming"
    millionlik = "million"
    son = list(input("Iltimos son kiriting: "))
    nomi = []
    for i in range(1, len(son) + 1):
        raqam = int(son[-i])
        if i == 1 and 0 == raqam and len(son) == 1:
            nomi.append(birlik[raqam])
            a = False
        if i == 1 and 0 < raqam:
            nomi.append(birlik[raqam])
        if i == 2 and 0 < raqam:
            nomi.append(onlik[raqam])
        if i == 3 and 0 < raqam:
            nomi.append(yuzlik)
            nomi.append(birlik[raqam])
        if i == 4 and 0 < raqam:
            nomi.append(minglik)
            nomi.append(birlik[raqam])
        if i == 5 and 0 < raqam: 
            if int(son[-4]) == 0:
                nomi.append(minglik)
            nomi.append(onlik[raqam])       
        if i == 6 and 0 < raqam:
            if int(son[i-5]) == 0:
                nomi.append(minglik)
                nomi.append(yuzlik)
            if len(son) == 7 and int(son[-5]) == 0:
                nomi.append(minglik)
            if int(son[i-5]) != 0:
                nomi.append(yuzlik)
                nomi.append(birlik[raqam])
        if i == 7 and 0 < raqam:
            nomi.append(millionlik)
            nomi.append(birlik[raqam])
    for i in range(1, len(nomi) + 1):
        print(nomi[-i],"", end="")
    print("\n")
son_soz()