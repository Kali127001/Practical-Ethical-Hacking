#!/bin/python3

def who_am_i(): # this is a function without parameters.
    name = "Kali"; # local variable
    age = 18;
    print("My name is " + name + " and I am " + str(age) + " years old.");

who_am_i();

def add_one_hundred(num):
    print(num + 100);

add_one_hundred(100);

def add(x, y):
    print(x + y);

add(20, 40);

def multiply(x, y):
    return x * y;

print(multiply(7, 7));

def square_root(x):
    print(x ** .5);

square_root(int(64));
