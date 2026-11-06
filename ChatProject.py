# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 12:08:07 2025

@author: Aaron
"""
import os
import random

def main():
    print("Welcome to this chatbot thing.")
    print("The program will talk to you to learn how to respond.")
    print("You can stop talking to it at any time by typing \"quit\".")
    print("\nNow, type out your user name below vvv")
    print("If you have already used the program this will load your progress")
    print("Or if this is your first time, it will create a conversation")
    print("Alternatively you could type \"default\" to use the shared program:")
    
    path = input("<< ").strip().lower()
    if not path.endswith(".txt"): 
        path += ".txt"
        
    if not os.path.exists(path):
        with open(path, "w") as file:
            file.write("")
        
    print("The program has loaded successfully!")
    print("You may now begin the conversation:")
    conversation(path)

   
def conversation(path):
    statement = "Hello"
    print(">> " + statement)
    response = input("<< ")
    response = ''.join(ch for ch in response if ch not in ",")
    while (response.lower() != "quit"):
        store(statement, response.split('\n')[0], path)
        statement = getStatement(response, path)
        print(">> "+ statement)
        response = input("<< ")
        response = ''.join(ch for ch in response if ch not in ",")

def store(statement, response, path):
    # Saves what it said and how the user responded
    with open(path, 'r') as file:
            arr = file.readlines()
    key = statement.split(',',1)[0].lower()
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_key = arr[mid].split(',',1)[0].lower()
        if mid_key < key:
            low = mid + 1
        elif mid_key > key:
            high = mid - 1
        else:
           arr[mid] = arr[mid].strip("\n") + ", " + response + "\n"
           with open(path, 'w') as file:
                   file.writelines(arr)
           return
    arr.insert(low, statement + ", " + response + "\n")
    with open(path, 'w') as file:
            file.writelines(arr)
        

def getStatement(statement, path):
    #Searches for previous responses to a statement
    with open(path, 'r') as file:
            arr = file.readlines()
    key = statement.split(',',1)[0].lower()
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_key = arr[mid].split(',',1)[0].lower()
        if mid_key < key:
            low = mid + 1
        elif mid_key > key:
            high = mid - 1
        else:
           return pickResponse(arr[mid])
       
    if (high < 0) or (low >= len(arr)):
            return pickResponse(random.choice(arr))        

    return pickResponse(arr[low])
    

def pickResponse(r):
    responses = (r.strip("\n")).split(', ')
    rnd = random.randint(1, len(responses) - 1)
    return responses[rnd];

    
main()