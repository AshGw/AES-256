# Cryptography App & Library w/ AES-256
##  Objective ## 
#### Enhanced Security, Simplicity & Ease of use For Everyone And Anyone Willing To Use AES 256.
## Reason Behind It
In a world where control, surveillance, and privacy violations are increasingly prevalent, the protection of individual freedom becomes crucial. 

As a firm believer in **Freedom** , I have developed a set of tools in Python that leverages the AES-256 algorithm to make it easier for undividuals to safeguard their data without blindly relying on third parties to do it tor them  . 

My aim here is to make these tools accessible and user-friendly, even for individuals with limited programming knowledge. By providing these resources, I hope to contribute to the preservation of privacy and enable individuals to take control of their own data security, so feel free to explore these tools.
## Overview ## 
![alt text](important/GUI.png)
The project incorporates an App & a library called **AshCrypt** : 

**App :** 
<br>Fully-fledged application that integrates all the modules in the library merging them into a unified and powerful software solution for developers and for people with no programming knowledge whatsoever
<br>check [GUI](https://github.com/AshGw/AES-256#AshCryptGUI) header for more info.

**Library :** 
<br>A simple, secure, and developer-oriented library for
encryption and decryption with AES-256 (CBC) . 
<br>The core of the library is the module `Ash`
It offers an intuitive interface, seamless integration with precompiled 
functions, and robust security measures to safeguard
sensitive data,  providing a hassle-free experience when dealing with cryptographic libraries.
<br>View [Features](https://github.com/AshGw/AES-256#features) Header for more details.





### For Developers ###
The project uses `Ash` module to ensure secure data encryption and decryption for Files and Texts while keeping it very easy and simple to use .
view the headers for [FileCrypt](https://github.com/AshGw/AES-256#filecrypt) and [TextCrypt](https://github.com/AshGw/AES-256#textcrypt) to learn more.


It also incorporates a database module that serve the same purpose which is allowing for the management and storage of classified content in a secure, 
safe and simple manner, you can use whichever you see fit.

<br>The module has a simple straight forward approach for dealing with sqlite3 databases, even if you're not familiar with Python itself you can still use this module to run SQL queries and built in functions to perform various operations on a given database.<br>Check [Database](https://github.com/AshGw/AES-256#database-1) header to learn more.

## Installation ##
There are many ways to go by this : 
### If you want to use it as a library ###
You can simply use **pip**
<br>First upgrade the package installer 
```bash
pip install --upgrade pip 
```
Then install the Library 
```bash
pip install AshCrypt
```
This will install the latest version of `AshCrypt`.
You can start using it in your code by importing its modules : 
```python
from AshCrypt.Ash import *
```
That's it.
### Ready-to-go Executable files:
If you want to use the App right away : 
<br>**For Windows** : Download this repo as a ZIP file, extract the content
<br>then click on `Executables > AshCryptGUI.exe` This will automatically run the GUI

### Whole repo installation 
Now if you want to get the whole repo with no manual configurations
<br>Run this command in the Terminal
```bash
curl -sSfL https://raw.githubusercontent.com/AshGw/AES-256/main/important/setup.sh | bash
```
This will run the commands in [setup.sh](important/setup.sh).
<br>It will clone & install all the dependencies needed on your machine and activate the development mode, inside the directory you're currently at.

you can use this command to automate the environment setup process if you haven't done it  already
```bash
curl -sSfL https://raw.githubusercontent.com/AshGw/AES-256/main/Docker-build/env-setup.sh | bash
```
<details>
<summary>Got Errors ?</summary>

<h5>For Debian based systems</h5>

1) Install `curl` if you don't have it already 
```bash
sudo apt-get install curl
```
2) If you're running a lightweight python version it might not include `tkinter` in the standard library so run
```bash
sudo apt-get update
sudo apt-get install python3-tk 
```
3) If you're running `python 3.6` or older then you might need to install `dataclasses`
```
pip install dataclasses
```
<br>Now if none of this works you might just use the docker image for this purpose, so check this [directory](Docker-build)
</details>

**After the library is installed** 
<br>To run the GUI 
```shell
python -m AshCrypt.AshCryptGUI
```

**NOTE**:
You  can use `CliCrypt.py` which is an innovative command line interface (CLI) designed to provide encryption and decryption capabilities for both text and file data with no constraints intended for use within systems where you can't use GUI's.


To run the CLI 
```shell
python -m AshCrypt.CliCrypt
```

## Ash Module ##
The `Ash.py` Module is a comprehensive collection of carefully designed functions and code modules that facilitate optimal performance and reliability in data encryption and decryption operations  while ensuring the utmost security and 
confidentiality.

<br>It uses primitives from the `cryptography.py` library with added security features while keeping it simple and highly flexible to provide a head-ache free solution for developers. 

