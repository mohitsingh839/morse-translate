#!/usr/bin/python3

MORSE_DICT = {
   '.':'.-.-.-', 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   'a':'.-', 'b':'-...', 'c':'-.-.', 
   'd':'-..', 'e':'.', 'f':'..-.', 
   'g':'--.', 'h':'....', 'i':'..', 
   'j':'.---', 'k':'-.-', 'l':'.-..', 
   'm':'--', 'n':'-.', 'o':'---', 
   'p':'.--.', 'q':'--.-', 'r':'.-.', 
   's':'...', 't':'-', 'u':'..-', 
   'v':'...-', 'w':'.--', 'x':'-..-', 
   'y':'-.--', 'z':'--..', '1':'.----', 
   '2':'..---', '3':'...--', '4':'....-', 
   '5':'.....', '6':'-....', '7':'--...', 
   '8':'---..', '9':'----.', '0':'-----', 
   ', ':'--..--', '?':'..--..', '/':'-..-.', 
   '-':'-....-', '(':'-.--.', ')':'-.--.-'
}

#Function for encrypting the message

def encryption(message):
   
   my_cipher = '' #Creating the blank string
   
   for letter in message:
      if letter != ' ':
         if letter in MORSE_DICT:
            my_cipher += MORSE_DICT[letter] + ' '
      else:
         my_cipher += ' '

   return my_cipher

#Main function where magic happens

def main():
   my_message=str(input("Enter Your message : "))
   
   output=encryption(my_message)
   
   print(f"\n{my_message} : {output}")

#Calling the main function

if __name__ == '__main__':
   main()
