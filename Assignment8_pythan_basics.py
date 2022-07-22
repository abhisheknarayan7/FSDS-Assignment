{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3703e72a",
   "metadata": {},
   "source": [
    "1. Is the Python Standard Library included with PyInputPlus?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7efd5a9c",
   "metadata": {},
   "source": [
    "ANS - No PyInputPlus is not included in python standard library, we need it install it seperately."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8334658e",
   "metadata": {},
   "source": [
    "2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ea33f119",
   "metadata": {},
   "source": [
    "ANS - pypi is alias of PyInputPlus so that we can use it in easy manner."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "157def2c",
   "metadata": {},
   "source": [
    "3. How do you distinguish between inputInt() and inputFloat()?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "66d77ac0",
   "metadata": {},
   "source": [
    "ANS - inputint() takes only integer value as input,  whereas inputfloat() takes integer and float both as input and returns floating point value."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "208ea2ac",
   "metadata": {},
   "source": [
    "4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "070262c2",
   "metadata": {},
   "source": [
    "ANS - By setting the min = 0 and max = 99 in the inputint() function"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "36d83b83",
   "metadata": {},
   "source": [
    "5. What is transferred to the keyword arguments allowRegexes and blockRegexes?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6d33fa7d",
   "metadata": {},
   "source": [
    "ANS - We can also use regular expressions to specify whether an input is allowed or not. The allowRegexes and blockRegexes keyword arguments take a list of regular expression strings to determine what the PyInputPlus function will accept or reject as valid input."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2497d54b",
   "metadata": {},
   "source": [
    "6. If a blank input is entered three times, what does inputStr(limit=3) do?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9480f28a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting pyinputplusCollecting pyinputplus\n",
      "  Using cached PyInputPlus-0.2.12-py3-none-any.whl\n",
      "Collecting pysimplevalidate>=0.2.7\n",
      "  Using cached PySimpleValidate-0.2.12-py3-none-any.whl\n",
      "Collecting stdiomask>=0.0.3\n",
      "  Using cached stdiomask-0.0.6-py3-none-any.whl\n",
      "Installing collected packages: stdiomask, pysimplevalidate, pyinputplus\n",
      "Successfully installed pyinputplus-0.2.12 pysimplevalidate-0.2.12 stdiomask-0.0.6\n",
      "\n",
      "  Downloading PyInputPlus-0.2.12.tar.gz (20 kB)\n",
      "  Installing build dependencies: started\n",
      "  Installing build dependencies: finished with status 'done'\n",
      "  Getting requirements to build wheel: started\n",
      "  Getting requirements to build wheel: finished with status 'done'\n",
      "    Preparing wheel metadata: started\n",
      "    Preparing wheel metadata: finished with status 'done'\n",
      "Collecting stdiomask>=0.0.3\n",
      "  Downloading stdiomask-0.0.6.tar.gz (3.6 kB)\n",
      "  Installing build dependencies: started\n",
      "  Installing build dependencies: finished with status 'done'\n",
      "  Getting requirements to build wheel: started\n",
      "  Getting requirements to build wheel: finished with status 'done'\n",
      "    Preparing wheel metadata: started\n",
      "    Preparing wheel metadata: finished with status 'done'\n",
      "Collecting pysimplevalidate>=0.2.7\n",
      "  Downloading PySimpleValidate-0.2.12.tar.gz (22 kB)\n",
      "  Installing build dependencies: started\n",
      "  Installing build dependencies: finished with status 'done'\n",
      "  Getting requirements to build wheel: started\n",
      "  Getting requirements to build wheel: finished with status 'done'\n",
      "    Preparing wheel metadata: started\n",
      "    Preparing wheel metadata: finished with status 'done'\n",
      "Building wheels for collected packages: pyinputplus, pysimplevalidate, stdiomask\n",
      "  Building wheel for pyinputplus (PEP 517): started\n",
      "  Building wheel for pyinputplus (PEP 517): finished with status 'done'\n",
      "  Created wheel for pyinputplus: filename=PyInputPlus-0.2.12-py3-none-any.whl size=11297 sha256=cce917c9f9b83107e8786e30e0e2f36d937357b84c652c445d0626f1319a6f1d\n",
      "  Stored in directory: c:\\users\\abhishek\\appdata\\local\\pip\\cache\\wheels\\b4\\6e\\2f\\8a852732646cabec36c3fe8fc060ec5bea1c1be711432c47f7\n",
      "  Building wheel for pysimplevalidate (PEP 517): started\n",
      "  Building wheel for pysimplevalidate (PEP 517): finished with status 'done'\n",
      "  Created wheel for pysimplevalidate: filename=PySimpleValidate-0.2.12-py3-none-any.whl size=16175 sha256=76d5848fc3fc73998832648e6df5c4e18d17147384e292ac35b8f120ae58b589\n",
      "  Stored in directory: c:\\users\\abhishek\\appdata\\local\\pip\\cache\\wheels\\b1\\44\\4a\\043a4f4c4512c7cdfb0c2b8408b18b0de5fd45cac57f5dfa02\n",
      "  Building wheel for stdiomask (PEP 517): started\n",
      "  Building wheel for stdiomask (PEP 517): finished with status 'done'\n",
      "  Created wheel for stdiomask: filename=stdiomask-0.0.6-py3-none-any.whl size=3306 sha256=79876dc21fed05b87fd77d5d7a39d3fa08c392749cb6ecc6c4bdf89d9f9d4d27\n",
      "  Stored in directory: c:\\users\\abhishek\\appdata\\local\\pip\\cache\\wheels\\1d\\aa\\47\\f41f117d22c5de82e95d9342f44da578c80610739a2d5ebec4\n",
      "Successfully built pyinputplus pysimplevalidate stdiomask\n",
      "Installing collected packages: stdiomask, pysimplevalidate, pyinputplus\n",
      "Successfully installed pyinputplus-0.2.12 pysimplevalidate-0.2.12 stdiomask-0.0.6\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -umpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution - (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -umpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution - (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -umpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution - (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -umpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution - (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -umpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution - (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -umpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution - (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -umpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -umpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution - (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -umpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution - (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -umpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution - (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -umpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution - (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -umpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution - (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -umpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution - (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "\n",
      "WARNING: Ignoring invalid distribution - (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -umpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution - (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -umpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution - (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -umpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution - (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -umpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution - (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -umpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -mpy (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution - (c:\\programdata\\anaconda3\\lib\\site-packages)\n"
     ]
    }
   ],
   "source": [
    "!pip install pyinputplus"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "29565198",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Blank values are not allowed.\n",
      "\n",
      "Blank values are not allowed.\n",
      "\n",
      "Blank values are not allowed.\n"
     ]
    },
    {
     "ename": "RetryLimitException",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValidationException\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\pyinputplus\\__init__.py\u001b[0m in \u001b[0;36m_genericInput\u001b[1;34m(prompt, default, timeout, limit, applyFunc, validationFunc, postValidateApplyFunc, passwordMask)\u001b[0m\n\u001b[0;32m    166\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 167\u001b[1;33m             possibleNewUserInput = validationFunc(\n\u001b[0m\u001b[0;32m    168\u001b[0m                 \u001b[0muserInput\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\pyinputplus\\__init__.py\u001b[0m in \u001b[0;36m<lambda>\u001b[1;34m(value)\u001b[0m\n\u001b[0;32m    242\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 243\u001b[1;33m     validationFunc = lambda value: pysv._prevalidationCheck(\n\u001b[0m\u001b[0;32m    244\u001b[0m         \u001b[0mvalue\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mblank\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mblank\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstrip\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mstrip\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mallowRegexes\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mallowRegexes\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mblockRegexes\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mblockRegexes\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexcMsg\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\pysimplevalidate\\__init__.py\u001b[0m in \u001b[0;36m_prevalidationCheck\u001b[1;34m(value, blank, strip, allowRegexes, blockRegexes, excMsg)\u001b[0m\n\u001b[0;32m    249\u001b[0m         \u001b[1;31m# value is blank but blanks aren't allowed.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 250\u001b[1;33m         \u001b[0m_raiseValidationException\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0m_\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Blank values are not allowed.\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexcMsg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    251\u001b[0m     \u001b[1;32melif\u001b[0m \u001b[0mblank\u001b[0m \u001b[1;32mand\u001b[0m \u001b[0mvalue\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m\"\"\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\pysimplevalidate\\__init__.py\u001b[0m in \u001b[0;36m_raiseValidationException\u001b[1;34m(standardExcMsg, customExcMsg)\u001b[0m\n\u001b[0;32m    221\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mcustomExcMsg\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 222\u001b[1;33m         \u001b[1;32mraise\u001b[0m \u001b[0mValidationException\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mstandardExcMsg\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    223\u001b[0m     \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValidationException\u001b[0m: Blank values are not allowed.",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mRetryLimitException\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_16860/3546477679.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mpyinputplus\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mpypi\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpypi\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0minputStr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlimit\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\pyinputplus\\__init__.py\u001b[0m in \u001b[0;36minputStr\u001b[1;34m(prompt, default, blank, timeout, limit, strip, allowRegexes, blockRegexes, applyFunc, postValidateApplyFunc)\u001b[0m\n\u001b[0;32m    245\u001b[0m     )[1]\n\u001b[0;32m    246\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 247\u001b[1;33m     return _genericInput(\n\u001b[0m\u001b[0;32m    248\u001b[0m         \u001b[0mprompt\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mprompt\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    249\u001b[0m         \u001b[0mdefault\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mdefault\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mC:\\ProgramData\\Anaconda3\\lib\\site-packages\\pyinputplus\\__init__.py\u001b[0m in \u001b[0;36m_genericInput\u001b[1;34m(prompt, default, timeout, limit, applyFunc, validationFunc, postValidateApplyFunc, passwordMask)\u001b[0m\n\u001b[0;32m    186\u001b[0m                 \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    187\u001b[0m                     \u001b[1;31m# If there is no default, then raise the timeout/limit exception.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 188\u001b[1;33m                     \u001b[1;32mraise\u001b[0m \u001b[0mlimitOrTimeoutException\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    189\u001b[0m             \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    190\u001b[0m                 \u001b[1;31m# If there was no timeout/limit exceeded, let the user enter input again.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mRetryLimitException\u001b[0m: "
     ]
    }
   ],
   "source": [
    "import pyinputplus as pypi\n",
    "response = pypi.inputStr(limit=3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e5b0c875",
   "metadata": {},
   "source": [
    "It will throw RetryLimitException Error"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f8316e53",
   "metadata": {},
   "source": [
    "7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "8b6a5007",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Blank values are not allowed.\n",
      "\n",
      "Blank values are not allowed.\n",
      "\n",
      "Blank values are not allowed.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'hello'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "response = pypi.inputStr(limit=3, default='hello')\n",
    "response"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ca916f43",
   "metadata": {},
   "source": [
    ". When you use limit keyword arguments and also pass a default keyword argument, the function returns the default value instead of raising an exception"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f3e5d86",
   "metadata": {},
   "outputs": [],
   "source": []
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
