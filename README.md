# Cryptography w/ AES-256
##  Objective ## 
#### Enhanced Security, Simplicity & Ease of use For Everyone And Anyone Willing To Use AES 256.
## Reason Behind It

Individual **Freedom** has become a rare commodity in a world dominated by control, surveillance, and constant privacy violation.
This led me to develop a way to work with a set of tools in Python , levereging the AES-256 algorithm  to make it easier for individuals to safeguard their data without blindly relying on third parties to do it for them , while at the same time making it easy for anyone with a limited programming knowledge to work with.

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

<br>The first one has a simple straight forward apporach for dealing with sqlite3 databases, even if youre not familiar with Python itself you can still use this module to run SQL queries to perform various operations on a given database, check [AshDatabase](https://github.com/AshGw/CryptographyAES-256#ashdatabase) header to learn more.

<br>The second one is using an Object-Relational Mapping (ORM) approach. It is designed for those who are already familiar with ORM concepts. It provides a higher-level abstraction for interacting with databases not only sqlite3 databases.
you can check the [AshDatabaseORM](https://github.com/AshGw/CryptographyAES-256#ashdatabaseorm) header for more info.

## Installation ##
1) Clone the repository : 
```bash
git clone https://github.com/AshGw/CryptographyAES-256.git
```
2) Install the necessary libraries 
```bash
pip install requirements.txt
```


## Ash Module ##
The Ash.py module is a comprehensive collection of carefully designed functions and code modules that facilitate optimal performance and reliability in data encryption and decryption operations  while ensuring the utmost security and 
confidentiality.

<br>It uses primitives from the cryptography.py with added security features while keeping it simple and highly flexible to provide a head-ache free solution for developers. You can check [Features](##Features) tag below to learn more about the security features.
<br>

### Usage ##
1) Generate a key if you don't have one already
```python
mainkey = Enc.genMainkey()
```
2) Before encrypting or decrypting anything, first set the arguments you want to pass, you can have an encrypted message or a  decrypted message , and a mainkey to use.
```python
mainkey = 'd5d717f57933ad21725888d3451a9cd7a565dfda677fe92fd8ff9e9c3a36d1496af58c17de2b77d4d3ea6d8791b27350fea0af3ad2610d38c8cb12a29fda4bcf'
str_normal_message = 'Hello There'
bytes_normal_message = b'Hello There'
encrypted_message_str = 'ZEfikRiNQ4EE1y5E-Qn4gQbo8goVpWLPstqTlgWtoRq1CK_oeMz4oelCYNpM-NZyzSIKk7DazkAUO9HcZJzWWMXR6zqRjNTN-c1Q6vRWSkj1g20oL6JbzUvEJL3xvY2-Fye1simoOAr7YP5YHAnSYAAAADIA0juak_JYQnzXQ-apJ8azahvngigFrHRg142g7OqvfA=='
encrypted_message_bytes = b'dG\xe2\x91\x18\x8dC\x81\x04\xd7.D\xf9\t\xf8\x81\x06\xe8\xf2\n\x15\xa5b\xcf\xb2\xda\x93\x96\x05\xad\xa1\x1a\xb5\x08\xaf\xe8x\xcc\xf8\xa1\xe9B`\xdaL\xf8\xd6r\xcd"\n\x93\xb0\xda\xce@\x14;\xd1\xdcd\x9c\xd6X\xc5\xd1\xeb:\x91\x8c\xd4\xcd\xf9\xcdP\xea\xf4VJH\xf5\x83m(/\xa2[\xcdK\xc4$\xbd\xf1\xbd\x8d\xbe\x17\'\xb5\xb2)\xa88\n\xfb`\xfeX\x1c\t\xd2`\x00\x00\x002\x00\xd2;\x9a\x93\xf2XB|\xd7C\xe6\xa9\'\xc6\xb3j\x1b\xe7\x82(\x05\xact`\xd7\x8d\xa0\xec\xea\xaf|'
```
3) Now pass these arguments accordingly. If you have a normal message and you try to decrypt it, an Exception will be raised so pass the arguments to the right classes. So first create an instance of either the Enc or Dec class. 
```python
encryption_instance = Enc(message=str_normal_message, mainkey=mainkey)
```
4) Ok now you're encrypting a string type message using the specified mainkey. 
<br>What type you want the output to be in ?
<br>You can choose to encrypt it to bytes or to strings.
```python
the_output = encryption_instance.encToBytes()
```
```python
the_output = encryption_instance.encToStr()
```
That simple, that's it.
