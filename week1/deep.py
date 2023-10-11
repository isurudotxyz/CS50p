str = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().replace("-","").replace(" ","")

if (str == "42") or (str == "fortytwo"):
  print("Yes")
else:
  print("No")