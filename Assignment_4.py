{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6583a61f",
   "metadata": {},
   "source": [
    "1. What exactly is []?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a112b040",
   "metadata": {},
   "outputs": [],
   "source": [
    "This is called paranthesis and it used to store values in a list"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "68e7624f",
   "metadata": {},
   "source": [
    "2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9374e5d8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 4, 'hello', 6, 8, 10]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "spam = [2,4,6,8,10]\n",
    "spam.insert(2,\"hello\")\n",
    "spam"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "754215a4",
   "metadata": {},
   "source": [
    "Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.\n",
    "3. What is the value of spam[int(int('3' * 2) / 11)]?\n",
    "4. What is the value of spam[-1]?\n",
    "5. What is the value of spam[:2]?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "aa0e84dd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'d'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "spam = ['a','b','c','d']\n",
    "spam[int(int('3' * 2) / 11)]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7cb4b5d6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'d'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "spam[-1]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b1ff4db8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['a', 'b']"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "spam[:2]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6965408d",
   "metadata": {},
   "source": [
    "Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.\n",
    "6. What is the value of bacon.index('cat')?\n",
    "7. How does bacon.append(99) change the look of the list value in bacon?\n",
    "8. How does bacon.remove('cat') change the look of the list in bacon?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7a6f9bc0",
   "metadata": {},
   "outputs": [],
   "source": [
    "bacon = [3.14, 'cat',  11, 'cat', True] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "36ff7fe1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacon.index('cat')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "1cf98b3a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3.14, 'cat', 11, 'cat', True, 99]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacon.append(99)\n",
    "bacon"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "16435c34",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3.14, 11, 'cat', True, 99]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bacon.remove('cat')\n",
    "bacon"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5d11efbf",
   "metadata": {},
   "source": [
    "9. What are the list concatenation and list replication operators?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ac115b83",
   "metadata": {},
   "outputs": [],
   "source": [
    "list concatenation operator is +\n",
    "list replication operator is *"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e04ad307",
   "metadata": {},
   "source": [
    "10. What is difference between the list methods append() and insert()?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e3080484",
   "metadata": {},
   "outputs": [],
   "source": [
    "list method\n",
    "append add the new variable at the last of the list\n",
    "insert adds the new variable at given index"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1fd3ac46",
   "metadata": {},
   "source": [
    "11. What are the two methods for removing items from a list?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df573500",
   "metadata": {},
   "outputs": [],
   "source": [
    "remove and pop are the two methods for removing item from a list"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "390bd5a1",
   "metadata": {},
   "source": [
    "12. Describe how list values and string values are identical."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b21a08e",
   "metadata": {},
   "outputs": [],
   "source": [
    "Because both have ordered collection of character\n",
    "but we cant say both are identical as list are mutable but strings are immutable"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "00082bff",
   "metadata": {},
   "source": [
    "13. What's the difference between tuples and lists?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f2682f40",
   "metadata": {},
   "outputs": [],
   "source": [
    "tuples are immutable and list are mutable means list can be modified but tuples can not"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "61b89e55",
   "metadata": {},
   "source": [
    ". How do you type a tuple value that only contains the integer 42?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "af520f27",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "42"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t =(42)\n",
    "t"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cd5b9417",
   "metadata": {},
   "source": [
    "15. How do you get a list value's tuple form? How do you get a tuple value's list form?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f3b524d",
   "metadata": {},
   "outputs": [],
   "source": [
    "Couldnt Understand the question"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "59dee530",
   "metadata": {},
   "source": [
    "16. Variables that \"contain\" list values are not necessarily lists themselves. Instead, what do they contain?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ecb2ccec",
   "metadata": {},
   "outputs": [],
   "source": [
    "Variable only contains string or integer value"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eacb5d64",
   "metadata": {},
   "source": [
    "17. How do you distinguish between copy.copy() and copy.deepcopy()?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f12f4bef",
   "metadata": {},
   "outputs": [],
   "source": [
    "copy.copy() changes the original object\n",
    "copy.deepcopy() creates new object and then copies it into new one\n",
    "copy.copy() affects the original object whereas copy.deepcopy() does not affect the original object"
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
