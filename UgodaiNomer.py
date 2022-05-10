print("Загадайте число от 1 до 100 и я его отгадаю за 8 ходов (писать 'да' или 'нет')")
ans1 = input("Это число больше 50?")
if ans1 == "да":
  ans2 = input("Это число больше 75?")
  if ans2 == "да":
    ans3 = input("Это число больше 87?")
    if ans3 == "да":
      ans4 = input("Это число больше 95?")
      if ans4 == "да":
        ans5 = input("Это число больше 98?")
        if ans5 == "да":
          ans6 = input("Это число 99?")
          if ans6 == "да":
            print("Это 99")
          elif ans6 == "нет":
            ans7 = input("Это число 100?")
            if ans7 == "да":
              print("Это 100")
        elif ans5 == "нет":
          ans6 = input("Это число 96?")
          if ans6 == "да":
            print("Это 96")
          elif ans6 == "нет":
            ans7 = input("Это число 97?")
            if ans7 == "да":
              print("Это 97")
            else:
              print("Это 98")
      elif ans4 == "нет":
        ans5 = input("Это число больше 91?")
        if ans5 == "да":
          ans6 = input("Это число больше 93?")
          if ans6 == "да":
            ans7 = input("Это число 94?")
            if ans7 == "да":
              print("Это 94")
            elif ans7 == "нет":
              print("Это 95")
          if ans6 == "нет":
            ans7 = input("Это число 92?")
            if ans7 == "да":
              print("Это 92")
            else:
              print("Это 93")
        if ans5 == "нет":
          ans6 = input("Это число больше 89?")
          if ans6 == "да":
            ans7 = input("Это число 90?")
            if ans7 == "да":
              print("Это 90")
            elif ans7 == "нет":
              print("это 91")
          if ans6 == "нет":
            ans7 = input("Это число 88?")
            if ans7 == "да":
              print("Это 88")
            elif ans7 == "нет":
              print("Это 89")
    elif ans3 == "нет":
      ans4 = input("Это число больше 81?")
      if ans4 == "да":
        ans5 = input("Это число больше 84?")
        if ans5 == "да":
          ans6 = input("Это 85?")
          if ans6 == "да":
            print("Это 85")
          if ans6 == "нет":
            ans7 = input("Это 86?")
            if ans7 == "да":
              print("Это 86")
            else:
              print("Это 85")
        if ans5 == "нет":
          ans6 = input("Это число больше 83?")
          if ans6 == "да":
            print("Это 84")
          if ans6 == "нет":
            ans7 = input("Это 82?")
            if ans7 == "да":
              print("Это 82")
            else:
              print("Это 83")
      elif ans4 == "нет":
        ans5 = input("Это число больше 78?")
        if ans5 == "да":
          ans6 = input("Это число больше 80?")
          if ans6 == "да":
            print("Это 81")
          else:
            print("Это 79")
        elif ans5 == "нет":
          ans6 = input("Это число больше 76?")
          if ans6 == "да":
            print("Это 77")
          elif ans6 == "нет":
            ans7 = input("Это 75?")
            if ans7 == "да":
              print("Это 75")
            else:
              print("Это 76")
  elif ans2 == "нет":
    ans3 = input("Это число больше 63?")
    if ans3 == "да":
      ans4 = input("Это число больше 69?")
      if ans4 ==  "да":
        ans5 = input("Это число больше 72?")
        if ans5 == "да":
          ans6 = input("Это число больше 73?")
          if ans6 == "да":
            print("Это 74")
          else:
            print("Это 73")
        elif ans5 == "нет":
          ans6 = input("Это число больше 70?")
          if ans6 == "да":
            ans7 = input("Это 72?")
            if ans7 == "да":
              print("Это 72")
            else:
              print("Это 71")
          elif ans6 == "нет":
            ans7 = input("Это 69?")
            if ans7 == "да":
              print("Это 69")
            else:
              print("Это 70")
      elif ans4 == "нет":
        ans5 = input("Это число больше 66?")
        if ans5 == "да":
          ans6 = input("Это 67?")
          if ans6 =="да":
            print("Это 67")
          else:
            print("Это 68")
        elif ans5 == "нет":
          ans6 = input("Это число больше 64?")
          if ans6 == "да":
            ans7 = input("Это 65?")
            if ans7 == "да":
              print("Это 65")
            else:
              print("Это 66")
          elif ans6 == "нет":
            print("Это 64")
    elif ans3 == "нет":
      ans4 = input("Это число больше 57?")
      if ans4 == "да":
        ans5 = input("Это число больше 60?")
        if ans5 == "да":
          ans6 = input("Это число больше 62?")
          if ans6 ==  "да":
            print("Это 63")
          else:
            ans7 = input("Это 61?")
            if ans7 == "да":
              print("Это 61")
            else:
              print("Это 62")
        elif ans5 == "нет":
          ans6 = input("Это число больше 58?")
          if ans6 == "да":
            ans7 = input("Это 59?")
            if ans7 == "да":
              print("Это 59")
            else:
              print("Это 60")
          else:
            ans7 = input("Это 57?")
            if ans7 == "да":
              print("Это 57")
            else:
              print("Это 58")
      elif ans4 == "нет":
        ans5 = input("Это число больше 52?")
        if ans5 == "да":
          ans6 = input("Это число больше 54?")
          if ans6 == "да":
            ans7 = input("Это 55?")
            if ans7 == "да":
              print("Это 55")
            else:
              print("Это 56")
          else:
            ans7 = input("Это 53?")
            if ans7 == "нет":
              print("Это 53")
            else:
              print("Это 54")
        elif ans5 == "нет":
          ans6 = input("Это 51?")
          if ans6 == "да":
            print("Это 51")
          else:
            print("Это 52")   
