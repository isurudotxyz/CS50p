list = {}

while True:
  try:
      item = input("").upper()
  except EOFError:
      list = dict(sorted(list.items()))
      break
  except:
      pass
  else:
      if item in list:
         list[item] += 1
      else : 
         list[item] = 1

for key in list:
    print(list[key],key)
      