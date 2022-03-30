from tqdm import tqdm
import zipfile

protected_file=input("zip file: ")
wordlist=input("choose wordlist: ")

try:
	zip_file=zipfile.ZipFile(protected_file)
	n_pass=len(list(open(wordlist, "rb")))
except:
	#print("\n")
	print("\nFile not zip, exiting...")
	exit(0)

print("\nNumber of password that will be checked:", n_pass)
with open(wordlist, "rb") as wordlist:
	for word in tqdm(wordlist, total=n_pass, unit="word"):
		# use for loop to check each password in the wordlist 
		try:
			zip_file.extractall(pwd=word.strip())
		except:
			continue
		else:
			print("\n")
			print("[+] Password found:", word.decode().strip())
			print("\n")
			print("Exiting...")
			exit(0)
			
print("\n")
print("[x] Password not found in the wordlist, try another wordlist")
		