<br>You can check [Features](https://github.com/AshGw/AES-256#features) tag below to learn more about the security features.
<br>You can check the [unittesting file](AshCrypt/unittests/unittestAsh.py) to verify how it works.

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
<br><br>So first create an instance of either the `Enc` or `Dec` class. 
<br>Here I chose to encrypt a message 
```python
instanceE = Enc(message=message, mainkey=mainkey)
```

4) Now you'd have to specify the output, you can encrypt to bytes or encrypt to URL-safe strings.
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
- In Ash module the key is flexible it doesn't have to be 512 bit long, it can actually be of any length but that's up to you to ensure it's security, or leave it as is and use the key generation function to get secure and random keys ( although in `TextCrypt` and `FileCrypt` you have to use a 512 bit long key )
- Encrypting to a string has URL-safe string representation 
### Regarding KDFs
Note that bcrypt is intentionally slow and computationally expensive, enhancing protection against brute-force attacks. The number of iterations, including salt and pepper, increases derivation time to strike a balance between security and performance. Use a suitable value based on your machine's capabilities and desired security level.
<br>Im using 50 just to demonstrate the process and make it quick.
<br>The bare minimum is 50, the max is 100 000, choose somewhere in between.
<br>In my use case 50 takes around 0.5 secs while using the maximum number of iterations takes around 11 minutes to derive the keys and finish the cryptographic operations at hand.
<br>You can check how it works by checking this [Jupyter Notebook](demo/demo.ipynb) demo file
## AshCryptGUI ##
The GUI as mentioned above is a fully fledged application , you can use it to encrypt files , texts , keep track of files by storing them on demand to a main database , also on demand it can keep track of the keys used for cryptographic operations.
### Usage ###
1) Set the main key up. If you don't have one , press on the button `generate` to generate a secure safe key ready for use. 
2) Now you're able to encrypt files or text (text is limited to 200 characters max)
####  Text : 
- You can insert some text in the entry right below the `TEXT ENCRYPTION` label.<br>The given text will be encrypted and you can choose if you want to have that text displayed as a qr code, a qr image will pop on the screen and you'll be able to scan it using your phone.
- Insert some encrypted text below the `TEXT DECRYPTION` label.<br>The Given text will be decrypted and you'd have the option to display the "plaintext" as a qr code to be scanned by other devices.
#### Files
- Under the `FILE PATH` label enter the file name (if it's in the current working directory) or submit the whole file path , the file can be of any type, click on `ENCRYPT FILE` Button to encrypt the given file , if the encryption turned out to be successful , you'll see a success message along with a `added .crypt extention to the file` message if the encryption wasn't successful you'll see an error message specifying the problem.<br>Note that you cannot re-encrypt a file that  has `.crypt` as extention.
- The file name should be changed by now to `filename + '.crypt'` , if the file has .crypt extention you can go ahead and decrypt it , if the same key is used for both enc/dec operations then the result should be `success` + `removed .crypt extention` from the file.
#### Database
- Now you have some encrypted/decrypted files but you want to keep them stored somewhere safe, this is where the main database comes in , where you need to store your files + their content + reference to the key used for their encryption/decryption. you can specify your database by 
1) Specify the actual path where you want your database to be 
2) Give it a name, it must be a valid file name that ends with `.db` .<br>
If the database doesn't exist then a database with the name you've given will be created and automatically connected to.<br>If the given database already exists then it will automatically be connected.
3) Did I mention the keys database ? well if you give a database it will also create a keys database with the same name as the database you chose plus `Keys` added to its name. This database holds the actual keys and the reference to these keys.
<br>The only common piece of data that the two separate databases have in common are the key reference values.  

**Note** : If your main database gets compromised , then the attacker wouldnt have anything useful , they can never know the actual key from the reference key so no problem with that if it only contains encrypted content BUT NEVER EVER GET YOUR KEYS DATABASE COMPROMISED ! 
<br>If anyone gets hold of your main database they would only see some encrypted content and some key refrence that is actually 100% independent of the actual key used for encryption so they have nothing , but if they get hold of the keys database they can look for matching refs and use the matching key to decrypt that binary encrypted data to its actual format.
That's why I made two different databases not two tables within a single database. 
<br> So you keep your keys database safe and secure.


**Info** Both databases have the same table called `Classified` that has 4 columns <br>`ID` which is auto generated & incremented for each piece of data that gets inserted<br>
`Name` that holds the filename in both databases , although in the keys database if you haven't specified any file to operate on and keep selecting keys the keys name will be `STANDALONE` 
<br>`Contnet` in the main db that holds the entire content of the given file, in keys db that holds the actual 512 bit long encryption key.
<br>`Key` in  both db's that holds the `KeyRef` or key reference value
#### Usage 
The buttons are self-explanatory so do what you see fit. the result of any task related to the databases is displayed in `DATABASE OUTPUT CONSOLE` although you can run a query anytime by writing a query and using `query` button , the result will be displayed to an `output.json` file that auto-deletes when you exit the app.
<br>Just click buttons and check the result in the output console, it will guide you through the process.

<br>To run the GUI anywhere
```shell
python -m AshCrypt.AshCryptGUI
```




