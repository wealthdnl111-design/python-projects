from tqdm import tqdm
import zipfile

var = ""
wordlist = [passwords.strip() for passwords in open("wordlist.txt")]
zip_file = zipfile.ZipFile("_Getintopc.com_FL_Studio_Producer_Edition_21.2.2.3914_All_Plugins_Edition.rar")

for i in tqdm(wordlist, desc = "Checkingpassword in wordlist"):
    try:
        zip_file.extractall(pwd = i.encode())
        var = i
        break
    except:
        continue
print("[+] Password Found: {}".format(var))
