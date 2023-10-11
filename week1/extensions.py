s = input("File name: ").lower()
extension = s[-4:]

def switch(input):
    if input == ".jpg" or input == "jpeg":
       print("image/jpeg")
    elif input == ".pdf":
       print("application/pdf")
    elif input == ".gif":
       print("image/gid")
    elif input == ".txt":
       print("text/plain")
    elif input == ".png":
       print("image/png")
    elif input == ".zip":
       print("application/zip")
       
switch (extension)