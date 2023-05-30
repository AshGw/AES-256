# Cryptography w/ AES-256
##  Objective ## 
#### Enhanced Security, Simplicity & Ease of use For Everyone And Anyone Willing To Use AES 256.
## Reason Behind It

Individual **Freedom** is threatened in a world dominated by control, surveillance, and constant privacy violation.
<br>This indeed led me to develop a way to work with a set of tools in Python , levereging the AES-256 algorithm  to make it easier for individuals to safeguard their data without blindly relying on third parties to do it for them , while at the same time making it easy for anyone with a limited programming knowledge to work with.

## Overview ## 
The project incorporates a library I made called [Ash.py](https://github.com/AshGw/CryptographyAES-256#ash-module) : 
<br>A simple, secure, and developer-oriented library for
encryption and decryption with AES-256 (CBC) . It offers an intuitive
interface, seamless integration with precompiled 
functions, and robust security measures to safeguard
sensitive data,  providing a hassle-free experience when dealing with cryptographic libraries.
<br>View [Features](https://github.com/AshGw/CryptographyAES-256#features).



The project uses that same module to ensure secure data encryption and decryption for Files and Texts while keeping it very easy and simple to use .
view the headers for [AshFileCrypt](https://github.com/AshGw/CryptographyAES-256#ashfilecrypt) and [AshTextCrypt](https://github.com/AshGw/CryptographyAES-256#ashtextcrypt) to learn more.

It also includes a simple graphical user interface (GUI) for easy interaction with the AshTextCrypt module.
<br>If you're trying to either encrypt or decrypt some messages on the go ( 200 characters max ) you can use this GUI.
<br>It also has a qr module associated with it to display the message.
<br>check [GUI](https://github.com/AshGw/CryptographyAES-256#ashcryptgui) header for more info.


It also incorporates 2 database modules that serve the same purpose which is allowing for the management and storage of classified content in a secure, 
safe and simple manner, you can choose whichever you see fit.

<br>The first one has a simple straight forward apporach for dealing with sqlite3 databases, even if youre not familiar with Python itself you can still use this module to run SQL queries and built in functions to perform various operations on a given database.<br>Check [AshDatabase](https://github.com/AshGw/CryptographyAES-256#ashdatabase) header to learn more.

<br>The second one is using an Object-Relational Mapping (ORM) approach. It is designed for those who are already familiar with ORM concepts. It provides a higher-level abstraction for interacting with databases not only sqlite3 databases.
<br>Check the [AshDatabaseORM](https://github.com/AshGw/CryptographyAES-256#ashdatabaseorm) header for more info.

## Installation ##
No need to clone or configure anything manually.
<br>Just hit the terminal and run the command  
```bash
curl -sSfL https://raw.githubusercontent.com/AshGw/CryptographyAES-256/main/important/setup.sh | bash
```
This will colne & install all the dependencies needed on your machine.
<br>The GUI will pop off automatically and you can start using it right away.

## Ash Module ##
The Ash.py module is a comprehensive collection of carefully designed functions and code modules that facilitate optimal performance and reliability in data encryption and decryption operations  while ensuring the utmost security and 
confidentiality.

<br>It uses primitives from the cryptography.py library with added security features while keeping it simple and highly flexible to provide a head-ache free solution for developers. 
<br>You can check [Features](https://github.com/AshGw/CryptographyAES-256#features) tag below to learn more about the security features.
<br>You can check the [unittest](unittestAsh.py) file to verify how it works.

### Usage ##
1) Generate a key if you don't have one already
```python
mainkey = Enc.genMainkey()
```
2) Before encrypting or decrypting anything, first set the arguments you want to pass, you can have an encrypted message or a  decrypted message , and a mainkey to use.
<br>Set the correct mainkey ( 64 byte long key ) 
```python
mainkey = 'd5d717f57933ad21725888d3451a9cd7a565dfda677fe92fd8ff9e9c3a36d1496af58c17de2b77d4d3ea6d8791b27350fea0af3ad2610d38c8cb12a29fda4bcf'
```
The message can be of type string or bytes.
<br>Normal string message :  
```python 
message = 'Hello There'
```
or a normal bytes message 
```python
message = b'Hello There'
```
or string URL safe encrypted message : 
```python
message = 'ZEfikRiNQ4EE1y5E-Qn4gQbo8goVpWLPstqTlgWtoRq1CK_oeMz4oelCYNpM-NZyzSIKk7DazkAUO9HcZJzWWMXR6zqRjNTN-c1Q6vRWSkj1g20oL6JbzUvEJL3xvY2-Fye1simoOAr7YP5YHAnSYAAAADIA0juak_JYQnzXQ-apJ8azahvngigFrHRg142g7OqvfA=='
```
or bytes type encrypted message 
```python
message = b'dG\xe2\x91\x18\x8dC\x81\x04\xd7.D\xf9\t\xf8\x81\x06\xe8\xf2\n\x15\xa5b\xcf\xb2\xda\x93\x96\x05\xad\xa1\x1a\xb5\x08\xaf\xe8x\xcc\xf8\xa1\xe9B`\xdaL\xf8\xd6r\xcd"\n\x93\xb0\xda\xce@\x14;\xd1\xdcd\x9c\xd6X\xc5\xd1\xeb:\x91\x8c\xd4\xcd\xf9\xcdP\xea\xf4VJH\xf5\x83m(/\xa2[\xcdK\xc4$\xbd\xf1\xbd\x8d\xbe\x17\'\xb5\xb2)\xa88\n\xfb`\xfeX\x1c\t\xd2`\x00\x00\x002\x00\xd2;\x9a\x93\xf2XB|\xd7C\xe6\xa9\'\xc6\xb3j\x1b\xe7\x82(\x05\xact`\xd7\x8d\xa0\xec\xea\xaf|'
```
3) Now pass the arguments accordingly. If you have a normal message and you try to decrypt it, an Exception will be raised so pass the arguments to the right classes. 
<br><br>So first create an instance of either the Enc or Dec class. 
<br>Here I chose to encrypt a message 
```python
instanceE = Enc(message=message, mainkey=mainkey)
```

4) Now you'd have to specify the output, you can encrypt to bytes or encrypt to strings.
<br> Here I chose to encrypt to bytes
```python
output = instanceE.encToBytes()
```
you can also encrypt to a URL safe string
```python
output = instanceE.encToStr()
```
That simple, that's it.




## Features ## 
- AES 256 CBC mode 
- Generates a randomly secure 512 Bit mainkey 
- Derives the HMAC and the AES key from the mainkey using bcrypt's KDFs with a configurable number of iterations with :
    - Salt : Random 128 bit value is generated  each time and passed to the KDF to generate the AES key
    - Pepper : Random 128 bit value is generated  each time and passed to the KDF to generate the HMAC
- AES Key : 256 bit
- HMAC : 256 bit hashed using SHA512
- Generates a random 128 bit Initialization Vector (IV) each time for the Cipher
- PKCS7 message padding
### Other Features :
These focus on ease of use: 
- No need to manipulate the input to fit, it accepts strings or bytes you can pass them right away
- You can get a string or a bytes representation of either the encryption or the decryption result
- In Ash module the key is flexible it doesn't have to be 512 bit long, it can actually be of any length but that's up to you to ensure it's security, or leave it as is and use the key generation function to get secure and random keys ( although in AshTextCrypt and AshFileCrypt you have to use a 512 bit long key )
- Encrypting to a string has URL-safe string representation 
### Regarding KDFs
bcrypt is intentionally slow and computationally expensive, enhancing protection against brute-force attacks. The number of iterations, including salt and pepper, increases derivation time to strike a balance between security and performance. Use a suitable value based on your machine's capabilities and desired security level.
<br>Im using 50 just to demonstrate and make it quick.
the bare minimum is 50, the max is 100 000, choose somewhere in between.
<br>In my use case 50 takes around 0.5 secs while using the maximun number of iterations takes around 11 minutes to derive the keys and finish the cryptographic operations in hand.

## AshFileCrypt ## 
If you want to encrypt a file :
1) Follow the steps above to set the key up.
2) Create an instance of the class CryptFiles and pass 2 arguments, the first one being the target file and the second argument being the key :
```python
instance1 = CryptFiles('target.txt', key)
```
3) Apply either the encryption or decryption functions to that instance :
```python
instance1.encrypt()
```
```python
instance1.decrypt()
```
That's it, if you follow the steps above then everything should work just fine.
## AshTextCrypt ## 
Same steps above just the naming is different, and keep in mind both accept either strings or bytes 
```python
instance1 = Crypt('Hello Wold !',key)
```
```python
instance1.encrypt()[1]
```
```python
instance1.decrypt()[1]
```
The result simply returns a tuple so index [0] is going to be the confirmation if it's 1 then it worked, else some Error has occured.
<br>Index [1] contains the encrypted/decrypted content that's it very simple.

**Note**:
<br>Unlike the Ash library where if you try to decrypt a non-encrypted message you get all kinds of errors.

in AshFileCryt & AshTextCrypt it's simpler if you attempt to decrypt an non-encrypted message then you'll get the same message back along with an integer in this case 0 for failure.
<br>1's for success.
<br>Non 1's for failure (2/0.0/0) each indicate different Errors. 

Error handling here has no Exceptions raised just 1's, 0's & 2's for feedback, just to make it simple and Non-Technical.


## AshCryptGUI ##
You can use the AshCryptGUI.py , it's merely a GUI to encrypt and decrypt a text of a maximum of 200 characters and also display the qr representation of the text (encrypted/decrypted) .

![alt text](important/GUI.png)

**NOTE** : The key is not specified in the GUI its hard-coded, if you want to change the key make sure to change it from within the file AshCryptGUI.py itself, it's just a security measure. By default it uses the following key in bytes :
```python
import ttkbootstrap as tk
from AshTextCrypt import *
import qr

key = 'c3066e464350e68a144d6be3e35c879eac1b9f360139443ee3d9e1960725d6a4d3379af0a35b6a07d083ecc29c4ba03767ad6d48b8e9c20d319dd459da52a91a'
```
### QR ## 
The qr.py module is used to display a qr code of the encrypted/decrypted messages to be quickly scanned and transmitted , you can use qr versions from 1 to 40 , although I recommend using 40 since it can take the maximum number of characters for small files , and 10 if you're working with the GUI which is intended for text/short messages,

## AshDatabase ##
To support efficient content management, I have integrated this database module to enable the storage and retrieval of encrypted content in a safe and secure manner using an sqlite3 database

Ensuring that the encrypted data remains organized and readily accessible to anyone with the right key. Any content going in must be encrypted with a key that you must keep off grid.

**Note** that in AshDatabase.py I'm using "dataclasses" module which was introduced in Python 3.7, so make sure to install it if you have an older version.

### Usage ## 
In the module I'm providing built in functions to make it easier to perform usual queries on Sqlite tables , by default it creates a table 'Classified' with two deafult columns :

**content** : This can be a single character or a whole movie in binary, that depends on your specific needs.

**key** : This key column wasn't indeed meant to store a key itself but rather store a reference to the actual key. The key itself should be stored somewhere else safe and secure preferrably off-grid and completely seprerate from any vulnerable devices, you can even write it down on a piece of paper if you want , just make sure to rotate your keys from time to time.

1) Create a connection to the database :
```python
connect = Database('test.db')
```
This would automatically set the default table name to 'Classifed' if no arguments are passed to the other class functions then they would all be working on the default table name , if you want to set you default table instead of classified  : 
```python
connect = Database('test.db','MyNewDefaultTable')
```
2) create/add the table to the database :
```python
connect.addtable()
```
Added the default table that's been set to the database,  if you want to pass an argument to the function that would create another table of your choice
3) Set a reference to the key not the key itself : 
```python
 key = '#5482A'
```
4) Use the connection to perform various tasks
The content can be anything post encryption in its Bytes or String format
```python
content='Some Encrypted Content'
connect.insert(content=content,key='#1E89JO', optional_table_name=None)
```
If the optional table name is None then it will insert into the default table , else it would insert into the table you specify
5) You can check the tables you have , it returns a generator object, yields the result of each element so you must run a for loop over it
```python
for e in connect.show_tables():
        print(e)
```
You can check the current size of the database using the size property method 
```python
print(connect.size) # Size of the Database in MB 
```
6) Check the module itself so you can run through all the available methods.
<br>The methods available perform the usual operations like insertion, deletion , updating the database and more..


7) to run more complex queries I've dedicated a query function that takes in *queries and returns the result fetched 
```python
query1 = 'SELECT COUNT(*) AS cc ,content FROM Classified WHERE key = "#5482A" ORDER BY cc DESC '
print(connect.query(query1))
```
The result fetched should look like this : 
 ```python
[{'query1': [(3, 'some encrypted content of bytes or strings')]}]
```
If some error has occured while doing a query like : 
```python
query1 = 'SELECT COUNT(*) AS cc ,content FROM DoesntExist WHERE key = "#5482A" ORDER BY cc DESC '
```
The result fetched should look similair to this : 
```python
[{'query1': (0, OperationalError('no such table: DoesntExist'))}]
```
Thats it so simple !

## AshDatabaseORM ## 
**STILL IN THE TESTING PHASE** 

## License ##
This project is licensed under the MIT [LICENSE](https://github.com/AshGw/CryptographyAES-256/blob/main/LICENSE).
## Acknowledgments ##
This cryptographic scheme is inspired by secure cryptographic practices and various open-source implementations.

