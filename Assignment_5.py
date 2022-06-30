{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e8faf875",
   "metadata": {},
   "source": [
    "1. What does an empty dictionary's code look like?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01401b11",
   "metadata": {},
   "outputs": [],
   "source": [
    "d = {}"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aeb10e8e",
   "metadata": {},
   "source": [
    "2. What is the value of a dictionary value with the key 'foo' and the value 42?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "213c8dff",
   "metadata": {},
   "outputs": [],
   "source": [
    "d1 = {'foo' : 42}"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f868aed8",
   "metadata": {},
   "source": [
    "3. What is the most significant distinction between a dictionary and a list?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc2c6117",
   "metadata": {},
   "outputs": [],
   "source": [
    "List is collection of values wheraeas Dictionary is collection of key value pair.\n",
    "list is represented in [] whereas dict is represented in {}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bfab02b4",
   "metadata": {},
   "outputs": [],
   "source": [
    "4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "dba7be8f",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'foo'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_1628/414641506.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mspam\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;34m'bar'\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;36m100\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mspam\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'foo'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m: 'foo'"
     ]
    }
   ],
   "source": [
    "spam = {'bar': 100}\n",
    "spam['foo']\n",
    "#it will give key error as shown below"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "46604fe9",
   "metadata": {},
   "outputs": [],
   "source": [
    "5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "49e12deb",
   "metadata": {},
   "outputs": [],
   "source": [
    "'cat' in spam will check whether it is present in the dictionary or not\n",
    "spam.keys() will return the key/keys present in the dictionary"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6f40d54f",
   "metadata": {},
   "source": [
    "6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70074d34",
   "metadata": {},
   "outputs": [],
   "source": [
    "'cat' in spam will check whether it is present in the dictionary or not\n",
    "spam.value() will return the value/values present in the dictionary"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dbcb7ca0",
   "metadata": {},
   "source": [
    "7. What is a shortcut for the following code?\n",
    "if 'color' not in spam:\n",
    "spam['color'] = 'black'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "330db706",
   "metadata": {},
   "outputs": [],
   "source": [
    "spam.setdefault('color', 'black')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ea839f3c",
   "metadata": {},
   "source": [
    "8. How do you \"pretty print\" dictionary values using which module and function?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e57494e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "We need to import pprint module\n",
    "We usepprint.pprint() function"
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
