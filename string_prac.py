# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 11:13:33 2016

@author: Somak
"""
import numpy as np

def isCharUnique(word): #checks if all the characters in a string are unique

    if type(word) is not str:
        return "error: not a string"
    elif len(word)==1:
        return True
    
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

def isPermut(A, B): #checks if two words are permutations of one another
    if type(A) is not str or type(B) is not str:
        return "error: one or both aren't strings"

    A = list(A)
    B = list(B)
    
    if len(A)!=len(B): return False
    
    a = 0
    while a < len(A):
        b = 0
        while b < len(B):
            if A[a]==B[b]: 
                B.pop(b)
                break
            b += 1
        a += 1
    
    if len(B)!=0: return False
    return True
    
def urlIfy(string): #replaces spaces with %20 like in urls
    if type(string) is not str:
        return "error: not a string" 

    i = 0
    while string[len(string)-1]==" ":
        string = string[:-1]
        i += 1
    
    a = string.replace(" ", "%20")

    return a
    
def string_reverse(string): #returns a string in reverse
    if type(string) is not str:
        return "error: not a string"

    i = 0
    ans = ""
    while i < len(string):
        ans = ans + string[len(string)-1-i]
        i += 1
    
    return ans

def levenstein(first, second): #checks if strings are a letter off
    if type(first) is not str or type(second) is not str:
        return "error: one or both aren't strings"

    i = 0
    edit = 0
    
    if abs(len(first) - len(second)) > 1:
        return False
    
    if len(first) == len(second):
        while i < len(first):
            if first[i] != second[i]:
                edit += 1
            if edit > 1:
                return False
            i += 1
    else:
        length = min(len(first), len(second))
        i = 0
        while i < length:
            if first[i] != second[i]:
                if first[i:] == second[i+1:] or first[i+1:] == second[i:]:
                    return True
                else:
                    return False
            i += 1
    
    return True
    
def palindrome(word): #checks if a word is a palindrome
    if type(word) is not str:
        return "error: not a string"
    
    i = 0
    while i < 1+len(word)/2:
        if word[i] != word[len(word)-i-1]:
            return False
        i += 1
    return True