elif ans1 == "нет":
  ans2 = input("Это число больше 25?")
  if ans2 == "да":
    ans3 = input("Это число больше 37?")
    if ans3 == "да":
      ans4 = input("Это число больше 44?")
      if ans4 == "да":
        ans5 = input("Это число больше 47?")
        if ans5 == "да":
          ans6 = input("Это число больше 49?")
          if ans6 == "да":
            print("Это 50")
          elif ans6 == "нет":
            ans7 = input("Это 48?")
            if ans7 == "да":
              print("Это 48")
            else:
              print("Это 49")
        elif ans5 == "нет":
          ans6 = input("Это число больше 45?")
          if ans6 == "да":
            ans7 = input("Это 46?")
            if ans7 == "да":
              print("Это 46")
            else:
              print("Это 47")
          elif ans6 == "нет":
            print("Это 45")
      elif ans4 == "нет":
        ans5 = input("Это число больше 41?")
        if ans5 == "да":
          ans6 = input("Это число больше 42?")
          if ans6 == "да":
            ans7 = input("Это 43?")
            if ans7 == "да":
              print("Это 43")
            else:
              print("Это 44")
          elif ans6 == "нет":
            print("Это 42")
        elif ans5 == "нет":
          ans6 = input("Это число больше 39?")
          if ans6 == "да":
            ans7 = input("Это 40?")
            if ans7 == "да":
              print("Это 40")
            else:
              print("Это 41")
          elif ans6 == "нет":
            ans7 = input("Это 38?")
            if ans7 == "да":
              print("Это 38")
            else:
              print("Это 39")
    elif ans3 == "нет":
      ans4 = input("Это число больше 31?")
      if ans4 == "да":
        ans5 = input("Это число больше 34?")
        if ans5 == "да":
          ans6 = input("Это число больше 36?")
          if ans6 == "да":
            print("Это 37")
          elif ans6 == "нет":
            ans7 = input("Это 35?")
            if ans7 == "да":
              print("Это 35")
            else:
              print("Это 36")
        elif ans5 == "нет":
          ans6 = input("Это число больше 32?")
          if ans6 == "да":
            ans7 = input("Это 33?")
            if ans7 == "да":
              print("Это 33")
            else:
              print("Это 34")
          elif ans6 == "нет":
            print("Это 32")
      elif ans4 == "нет":
        ans5 = input("Это число больше 28?")
        if ans5 == "да":
          ans6 = input("Это число больше 29?")
          if ans6 == "да": 
            ans7 = input("Это 30?")
            if ans7 == "да":
              print("Это 30")
            else:
              print("Это 31")
          elif ans6 == "нет":
            print("Это 29")
        elif ans5 == "нет":
          ans6 = input("Это число больше 26?")
          if ans6 == "да":
            ans7 = input("Это 27?")
            if ans7 == "да":
              print("Это 27")
            else:
              print("Это 28")
          elif ans6 == "нет":
            print("Это 26")
  elif ans2 == "нет":
    ans3 = input("Это число больше 13?")
    if ans3 == "да":
      ans4 = input("Это число больше 18?")
      if ans4 == "да":
        ans5 = input("Это число больше 22?")
        if ans5 == "да":
          ans6 = input("Это число больше 23?")
          if ans6 == "да":
            ans7 = input("Это 24?")
            if ans7 == "да":
              print("Это 24")
            else:
              print("Это 25")
          elif ans6 == "нет":
            print("Это 23")
        elif ans5 == "нет":
          ans6 = input("Это число больше 20?")
          if ans6 == "да":
            ans7 = input("Это 21?")
            if ans7 == "да":
              print("Это 21")
            else:
              print("Это 22")
          elif ans6 == "нет":
            ans7 = input("Это 19?")
            if ans7 == "да":
              print("Это 19")
            else:
              print("Это 20")
      elif ans4 == "нет":
        ans5 = input("Это число больше 15?")
        if ans5 == "да":
          ans6 = input("Это число больше 17?")
          if ans6 == "да":
            print("Это 18")
          elif ans6 == "нет":
            ans7 = input("Это 16?")
            if ans7 == "да":
              print("Это 16")
            else:
              print("Это 17")
        elif ans5 == "нет":
          ans6 = input("Это 14?")
          if ans6 == "да":
            print("Это 14")
          elif ans6 == "нет":
            print("Это 15")
    elif ans3 == "нет":
      ans4 = input("Это число больше 7?")
      if ans4 == "да":
        ans5 = input("Это число больше 10?")
        if ans5 == "да":
          ans6 = input("Это число больше 12?")
          if ans6 == "да":
            print("Это 13")
          elif ans6 == "нет":
            ans7 = input("Это 11?")
            if ans7 == "да":
              print("Это 11")
            else:
              print("Это 12")
        elif ans5 == "нет":
          ans6 = input("Это число больше 9?")
          if ans6 == "да":
            print("Это 10")
          elif ans6 == "нет":
            ans7 = input("Это 8?")
            if ans7 == "да":
              print("Это 8")
            else:
              print("Это 9")
      elif ans4 == "нет":
        ans5 = input("Это число больше 4?")
        if ans5 == "да":
          ans6 = input("Это число больше 6?")
          if ans6 == "да":
            print("Это 7")
          elif ans6 == "нет":
            ans7 = input("Это 5?")
            if ans7 == "да":
              print("Это 5")
            else:
              print("Это 6")
        elif ans5 == "нет":
          ans6 = input("Это число больше 2?")
          if ans6 == "да":
            ans7 = input("Это 3?")
            if ans7 == "да":
              print("Это 3")
            else:
              print("Это 4")
          elif ans6 == "нет":
            ans7 = input("Это 1?")
            if ans7 == "да":
              print("Это 1")
            else:
              print("Это 2")
              
          
          
            