try:
    import pyperclip  #pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, it does nothing.
 
 # Every possible symbol that can be encrypted/decrypted:
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
print('Welcome to Ceaser Cipher by Yasir')
print('Decode any text you want!')
print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

 # Asks the user if they are encrypting or decrypting:
 # While loop used to keep asking until the user enters e or d.
while True:  
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')
 
 #Asks the user which key they want to use:
 #Keeps asking until the user enters a valid key.
while True:  
    maxKey = len(LETTERS) - 1
    print('Please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(LETTERS):
        key = int(response)
        break
 
 #Lets the user input the message to encrypt/decrypt:
print('Enter the message to {}.'.format(mode))
message = input('> ')
 
 #Caesar cipher only works on uppercase letters:
message = message.upper()
 
 #Stores the encrypted/decrypted form of the message:
translated = ''
 
 #Encrypts/decrypts each letter in the message:
for symbol in message:
    if symbol in LETTERS:
        # Gets the encrypted (or decrypted) number for this symbol.
        num = LETTERS.find(symbol)  # Get the number of the symbol.
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
 
         # Handles the loop hole if num is larger than the length of
         # Letters or less than 0:
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)
 
         # Adds the encrypted/decrypted number's symbol to translated:
        translated = translated + LETTERS[num]
    else:
         # Just adds the symbol without encrypting/decrypting:
        translated = translated + symbol
 
# Displays the encrypted/decrypted string to the screen:
print(translated)
 
try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass  # Do nothing if pyperclip wasn't installed.