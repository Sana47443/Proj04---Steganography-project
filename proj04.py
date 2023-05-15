#####################################################################################################################################################################################
#  Computer Project #4
#
#  Algorithm
#    import required modules
#    writing function definition of the function numtobase() which has 2 required arguments N and B and returns the same number in the base the user asked for
#    writing function definition of the function basetonum() which has 2 required arguments S and B and returns the same value in decimal integer form
#    writing function definition of the function basetobase() which basically utilizes the above two functions to convert a value in a given base to the user inputted required base
#    writing function definition of the function encode_image() which embeds a secret text message and returns an image with the text
#    writing function definition of the function decode_image() which extracts the text message from the image
#    writing function definition of the function planet_menu() and it prints the menu
#    writing function definition of the function valid_base()  which does not leave the user until the user enters a valid one
#    writing function definition of the main function which calls all the above functions
######################################################################################################################################################################################    

import math       #importing math module

def numtobase(N,B):
    '''
    Converts decimal integer(in base 10) into a base as requested by the user
    Parameters
    ----------
    N : String
        The decimal integer
    B : String
        The base to which the user wants the value to be converted to
        
    Returns
    -------
    String
        if the user inputs the nuber as zero, it returns an empty string
        else it returns the computed value in the required base as a string
    '''
    if N==0:
        return ""
    else:
        des_base_rev=""
        num=N
        while num!=0:     #a while loop to loop until the function finds the 
            remainder=num% B      #the remainders and concatenate them all into 
            des_base_rev+=str(remainder)  #a variable
            num=num//B
        des_base=des_base_rev[::-1]  #reversing it
        des_len=math.ceil(len(des_base)/8) #using math.ceil() function to 
        if des_len==0:     #find the closest multiple of 8 which is higher   
            des_base=des_base.zfill(8)  #using .zfill() accordingly
        else:
            des_base=des_base.zfill(des_len*8)
        return des_base


def basetonum(S,B):
    '''
    Converts a value in a different base to base 10(decimal integer)
    Parameters
    ----------
    S : String
        It is the value in a different base which the user wants to convert to
        base 10
    B : String
        It is the value of base in which the string is inputted
        
    Returns
    -------
    0
      If the inputted value of S is an empty string
    Integer
      Which is in the base 10
    '''
    if S=="":      #an if condition to check if the user has enteres S as an 
        return 0   #empty string
    else:
        s_rev=S[::-1]   #reversing the string
        dec_no=0
        for i in range(len(s_rev)):
            dec_no+=int(s_rev[i])*(B**i) #doing it accordingly
        return dec_no
    
def basetobase(B1,B2,s_in_B1):
    '''
    Converts a value in base(in a different base to another base.
    It calls 2 functions within it: 1) basetonum() to convert the recieved 
    valu to base 10 and 2) numtobase() to convert the previously converted 
    value in base 10 to the required base as asked by the user.
    Parameters
    ----------
    B1 : String
        It is the base which the user has entered the value s_in_B1 in
    B2 : String
        It is the base to which the user asked the program to convert it into
    s_in_B1 : String
        It is the value which the user wants to be converted to another base

    Returns
    -------
    String
        It returns the computed value in base 2
    '''
    dec=basetonum(s_in_B1, B1)  #using both the above functions to convert 
    new_n=numtobase(dec,B2)     #from base1 to num and then num to base2
    return new_n
 
