import hashlib
file = open("Data.txt","r",encoding="utf-8")
for line in file.readlines():
    if(line!="\n"):
        line = line.split('"')
        fraseMD5 = hashlib.md5(line[1].encode("utf-8")).hexdigest()
        fraseSHA256 = hashlib.sha256(line[1].encode("utf-8")).hexdigest()
        frase = line[1]
        line = line[2].split("-")
        sha256 = line[1]
        md5 = line[2].strip()
        if(md5==fraseMD5 and sha256==fraseSHA256):
           print(f"{frase} | SHA256 e MD5 corretos")
        elif(md5==fraseMD5 and sha256!=fraseSHA256):
            print(f"{frase} | Somente SHA256 correto")
        elif(md5!=fraseMD5 and sha256==fraseSHA256):
            print(f"{frase} | Somente MD5 correto")
        else:
            print(f"{frase} | Nenhum dos dois corretos")
file.close()
