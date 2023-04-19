i = 1
with open("pitanja", "r") as f:
    for line in f:
        print("\""+str(i)+"\" : \""+ line.strip()+ "\",")
        i = i + 1