def encode_image(image, text, N):
    '''
    Embeds a secret text message into the given image as inputted by the user.
    Parameters
    ----------
    image : String 
        It is the image(in binary) in which the secret text has to be embedded
    text : String
        It is the secret image which has to be embedded
    N : Integer
        It gives details about the number of bits in a pixel

    Returns
    -------
    String
        If the image inputted by the user is an empty string, then return an empty string
        If the text to be embedded in the image is an empty string, the return the image itself
        If none of the above, then return the image with the text message embedded

    '''
    if image=="":  #an if condition ccordingly to check if image is an empty
        return ""  #string
    elif text=="":   #this is to check if the text is an empty string
        return image  #then just return the original image
    else:
        img_len=len(image)   
        bin_num=""
        for val in text:
            temp_b= ord(val)     #ord() function being used
            temp_bin=numtobase(temp_b,2)
            bin_num+=temp_bin       #here computing the string in binary to be 
                                    #embedded in the image
        if len(bin_num)>img_len:  #to check if the message will fit in or not
            return None
        else:
            encoded_img=image
            x=0
            for i in range(N-1, len(image),N):   #replacement of the original
                if x<len(bin_num) and image[i]!=bin_num[x]: #characters with 
                    temp_img=image[i:]            #secret text message happening
                    temp_img=temp_img.replace(image[i],bin_num[x],1) #here
                    encoded_img=encoded_img[:i]+temp_img
                x+=1
            return encoded_img

def decode_image(stego, N):
    '''
    It extracts the hidden message from the image

    Parameters
    ----------
    stego : String
        It is the image with the secret text embedded.
    N : Integer
        It gives details about the number of bits in a pixel.

    Returns
    -------
    String
        Returns the hidden text message from the image

    '''
    pro_string=""
    for j in range(N-1,len(stego),N):  #extracting the binary version of 
        pro_string+=stego[j]           #the secret text
    counter=0
    hid_word=""
    for ch in range(8,len(pro_string)+1,8): #step by step finding the hidden 
        word=pro_string[counter:ch]        #text by taking one by one 8 length
        counter=ch             # its and converting to deciaml integer and then
        calc_num=basetonum(word,2)      #using chr() to find the character and 
        char=chr(calc_num)            #concatenating
        hid_word+=char
    return hid_word

def planet_menu():
    '''
    It prints the menu and all of it's options

    Returns
    -------
    None.

    '''
    print("\nPlease choose one of the options below:")   #printing menu and options
    print("             A. Convert a decimal number to another \
base system         ")
    print("             B. Convert decimal number from another \
base.")
    print("             C. Convert from one representation system \
to another.")
    print("             E. Encode an image with a text.")
    print("             D. Decode an image.")
    print("             M. Display the menu of options.")
    print("             X. Exit from the program.")

def valid_base(inp_base):
    '''
    It does not leave until the user enters a valid base(loops until that)

    Parameters
    ----------
    inp_base : String
        It is the base inputted by the user

    Returns
    -------
    String
        It returns a valid base

    '''
    if int(inp_base)<2 or int(inp_base)>10:
        print("\n\tError: {} was not a valid integer between 2 and 10 \
inclusive.".format(inp_base))     #checks if base is between 2 and 10 or not
        while True:            #it will not leave until user enters a valid one 
            inp_base=input("\n\tEnter Base: ")
            if int(inp_base)<2 or int(inp_base)>10:
                print("\n\tError: {} was not a valid integer between 2 and \
10 inclusive.".format(inp_base))  #keeps printing  error statement until a 
            else:                 #valid one is inputted
                break   
    return inp_base
