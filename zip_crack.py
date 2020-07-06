import zipfile
import os
import glob
import itertools
import time

#Password list go here.
all_pw_lists = glob.glob('pw_lists/*.txt')

#The target file goes here
zp = glob.glob('target/*.zip')[0]
zp = zipfile.ZipFile(zp)

'''
sys_clear function detects the OS and then sends the correct 
command to clear the screen.
'''
def sys_clear():
    if os.uname().sysname == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def dictionary_attack(zp):
    print("\n")
    count = 1

    all_data = ''
    for f in all_pw_lists:
        with open('pw_list.log', 'a') as nf:
            nf.write(f + '\n')
        with open(f, 'rb') as txt:
            for entry in txt.readlines():
                
                try:
                    #If pw found extract the files
                    #TODO: Set a default directory to extract files to.
                    zp.extractall(pwd=entry.strip())
                    #Make password into a string
                    all_data = entry.decode("utf-8")
                    break
                except:
                    #Show progress statitistics
                    number = count
                    os.sys.stdout.write('Number of Passwords: %s\r' % (number))
                    os.sys.stdout.flush()
                    count += 1
                    pass
    sys_clear()
    print(f'Password found! {all_data}')
    #Write the password to a file
    with open('found_pw.txt', 'w') as found:
        found.write(all_data)


def generate_word_list(zp, lower, upper, alpha):
    #Define character sets
    l_case =('abcdefghijklmnopqrstuvwxyz')
    u_case = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    nums = ('0123456789')
    s_chars = ('_.-!@*$?&%')

    #Alphabet to use for dictionary generation
    Alphabet = ''

    #Declare an empty variable for dictionary name
    dict_name =''

    #Auto dictionary file naming and fill Alphabet
    if upper - 1 == lower:
        dict_name = str(lower) + '_'
    elif upper - 1 > lower:
        dict_name = str(lower) + '_' + str(upper - 1) + '_'
    
    if alpha == 'a':
        Alphabet = l_case
        dict_name += 'lower_case'
    elif alpha == 'b':
        Alphabet = u_case
        dict_name += 'upper_case'
    elif alpha == 'c':
        Alphabet = nums
        dict_name += 'numbers'
    elif alpha == 'd':
        Alphabet = s_chars
        dict_name += 'special_chars'
    elif alpha == 'e':
        Alphabet = l_case + u_case
        dict_name += 'lower_upper'
    elif alpha == 'f':
        Alphabet = l_case + nums
        dict_name += 'lower_numbers'
    elif alpha == 'g':
        Alphabet = l_case + s_chars
        dict_name += 'lower_special'
    elif alpha == 'h':
        Alphabet = l_case + u_case + nums + s_chars
        dict_name += 'all_chars'

    start = time.time()

    counter = 1

    CharLength = lower
   
    dictionary = 'pw_lists/' + dict_name + '.txt'
    print("\n")

    for CharLength in range(lower, upper):
        #Generate the password combinations
        passwords = (itertools.product(Alphabet, repeat=CharLength))

        for i in passwords:
            counter += 1
            i = str(i)
            #Remove unwanted characters
            i = i.replace("[", "")
            i = i.replace("]", "")
            i = i.replace("'", "")
            i = i.replace(" ", "")
            i = i.replace(",", "")
            i = i.replace("(", "")
            i = i.replace(")", "")

            try:
                #Display progress statistics
                os.sys.stdout.write('Seconds: %s pw: %s\r' % (int(time.time() - start), i))
                os.sys.stdout.flush()
                #Append to the dictionary file
                with open(dictionary, 'a') as dict:
                    dict.write(i + '\n')
            except:
                pass
    sys_clear()
    print('Done!\n')

    attack = input('Do you want to commence a dictionary attack? y/n')

    if attack == 'y':
        sys_clear()
        dictionary_attack(zp)
    else:
        sys_clear()
        print('Thank you your password list/s are in the pw_list folder')

def menu():
    sys_clear()
    ans = input('1: Dictionary Attack\n2: Generate Word List ')

    if ans == '1':
        sys_clear()
        dictionary_attack(zp)

    else:

        lower = int(input('Specify the lowest # of pw chars, example 4:\n'))
        upper = int(input('Specify the highest # of pw chars, example 10:\n'))
        alpha = input('Choose alphabet:\na. Lower\nb. Upper\nc. Numbers\nd. Special\ne. L + U\nf. L + N\ng. L + S\nh. All\n')
        sys_clear()
        generate_word_list(zp, lower, upper, alpha)
