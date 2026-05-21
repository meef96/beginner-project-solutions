''' 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
Program description: 
99 Bottles
Create a program that prints out every line to the song "99 bottles of beer on the wall."

Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

Project Source: https://github.com/jorgegonzalez/beginner-projects#99-bottles
Author: Kathleen C
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
'''

def bottle_song(num):
    for i in range(num, 0, -1): 
        # if there is more than 1 bottle on wall, pluralize
        if i > 1:
            bottle = str(i) + " bottles"
        else:
            bottle = str(i) + " bottle"
        # set next number of bottle(s)    
        new_num = i - 1
        # if more than 1 bottle left, pluralize
        if new_num != 1:
            new = str(new_num) + " bottles"
        else:
            new = str(new_num) + " bottle"        

        print(f"{bottle} of beer on the wall, \n{bottle} of beer, \ntake one down, pass it around, \n{new} of beer on the wall!\n")

def main():
    bottle_song(99)

if __name__ == "__main__":
    main()