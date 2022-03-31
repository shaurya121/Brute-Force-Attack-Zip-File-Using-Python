
# Brute Force Attack on Zip File Using Python

ZIP is file format that is used for data compression. It also supports password protection. 
This program helps in knowing the password in case forgot it.

## Screenshots

![App Screenshot](## Screenshots

![App Screenshot](https://github.com/shaurya121/Brute-Force-Attack-Zip-File-Using-Python/blob/main/Screenshot.png/468x300?text=App+Screenshot+Here/468x300)

## Installation

Install tqdm module to create progress bar

```bash
  pip install tqdm
```
    
## Usage/Examples
Here, enter the location of zip file.
```python
protected_file=input("zip file: ")
```

Enter the location of wordlist (text file containing random passwords).
```python
wordlist=input("choose wordlist: ")
```

Now, we need to whether it is actually a zip file or not. 
```python
try:
	zip_file=zipfile.ZipFile(protected_file)
	n_pass=len(list(open(wordlist, "rb")))
except:
	#print("\n")
	print("\nFile not zip, exiting...")
	exit(0)
```

Finally, we will start attacking the zip file and print the actual password.
```python
with open(wordlist, "rb") as wordlist:
	for word in tqdm(wordlist, total=n_pass, unit="word"): 
		try:
			zip_file.extractall(pwd=word.strip())
		except:
			continue
		else:
			print("[+] Password found:", word.decode().strip())
			print("Exiting...")
			exit(0)
```
## Acknowledgements

 - [@xtremepentest](https://twitter.com/xtremepentest)
 
