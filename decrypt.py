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
