# Unix Lab Assignment

A Caesar cipher is one of the simplest techniques for data encryption and decryption. The idea of a Caesar cipher is this: you encode a message by shifting each letter some number of places. Thus, if the shift is 2, then A becomes C, B becomes D, and so on. This is a basic project for my UNIX Lab class, designed to me practice using: vi, git, github, and a compiler from the CLI. 


# Assignment Requirements

- Accept the amount to shift (i.e. 2, in the example above) as an input to your main method. You can do this by using sys.argv in python, and main(argc, argv) in C and C++.
- 
- Read (type) in a message from the keyboard (Stdin). The message will consist of one line, which your program will see as a String.
- Convert the message to all uppercase.
- 
- Encode each letter by shifting it the right amount (as shown above). Discard all the punctuation marks, digits, blanks, and anything else from the input string. Your program should only handle letters ‘A’ thru 'Z’.
- 
- Print the final encoded message in blocks of five letters to the screen (stdout), ten blocks per line. The last line may be shorter than five blocks, and the last block may be shorter than five letters.

# How To Run Code Using Input From A File

In order to run your code with input from a file versus having to type from the keyboard, you will use the shell operator < to redirect a file to replace standard input (stdin). Assuming your non-encrypted input is in a file plaintext, you would encrypt it by calling your code and passing the key (i.e. the shift amount) in the following format: "$python3 mycipher.py 3 < words". This command would shift your text by 3.

If you want to also save the encrypted text to a file versus having it print to the screen, you could redirect the output to a file cryptedtext using the shell operator > following this format: "$python3 mycipher 3 < words > cryptedtext". 








