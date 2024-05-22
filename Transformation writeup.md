# Transformation  
#### #reverse engineering #intro_ #picoCTF
---

## Description
> The challenge is to decode a string stored in a file called [enc](https://mercury.picoctf.net/static/a757282979af14ab5ed74f0ed5e2ca95/enc).

## Hint
> we are given both the file containing the encrypted string and the piece of code that was used to encrypt it.below is that piece of code.                           
```python

''.join([chr((ord(flag[i]) << 8) + ord(flag[i+1])) for i in rang(0,len(flag),2)])
```

## Approach
> Looking at the given code snippet I noticed two functions, `ord()` and `chr()` with the `ord` function being embedded in the `chr()` function.So I searched the two up on google and this is what I obtained. The `ord()` or ordinal fuction maps a character to its `ascii` decimal represenation.Forexample the ascii decimal representation of capital letter P is 80.
> 
┌──(gentleman㉿gentleman)-[~]  
└─$ python3          
Python 3.11.8 (main, Feb  7 2024, 21:52:08) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.  
*>>>*  ord('P')  
80

> The chr() function or character function really just undoes what the ord() function does. it maps the ascii decimal value of a character to an ascii character.
> 
┌──(gentleman㉿gentleman)-[~]  
└─$ python3          
Python 3.11.8 (main, Feb  7 2024, 21:52:08) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.  
*>>>*  chr(80)  
"P"


## Solution
> Okay. so how did i approach this challenge.Well...I  used brute force.no no..., I used reverse engineering with a little force. 

First i generated a list of possible two character combinations of ascii characters ranging from  ascii decimal value 48 to 127 as shown below in the python script that i wrote.  

```python
enc = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽"  # The encrypted string
element_list = [] 
flag_list = []  
index_list = []
flag ="" # final string
printable_chrs = [chr(i) for i in range(48,127)] # a list of printable characters in picoCTF flags

# a generator of all possible two character combinations of printable characters
for chr1 in printable_chrs:
    for chr2 in printable_chrs:
        element = chr((ord(chr1) << 8) + ord(chr2)) 
        for i in range(0,len(enc)):
            if enc[i] == element: # brute force
                flag_list.append(chr1+chr2)
                element_list.append(element)

# generator that returns a list of indexes of elements as they appear in the string enc
for value in element_list:
    if value in enc:
        index_list.append(enc.index(value))

# this organises the flag in order
for j in range(0,len(index_list)):
    flag += flag_list[index_list.index(j)]
print(flag) 
```
> Then i used part of the provided code snippet to create the  encrypted characters(referred to as elements in my code) from the possible combinations of the two ascii characters and compared each character in the encrypted string "enc" with the generated elements. if there is a match then that pair of printable ascii characters is appended to a list called flag_list. which looks like this; 
> 
 ['16', '34', '3}', '52', 'CT', 'F{', '_8', '_b', '_d', 'b9', 'c6', 'co', 'd_', 'in', 'it', 'of', 'pi', 's_', 'st']

> But notice that the pair of characters are not in order. Therefore so as to organise that list inorder and print the final flag, I created a generator that returns a list of indexes of elements as they appear in the string enc  and appends the indexes in the list called `index_list` that looks as such;  
> 
 [4, 10, 18, 15, 2, 3, 13, 5, 14, 17, 16, 1, 11, 8, 6, 12, 0, 7, 9]

> so all was left was to rearrange the pair of characters starting from index 0 to index 18 using this piece of code at the end.
```python
for j in range(0,len(index_list)):
    flag += flag_list[index_list.index(j)]
print(flag)
```
so when the code is run with the encrypted string as `enc` the flag is printed in order.