def main():
    '''
    It prints the banner
    It is the main function which calls all the other functions according to the options as inputted by the user
    It loops until the user volunteerly wants to exit
    
    Returns
    -------
    None.

    '''
    x=0  #now this acts like a check to know for which options to ask input again
    BANNER = '''
               A long time ago in a galaxy far, far away...   
              A terrible civil war burns throughout the galaxy.      
  ~~ Your mission: Tatooine planet is under attack from stormtroopers,
                   and there is only one line of defense remaining        
                   It is up to you to stop the invasion and save the planet~~
    '''
    print(BANNER)      #printing banner
    planet_menu()      #calling planet_menu() function to print menu
    while True:        #A while loop which loops until it's false(Boolean False)
        if x==0:
            choice=input("\n\tEnter option: ")  #choice of the user inputted
        if choice not in "ABCEDMXabcedmx":      #if invalid,we go into this 
            print("\nError:  unrecognized option [{}]".format(choice.upper()))
            planet_menu()
            while True:        #prompt until user enters a valid one
                choice=input("\n\tEnter option: ")
                if choice not in "ABCEDMXabcedmx":
                    print("\nError:  unrecognized option \
[{}]".format(choice.upper()))  #and tis error is printed
                    planet_menu()  #menu options displayed
                else:
                    x=None
                    break
        elif choice.upper()=="M":  #this option is to display th menu
            planet_menu()
            choice=input("\n\tEnter option: ")
            x=None
        elif choice.upper()=="X":  #this one is to exit the loop
            print('\nMay the force be with you.')
            break
        elif choice.upper()=="A":  #this one is for decimal number to another base
            x=0
            number=input("\n\tEnter N: ")
            if number.isdigit()==False:  #error checking if not digit
                print("\n\tError: {} was not a valid non-negative \
integer.".format(number))
                while True:        #prompt until user enters a valid one     
                    number=input("\n\tEnter N: ")
                    if number.isdigit()==False:
                        print("\n\tError: {} was not a valid non-negative \
integer.".format(number))
                    else:
                        break
            inp_base=input("\n\tEnter Base: ") #for a valid base below
            input_base=valid_base(inp_base)   #function calling here
            if number.isdigit()==True and (int(input_base)>=2 and \
                                           int(input_base)<=10):
                num_base=numtobase(int(number),int(input_base))
                print("\n\t {} in base {}: {}".format(number,\
                                input_base,num_base)) #printing final
        elif choice.upper()=="B":  #this option from another base to decimal integer
            x=0
            str1=input("\n\tEnter string number S: ") #getting all inputs
            inp_base=input("\n\tEnter Base: ")
            input_base=valid_base(inp_base) #for a valid base.....
            base_num=basetonum(str1,int(input_base))
            print("\n\t {} in base {}: {}".format(str1,input_base,base_num))
        elif choice.upper()=="C": #this one for conversion from some base to some 
            x=0                   #other base
            base_1=input("\n\tEnter base B1: ")
            if int(base_1)<2 or int(base_1)>10:  #valid base checking for B1
                print("\n\tError: {} was not a valid integer between \
2 and 10 inclusive.".format(base_1))
                while True:
                    base_1=input("\n\tEnter base B1: ")
                    if int(base_1)<2 or int(base_1)>10:
                        print("\n\tError: {} was not a valid integer \
between 2 and 10 inclusive.".format(base_1))
                    else:
                        break               
            base_2=input("\n\tEnter base B2: ")
            if int(base_2)<2 or int(base_2)>10: #valid base checking for B2
                print("\n\tError: {} was not a valid integer between \
2 and 10 inclusive.".format(base_2))
                while True:
                    base_2=input("\n\tEnter base B2: ")
                    if int(base_2)<2 or int(base_2)>10:
                        print("\n\tError: {} was not a valid integer \
between 2 and 10 inclusive.".format(base_2))
                    else:
                        break               
            str2=input("\n\tEnter string number: ")
            base_num_base=basetobase(int(base_1),int(base_2),str2) #conversion happening
            print("\n\t {} in base {} is {} in base \
{}...".format(str2,base_1,base_num_base,base_2)) 
        elif choice.upper()=="E":   #This one for encoding secret text into img
            x=0
            bin_str=input("\n\tEnter a binary string of an image: ")
            n_pix=input("\n\tEnter number of bits used for pixels: ")
            secret_txt=input("\n\tEnter a text to hide in the image: ")
            enc_img=encode_image(bin_str,secret_txt,int(n_pix))#function-calling
            if enc_img==None or enc_img=="": #for other appropriate cases
                print("\n\tImage not big enough to hold all the text \
to steganography")
            else:
                print("\n\t Original image: {}".format(bin_str)) #if normal,this
                print("\n\t Encoded image: {}".format(enc_img))
        elif choice.upper()=="D":  #This one for decoding the secret text from img
            x=0
            secret_img=input("\n\tEnter an encoded string of an image: ")
            n_bits=input("\n\tEnter number of bits used for pixels: ")
            dec_text=decode_image(secret_img,int(n_bits))#function-calling   
            
            print("\n\t Original text: {}".format(dec_text)) #printing final

if __name__ == '__main__': #appropriate method of calling- if satisfied
    main()
