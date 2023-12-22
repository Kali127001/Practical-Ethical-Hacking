#!/bin/python3

# variables
quote = "Everything is fair in love and war!";
print(quote);

name = "Kali"; # string
age = 18; # integer
gpa = 3.7 # float, btw I don't have any gpa

print(int(age));
print(int(30.2));
print(int(30.9)); # will it round? NO.

print("My name is " + name + ". And I am " + str(age) + " years old.");

age += 1; # age = age + 1
print(age);

birthday = 1;
age += birthday; # age = age + birthday

print(age);

# methods
print(quote.upper()); # uppercase => every word in uppercase
print(quote.lower()); # lowercase => every word in lowercase
print(quote.title()); # title case => first letter of every word in capital

print(len(quote)); # length of a string with spaces.