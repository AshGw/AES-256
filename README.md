# Cryptography
If you're running Python 3.7 or newer you're good to go. 
Simply hit the terminal and run the command "pip install -r Requirements.txt" all the necessary libraries should be installed.

Simple and easy to use just follow through, you can either encrypt/decrypt text or files. If you want to save the content you've enctypted/decrypted
and keep a log you can use AshDatabase.py module to register your content with the according keys, this module uses dataclasses module which 
was introduced in Python 3.7, so make sure to install it if you have a version older than 3.7.

the qr.py module is used to display a qr code of either the key or the encrypted message, here im using it to display the encrypted message so it 
can be quickly scanned and transmitted , you can switch between qr versions from 1 and 40 , although I recommend using 40 since it can take the most amount 
of characters.

you can use the AshCryptGUI.py , it's merely a GUI to encrypt and decrypt a text of maximum length = 200 characters and also display the qr representation 
of the encrypted message.
