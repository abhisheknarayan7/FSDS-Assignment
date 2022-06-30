{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "2279bb81",
   "metadata": {},
   "source": [
    "1. What are escape characters, and how do you use them?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3703d700",
   "metadata": {},
   "outputs": [],
   "source": [
    "backslash is an escape character used with following\n",
    "\\\\ backslash\n",
    "\\n is used to insert newline\n",
    "\\t is used to insert tab\n",
    "\\b is used to enter backspace\n",
    "\\0 is used to insert null character"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1d33bac4",
   "metadata": {},
   "source": [
    "2. What do the escape characters n and t stand for?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "741b969d",
   "metadata": {},
   "outputs": [],
   "source": [
    "n is used to insert newlone\n",
    "t is used to insert horizontal tab"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8b1dd634",
   "metadata": {},
   "source": [
    "3. What is the way to include backslash characters in a string?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dcadc7ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "\\\\ is used to include backslash"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "39f1670b",
   "metadata": {},
   "source": [
    "4. The string \"Howl's Moving Castle\" is a correct value.\n",
    "Why isn't the single quote character in the word Howl's not escaped a problem?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8d833412",
   "metadata": {},
   "outputs": [],
   "source": [
    "Because it is within double quotes otherwise it will give syntax error"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e1ae9432",
   "metadata": {},
   "source": [
    "5. How do you write a string of newlines if you don't want to use the n character?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "113c291b",
   "metadata": {},
   "outputs": [],
   "source": [
    "By using every line inside triple quotes \"\"\"\"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "727530ea",
   "metadata": {},
   "source": [
    "6. What are the values of the given expressions?\n",
    "'Hello, world!'[1]\n",
    "'Hello, world!'[0:5]\n",
    "'Hello, world!'[:5]\n",
    "'Hello, world!'[3:]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "908dafec",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'e'"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " 'Hello, world!'[1] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "eb353618",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'Hello, world!'[0:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "13315894",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'Hello, world!'[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3e5f981d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'lo, world!'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'Hello, world!'[3:]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e63da973",
   "metadata": {},
   "source": [
    "7. What are the values of the following expressions?\n",
    "'Hello'.upper()\n",
    "'Hello'.upper().isupper()\n",
    "'Hello'.upper().lower()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1e3125a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'HELLO'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'Hello'.upper()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d59623c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'Hello'.upper().isupper()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "63c48a5f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'Hello'.upper().lower()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d015dc50",
   "metadata": {},
   "source": [
    "8. What are the values of the following expressions?\n",
    "'Remember, remember, the fifth of July.'.split()\n",
    "'-'.join('There can only one.'.split())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "355cab61",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Remember,', 'remember,', 'the', 'fifth', 'of', 'July.']"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'Remember, remember, the fifth of July.'.split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "40c17690",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'There-can-only-one.'"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'-'.join('There can only one.'.split())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6bd4a47c",
   "metadata": {},
   "source": [
    "9. What are the methods for right-justifying, left-justifying, and centring a string?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "006ebc83",
   "metadata": {},
   "outputs": [],
   "source": [
    "right-justifying = str.rjust()\n",
    "left-justifying = str.ljust()\n",
    "center-justifying = str.center()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4eed8279",
   "metadata": {},
   "source": [
    "10. What is the best way to remove whitespace characters from the start or end?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "051f4083",
   "metadata": {},
   "outputs": [],
   "source": [
    "string.trim()"
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
