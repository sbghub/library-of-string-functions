# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 11:13:33 2016

@author: Somak
"""
import numpy as np
import unittest

#(1.) checks if all the characters in a string are unique
def isCharUnique(word): 
    #tries to convert word to a string if it isn't one
    if type(word) is not str:
        try:
            word = str(word)
        except:
            return "error: not a string and couldn't convert to one"
    elif len(word)==1:
        return True
    
    #runs through each letter and checks if it matches any letters after it
    #assumes it's True and returns False if a letter matches a letter after it
    i = 0    
    while i < len(word)/2 + 1:
        j = 1
        while j < len(word):
            if i==j:
                j += 1
            if word[i]==word[j]:
                return False
            j += 1
        i += 1
        
    return True

#(2.) checks if two words are permutations of one another
def isPermut(A, B): 
    #returns error message if A and B aren't strings
    if type(A) is not str or type(B) is not str:
        return "error: one or both aren't strings"

    A = list(A)
    B = list(B)
    
    #returns False if they aren't the same length
    if len(A)!=len(B): return False
    
    #tries to match each letter in A to the letters left in B
    #pops matching letters in B 
    #moves onto the next letter in A when there's a match or if A went through all the letters in B
    a = 0
    while a < len(A):
        b = 0
        while b < len(B):
            if A[a]==B[b]: 
                B.pop(b)
                break
            b += 1
        a += 1
    
    #assumes they're permutations, returns True unless proven otherwise
    #returns False if B isn't empty / if there are any letters that didn't match form A to B
    if len(B)!=0: return False
    return True

#(3.) replaces spaces with %20 like in urls
def urlIfy(string): 
    #returns error message if string isn't a string
    if type(string) is not str:
        return "error: not a string" 

    #replace spaces with %20 and return
    a = string.replace(" ", "%20")
    return a

#(4.) returns a string in reverse
def string_reverse(string): 
    #returns error message if not a string
    if type(string) is not str:
        return "error: not a string"

    #initializes empty string ans
    #adds letters from string to ans letter by letter from back to front
    #then returns ans
    i = 0
    ans = ""
    while i < len(string):
        ans = ans + string[len(string)-1-i]
        i += 1
    
    return ans

#(5.) checks if strings are the same, or 1 letter off
def levenstein(first, second): 
    if type(first) is not str or type(second) is not str:
        return "error: one or both aren't strings"

    i = 0
    edit = 0
    
    #returns False if lengths off by more than a letter
    if abs(len(first) - len(second)) > 1:
        return False
    
    #if same length
    if len(first) == len(second):
        #checks each letter in first to corresponding letter in second
        while i < len(first):
            #increments edit for every letter off
            if first[i] != second[i]:
                edit += 1
            #returns False if edit > 1 since that means they're were more than one letter off 
            if edit > 1:
                return False
            i += 1
    #if one word is a letter longer than the other 
    else:
        #sets length to that of the shorter word and initalizes i as 0
        length = min(len(first), len(second))
        i = 0
        while i < length:
            #if letter at position i doesn't match for the two words it means that it is the off letter for either first or second
            if first[i] != second[i]:
                #if the non-discrepant letter in first matches that of second or vice versa, then return True else False
                if first[i:] == second[i+1:] or first[i+1:] == second[i:]:
                    return True
                else:
                    return False
            i += 1
    #assumes first and second are off by no more than one letter unless proven otherwise
    return True

#(6.) checks if a word or number is a palindrome
def palindrome(word):
    #tries to convert word to a string if it isn't one
    if type(word) is not str:
        try:
            word = str(word)
        except:
            return "error: not a string and couldn't convert to one" 

    #get rid of spaces, periods, and commas
    #then converts the letters to lowercase for ease of comparison
    word = word.replace(" ", "")
    word = word.replace(".", "")
    word = word.replace(",", "")
    word = word.lower()

    #checks first and last letter and each letter after and before respectively
    #stops halfway through the word
    i = 0
    while i < 1+len(word)/2:
        if word[i] != word[len(word)-i-1]:
            return False
        i += 1
    #assumes word is a plaindrome unless proven otherwise
    return True


class Tester(unittest.TestCase):
    def test_isCharUnique(self):
        self.assertEqual(isCharUnique("asdfghjkl"), True)
        self.assertEqual(isCharUnique("asdfghjkla"), False)
        self.assertEqual(isCharUnique("1234567890"), True)
        self.assertEqual(isCharUnique(1234567890), True)
    def test_isPermut(self):
        self.assertEqual(isPermut("asdfgdxgfd", "asgfdfgdxd"), True)
        self.assertEqual(isPermut("asdfgdxgfd", "asdfgdxgfds"), False)
        self.assertEqual(isPermut("asdfgexgfd", "gfdfgasdxd"), False)
    def test_urlify(self):
        self.assertEqual(urlIfy("did it work?"), "did%20it%20work?")
        self.assertEqual(urlIfy("How about  now?"), "How%20about%20%20now?")
    def test_string_reverse(self):
        self.assertEqual(string_reverse("asdfghjkl"), "lkjhgfdsa")
    def test_levenstein(self):
        self.assertEqual(levenstein("casino", "casinos"), True)
        self.assertEqual(levenstein("latino", "latina"), True)
        self.assertEqual(levenstein("Latino", "latina"), False)
        self.assertEqual(levenstein("cabino", "casinos"), False)
    def test_palindrome(self):
        self.assertEqual(palindrome("a man a plan a canal panama"), True)
        self.assertEqual(palindrome("A man a plan a canal. Panama"), True)
        self.assertEqual(palindrome("A man, a plan, a canal. Panama"), True)
        self.assertEqual(palindrome(123456654321), True)

if __name__ == '__main__':
    unittest.main()