## FileCrypt ## 
If you want to encrypt a file :
1) Follow the steps above to set the key up.
2) Create an instance of the class CryptFiles and pass 2 arguments, the first one being the target file and the second argument being the key :
```python
instance1 = CryptFile('target.txt', key)
```
```python
instance1 = CryptFile('testDataBase.db', key)
```
The file can be of anything : image`.png`, movie `.mp4`,`.sqlite`  etc..
<br>It doesn't have to just be of `.txt` extension ,can be of anything really.  
<br>**Note** : 
If the file is not in the working directroy you can specify the whole path: 
<br>**For windows**
```python
target = CryptFile('C:\\Users\\offic\\MyProjects\\SomeOtherfolder\\myfile.txt',key) 
```
<br>**On Mac and Linux :**
```python
target = CryptFile('/User/Desktop/MyProjects/SomeOtherfolder/myfile.txt',key)
```
3) Apply either the encryption or decryption functions to that instance :
```python
instance1 = CryptFile('qrv10.png',key)
instance1.encrypt()
```
you can apply `print()` on `instance1.encrypt()`to check the result :
<br> 1 : File successfully encrypted/decrypted + added/removed .crypt extension 
<br> 2 : File is empty
<br> 3 : File doesn't exist
<br> 4 : Unknown Error usually a system related one 
<br> 5 : Key is denied for cryptographic use
<br> 6 : File is already encrypted/decrypted
<br> 7 : File is not a file it's a directory
<br> 0 : Error in enc/dec probable file distortion, tampering or wrong key
```python
instance1.encrypt()
```
```python
instance1.decrypt()
```
**Note** : 
<br>Sometimes you might forget that you've applied  `encrypt()` more than one time , so when you try to `decrypt()` the file ,  the output is 1 but the file content is still in binary, just apply the function `decrypt()` the same number of times you applied `encrypt()`.


That's it, if you follow the steps above then everything should work just fine.
## TextCrypt ## 
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
The result simply returns a tuple so index `[0]` is going to be the confirmation if it's 1 then it worked, else some Error has occured.
<br>Index `[1]` contains the encrypted/decrypted content that's it very simple.

**Note**:
<br>Unlike the `Ash` library where if you try to decrypt a non-encrypted message you get all kinds of errors.

in `FileCryt` & `TextCrypt` it's simpler if you attempt to decrypt an non-encrypted message then you'll get the same message back along with an integer in this case `0` for failure.
<br>`1`'s for success.
<br>Non `1`'s for failure (`2`/`0.0`/`0`) each indicate different Errors. 

Error handling here has no Exceptions raised just `1`'s, `0`'s & `2`'s for feedback, just to make it simple and Non-Technical.


### QR ## 
The `qr.py` module is used to display a qr code of the encrypted/decrypted messages to be quickly scanned and transmitted , you can use qr versions from `1` to `40` , although I recommend using `40` since it can take the maximum number of characters for small files , and `10` if you're working with the GUI which is intended for text/short messages,

## Database ##
To support efficient content management, I have integrated this database module to enable the storage and retrieval of encrypted content in a safe and secure manner using an sqlite3 database

Ensuring that the encrypted data remains organized and readily accessible to anyone with the right key. Any content going in must be encrypted with a key that you must keep off grid.

**Note** that in `Database.py` I'm using `dataclasses` module which was introduced in `python 3.7`, so make sure to install it if you have an older version.

### Usage ## 
In the module I'm providing built-in functions to make it easier to perform usual queries on Sqlite tables , by default it creates a table `Classified` with two deafult columns :

**content** : This can be a single character or a whole movie in binary, that depends on your specific needs.

**key** : This key column wasn't indeed meant to store a key itself but rather store a reference to the actual key. The key itself should be stored somewhere else safe and secure preferrably off-grid and completely seprerate from any vulnerable devices, you can even write it down on a piece of paper if you want , just make sure to rotate your keys from time to time.

1) Create a connection to the database :
```python
connect = Database('test.db')
```
This would automatically set the default table name to `Classifed` if no arguments are passed to the other class functions then they would all be working on the default table name , if you want to set your default table name instead of `Classified` you can pass your table name as the second argument : 
```python
connect = Database('test.db','MyDefaultTable')
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
query = 'SELECT COUNT(*) AS cc ,content FROM Classified WHERE key = "#5482A" ORDER BY cc DESC '
print(connect.query(query))
```
The result fetched should look like this : 
 ```python
[{'query 0': ['SUCCESS', [(1, 'some encrypted content of bytes or strings')]]}]
```
If some error has occurred while doing a query like : 
```python
query = 'SELECT COUNT(*) AS cc ,content FROM DoesntExist WHERE key = "#5482A" ORDER BY cc DESC '
```
The result fetched should look similar to this : 
```python
[{'query 0': ('FAILURE', 'no such table: DoesntExist')}]
```
Thats it so simple !

## License ##
This project is licensed under the [MIT LICENSE](https://github.com/AshGw/AES-256/blob/main/LICENSE).
## Acknowledgments ##
This cryptographic scheme is inspired by secure cryptographic practices and various open-source implementations.

