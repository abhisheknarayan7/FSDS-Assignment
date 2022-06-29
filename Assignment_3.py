{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "2fb1d103",
   "metadata": {},
   "source": [
    "1. Why are functions advantageous to have in your programs?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d05da25",
   "metadata": {},
   "outputs": [],
   "source": [
    "Function makes code reusability easy.\n",
    "Reduces duplicacy of code\n",
    "we can call it as many times as we need\n",
    "we can make complex program into a function and use it easily\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c9d517f0",
   "metadata": {},
   "source": [
    "2. When does the code in a function run: when it's specified or when it's called?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e904d809",
   "metadata": {},
   "source": [
    "When it is called"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f85fd716",
   "metadata": {},
   "source": [
    "3. What statement creates a function?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "83d3dd8a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def func_name():"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9a22cf9f",
   "metadata": {},
   "source": [
    "4. What is the difference between a function and a function call?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a1850b0d",
   "metadata": {},
   "outputs": [],
   "source": [
    "A function is a program that does specified operation\n",
    "whereas a function call is use to initiate the program within a functiom."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bd9c31a1",
   "metadata": {},
   "source": [
    "5. How many global scopes are there in a Python program? How many local scopes?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3bc61716",
   "metadata": {},
   "outputs": [],
   "source": [
    "There is one global function in python and one local scope in python."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "628e67a6",
   "metadata": {},
   "source": [
    "6. What happens to variables in a local scope when the function call returns?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b1e756a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "Variable gets destroyed and undefined"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b88790c",
   "metadata": {},
   "source": [
    "7. What is the concept of a return value? Is it possible to have a return value in an expression?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d17845b",
   "metadata": {},
   "outputs": [],
   "source": [
    "A return value in a statement ends the function call and return the given value.\n",
    "Yes it is possible to have a return value in an expression because everything in Python is an object."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8e91ca94",
   "metadata": {},
   "source": [
    "8. If a function does not have a return statement, what is the return value of a call to that function?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "796783b0",
   "metadata": {},
   "outputs": [],
   "source": [
    "It will return nothing and return yo the main function"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "52e5c5f4",
   "metadata": {},
   "source": [
    "9. How do you make a function variable refer to the global variable?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65b078e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "By using 'Global' word with the variable we wish to make global"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9b726bc2",
   "metadata": {},
   "source": [
    "10. What is the data type of None?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "afb69130",
   "metadata": {},
   "outputs": [],
   "source": [
    "NoneType"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "afbfc78f",
   "metadata": {},
   "source": [
    "11. What does the sentence import areallyourpetsnamederic do?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3a544c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "It will give error that to such module is available in python"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c2cdeed9",
   "metadata": {},
   "source": [
    "12. If you had a bacon() feature in a spam module, what would you call it after importing spam?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b017ed9d",
   "metadata": {},
   "outputs": [],
   "source": [
    "spam.bacon()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f4247e4c",
   "metadata": {},
   "source": [
    "13. What can you do to save a programme from crashing if it encounters an error?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a4cf2bf0",
   "metadata": {},
   "outputs": [],
   "source": [
    "Stop the kernel\n",
    "Use try and except"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0a59269e",
   "metadata": {},
   "source": [
    "14. What is the purpose of the try clause? What is the purpose of the except clause?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "616338b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "Try clause used to test the error in code\n",
    "Except clause used to handle the error in code"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
