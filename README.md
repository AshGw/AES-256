# Cryptography w/ AES-256 Algorithm
## Overview
This project implements AES-256 cryptography to ensure secure data encryption and decryption (Files/Text). It also includes a simple graphical user interface (GUI) for easy interaction with the application. The project incorporates a database module that allows for the management and storage of classified content securely.

## Reason Behind It

I firmly believe in the power of Freedom in a world dominated by control, surveillance, and constant privacy violations , this led me to develop a way to work with a set of tools in Python , levereging the AES-256 algorithm using the Cryptography module to make it easier for individuals to safeguard their data without blindly relying on third parties to do it for them , while at the same time making it easy enough for anyone to use even with limited programming knowledge.

## Installation

If you're running Python 3.7 or newer you're good to go. 
Simply open the terminal and run the command:

```shell
pip install -r Requirements.txt
```

All the necessary libraries should be installed.

## Database Module
To support efficient content management, I have integrated a database module. This module enables the storage and retrieval of classified content in a safe and secure manner. 

The database ensures that the encrypted data remains organized and readily accessible to anyone with the right key.
Any content going to it is encouraged to be encrypted with a key first that you must keep off grid.

Note that in AshDatabase.py I'm using "dataclasses" module which was introduced in Python 3.7, so make sure to install it if you have an older version.



## QR Module
The qr.py module is used to display a qr code of either the key or the encrypted message, here I'm using it to display the encrypted message so it 
can be quickly scanned and transmitted , you can use qr versions from 1 to 40 , although I recommend using 40 since it can take the maximum number 
of characters for small files , and 10 if you're working with the GUI which is intended for text/short messages,


## GUI
You can use the AshCryptGUI.py , it's merely a GUI to encrypt and decrypt a text of a maximum of 200 characters and also display the qr representation 
of the text post encryption.

NOTE : 
The key is not specified in the GUI its hard-coded, if you want to change the key make sure to change it from within the file AshCryptGUI.py itself,
it's just a security measure. 
By default it uses the following key in bytes : 
```python
k = b'Ashreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef='
```
if you want to change the key you can directly replace the key by another BYTES key it will automatically work if its the correct form.
To check if it's in the correct form run this ( replace b'Ashreee...eef=' with your key ) : 
```python
print(CryptFiles.bytesverify(b'Ashreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef='))
```
If the output is 1 then the specified key can be used.

NOTE again that only works if the key is in BYTES format.

## Recommendations

I recommend using the genkey() function ALL THE TIME to generate randomly secure keys since AES-256 is considered secure against brute-force attacks, given the key is generated randomly and has sufficient entropy. The security of AES-256 lies in the strength of the key and the inability to efficiently search through the vast keyspace a brute force attacker can run through 1 trillion combos a second it will still take 10^46 years to run through every possible one.


NOTE that securing the key is as important as generating a cryptographically secure one , so 
implement secure key management practices, including secure key storage, rotation, and exchange when necessary. Protect the confidentiality and integrity of your keys to prevent unauthorized access.

Here you might see me using the bytes key : 
```python
b'Ashreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef='
```
or the string key : 
```python
'Ashreeeeeeeeeeeeeeeeeeeeeeeeeeef' 
```
they're used for demonstartion purposes only. 
It takes no time to guess a key based on my name. So ALWAYS use a RANDOMLY generated key.  

## Generate a Key 

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

## How to Encrypt/Decrypt

I want to state that By default it accepts UTF-8 encoded strings but you can modify AshFileCrypt.py to read files in binary mode and encrypt or decrypt binary data.

If you want to encrypt a file : 
1) Follow the steps above to set the key up.
2) Create an instance of the class CryptFiles and pass 2 arguments, the first one being the target file and the second argument being the key : 
```python
instance1 = CryptFiles('target.txt', key)
```
3) Apply either the function encrypt() or decrypt() to that instance :
```python
instance1.encrypt()
```
```python
instance1.decrypt()
```

The same applies for AshTextCrypt.

That's it, if you follow the steps above then everything should work just fine. 

## Important Points

There are couple of points I want to touch on : 

This function : 
```python
changeform(key : string) -> Union [ bytes , int ]
```
This fucntion can be used to turn a given string key that looks like bytes ( but is a string ) into actual bytes , the_given_key.encode() wouldn't work here to get the expected result.

For example if you have a simple user input as  : 
```python
b'Ashreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef='
```
Any time a bytes key like this is given, it is automatically read as a string unless it's hardcoded already, then you dont need to use this function just pass the key directly.

Now if it's passed along as string from a GUI or a simple user input, trying to encrypt/decrypt with it would raise an Exception, this is where this function comes in , pass in the key that looks like bytes then it will bring back the same key , same look , but in actual bytes format so it can be used.

After you changeform(key) you need to actually check if it can be used as a bytes key , it must be a urlsafe base64 endoced key, to check it use  : 
```python
result = bytesverify(key_in_bytes)
```
If the result is 1 then the key can be used.

Although you don't have to use bytes keys it is optional my recommendation is to always generate a random key and then get it ready for use as I specified above, 
although sometimes you need to pass in a key that you've received then in that situation you can verify it using : 
```python
result = strverify(string_key)
```
If the result is 1 you can use it.

## Already an Expert ?
...
1) the low-level primitive code AES using CBC mode with PKCS7 padding, HMAC with SHA512
2)This decision was made to ensure that the encryption remains secure against potential advancements in computing technology in the years to come. thats why I didnt include a timestamp like Fernet's module implementations also i have made the key 512 Bit long 
3) You can keep using fernet for simplicity but if you want to switch Fernet with Ash you can simply change the name thats it at encrypt() and decrypt() functions after you've imported the module ofc  

