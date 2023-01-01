''' Write a Python program to compute following operations on String:
a) To display word with the longest length
b) To determines the frequency of occurrence of particular character in the string
c) To check whether given string is palindrome or not
d) To display index of first appearance of the substring
e) To count the occurrences of each word in a given string '''

#To display word with the longest length
def longest_word():
    str=input("Enter a string")
    l1=str.split()
    print(l1)
    m=0
    word=0
    for i in range(len(l1)):
        len(l1[i])
        if m<len(l1[i]):
            m=len(l1[i])
            word=i
    print("Longest word - ",l1[word])
longest_word()

#To determines the frequency of occurrence of particular character in the string
def fre_char():
    str='Hello'
    char='l'
    cnt=str.count(char)
    print("Frequency of occurence of char - ",cnt)
fre_char()

#To check whether given string is palindrome or not
def pali():
    str='madam'
    print("Word is - ",str)
    rev=reversed(str)
    if list(rev)==list(str):
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
pali()

#To display index of first appearance of the substring
str='Python programming network programming'
sub='prog'
index=str.find(sub)
print(index)

