# Cryptography w/ AES-256 Algorithm
If you're running Python 3.7 or newer you're good to go. 
Simply open the terminal and run the command:

```shell
pip install -r Requirements.txt
```

All the necessary libraries should be installed.

Simple and easy to use just follow through, you can either encrypt/decrypt texts or files, by default it accepts UTF-8 encoded strings but you can modify 
AshFileCrypt to read files in binary mode and encrypt/decrypt binary data.

If you want to save the contents you've enctypted/decrypted and keep a log then use AshDatabase.py module to register your contents with the according keys,
or you can use this to save various account names with their according passwords.  
Here Im using "dataclasses" module which was introduced in Python 3.7, so make sure to install it if you have an older version.

The qr.py module is used to display a qr code of either the key or the encrypted message, here I'm using it to display the encrypted message so it 
can be quickly scanned and transmitted , you can use qr versions from 1 to 40 , although I recommend using 40 since it can take the maximum number 
of characters for files and 10 if you're working with the GUI,

You can use the AshCryptGUI.py , it's merely a GUI to encrypt and decrypt a text of a maximum of 200 characters and also display the qr representation 
of the text post encryption.

NOTE : the key is not specified in the GUI its hard-coded, if you want to change the key make sure to change it from within the file AshCryptGUI.py itself, 
by default it uses the key in bytes : 
```python
k = b'Ashreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef='
```
if you want to change the key you can directly replace the key by another BYTES key it will automatically work if its the correct form.
To check if it's in the correct form run this ( replace b'Ashreee...eef=' with your key ) : 
```python
print(CryptFiles.intruder_bytes_key_verification(b'Ashreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef='))
```
If the output is 1 then the specified key can be used.

NOTE again that only works if the key is in BYTES format.

I recommend using key_gen() function ALL THE TIME to generate randomly secure keys since AES-256 is considered secure against brute-force attacks, given the key is generated randomly and has sufficient entropy. The security of AES-256 lies in the strength of the key and the inability to efficiently search through the vast keyspace, it takes 2^256 attempts to run through all the possible combinations. If a brute force attacker runs through 1 trillion combos a second it will 
still take 10^46 years to run through every possible combination.

Im using  the bytes key :  b'Ashreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef=' / string key : 'Ashreeeeeeeeeeeeeeeeeeeeeeeeeeef'   for demonstartion purposes only. 
It doesnt take 2 seconds to guess a key based on my name. So ALWAYS USE A RANDOMLY GENERATED KEY.  

Follow these 2 simple steps to work a key: 
1) Generate a random string key : 
```python
key = CryptFiles.genkey()
```
The output should be something like this : 
```python
EcQJTaIHLx0lbWLnz8K28moOEywjJwPx
```
2) Use the getready() function to get it ready for use, otherwise it will raise a TypeError
```python
key = CryptFiles.getready(key)
```
Then you can simply pass the key variable to any of the encrypt() or decrypt() functions.

These steps work for all the modules I provided.

If you want to encrypt a file : 
1) Follow the steps above to set the key up.
2) Create an instance of the class CryptFiles and pass 2 arguments, the first one being the target file and the second argument is the key : 
```python
instance1 = CryptFiles('target.txt', key)
```
3) Apply either the function encrypt() or decrypt() to that instance :
```python
instance1.encrypt()
```
```python
target.decrypt()
```

The same applies for AshTextCrypt.
Thats it, if you follow the steps above then everything should work just fine. 






