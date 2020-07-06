# Purpose and Disclaimer

The purpose of this repository is for education only and I will not be held liable for any damage done to your computer or others computers. Nor will I be held liable for any criminal use of the files herein. By using any of the files contained in this repository you are accepting responsibility for any consequences that may be incurred. Use are your own risk.

## Files

**zip_crack.py**: 

This python script does two things performs a dictionary attack on an encrypted zip file and generates password lists for a dictionary attack. Presently there are no password lists included google password lists and you will find a plethora of lists to download. Or you can generate you own lists, the choice is up to you. All password list files must have the form filename.txt and be placed in the pw_lists folder. There is no need to specify which dictionary to use just select Dictionary Attack from the menu and it will run a Dictionary attack on the zip file contained in the target folder. If there are multiple password lists in the pw_lists folder it will loop through the lists until a password is found or it has gone through all the lists.

The generate_word_list function does just that, generate a list of words using the character set you specify and the length you specify. 

For example: The included target file locked.zip has a password length of 4 all lower case. You can generate a password list of only 4 characters with every combination possible in a relatively short time. Just select Generate Word List from the menu and make the following choices from the prompts:

Lower bound, press 4
Upper bound, press 5
Choose alphabet, press a

This will generate a lower case word list four characters long from aaaa to zzzz. You will see some progress statistics time in seconds and the passwords being generated. When done you will be asked if you want to commence the dictionary attack, pressing y will start the attack on the zip file in the target folder. Once the password is found it will extract the contents of the zip folder and output the password to the screen and a file.

The dictionary attack also outputs to a log file where you can view the dictionaries used in the attack. 

**combine_files.py**:

This script was more of an after thought all it does is combine password lists into one file. 

### Limitations

I have discovered the hard way that super large word lists are not really desirable. In my testing of the dicitonary attack I had a 9GB password list and it froze my computer. The same list split into 500MB chunks words worked quite well for me, you may have different results depending upon your machine. 