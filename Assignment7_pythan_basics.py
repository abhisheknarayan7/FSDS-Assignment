{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "87e75e89",
   "metadata": {},
   "source": [
    "1. What is the name of the feature responsible for generating Regex objects?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a97069c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#re.compile()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "68f56ce3",
   "metadata": {},
   "source": [
    "2. Why do raw strings often appear in Regex objects?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "fe51722e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#it is easy to pass raw strings to the re.compile() function instead of typing extra backslashes."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f5081128",
   "metadata": {},
   "source": [
    "3. What is the return value of the search() method?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "acb53732",
   "metadata": {},
   "outputs": [],
   "source": [
    "#If regex pattern not found in string it will return None otherwise it will return the string available in regex object."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "42b019f0",
   "metadata": {},
   "source": [
    "4. From a Match item, how do you get the actual strings that match the pattern?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8caa185c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#By calling grou()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a7528e61",
   "metadata": {},
   "source": [
    "5. In the regex which created from the r'(\\d\\d\\d)-(\\d\\d\\d-\\d\\d\\d\\d)', what does group zero cover? Group 2? Group 1?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9a43eb4a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# group0 = (\\d\\d\\d)-(\\d\\d\\d-\\d\\d\\d\\d)\n",
    "# group1 = (\\d\\d\\d)\n",
    "# group2 = (\\d\\d\\d-\\d\\d\\d\\d)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "75210cf5",
   "metadata": {},
   "source": [
    "6. In standard expression syntax, parentheses and intervals have distinct meanings. How can you tell a regex that you want it to fit real parentheses and periods?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5b1d8a9",
   "metadata": {},
   "outputs": [],
   "source": [
    "r.'()'"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "826e622b",
   "metadata": {},
   "source": [
    "7. The findall() method returns a string list or a list of string tuples. What causes it to return one of the two options?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6d89fd6b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# When called on a regex with no groups, such as \\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d, the method findall() returns a list of string matches, such as ['(\\d\\d\\d)-(\\d\\d\\d\\d-\\d\\d\\d)', '(\\d\\d\\d)-(\\d\\d\\d\\d-\\d\\d\\d)'].\n",
    "\n",
    "# When called on a regex that has groups, such as (\\d\\d\\d)-(\\d\\d\\d)-(\\d\\d\\d\\d), the method findall() returns a list of tuples of strings(one string for each group), such as [('415', '555', '9999'),('212', '555','0000')]."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d39e60b7",
   "metadata": {},
   "source": [
    "8. In standard expressions, what does the | character mean?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4aff81cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "#The | character is called a pipe. You can use it anywhere you want to match one of many expressions."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9942a675",
   "metadata": {},
   "source": [
    "9. In regular expressions, what does the character stand for?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2afb27bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# The ? stands for  \"Match zero or one of the group preceding this question mark.\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "354695f7",
   "metadata": {},
   "source": [
    "10.In regular expressions, what is the difference between the + and * characters?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "fdbb312c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#While * means \"match zero or more\", the + means \"match one or more."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f86eb033",
   "metadata": {},
   "source": [
    "11. What is the difference between {4} and {4,5} in regular expression?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "78520d99",
   "metadata": {},
   "outputs": [],
   "source": [
    "#{4} is saying \"match this pattern four times.\" {4,5} means \"match this pattern four to five times.\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bfc5204e",
   "metadata": {},
   "source": [
    "12. What do you mean by the \\d, \\w, and \\s shorthand character classes signify in regular expressions?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4f7bcd16",
   "metadata": {},
   "outputs": [],
   "source": [
    "# \\d searches only digits \n",
    "# \\w searches only letter, numeric digit or underscore\n",
    "# \\s searches only space, tab or new line character"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dc429fe7",
   "metadata": {},
   "source": [
    "13. What do means by \\D, \\W, and \\S shorthand character classes signify in regular expressions?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "29d3a446",
   "metadata": {},
   "outputs": [],
   "source": [
    "#\\D searches only character which are non digit\n",
    "#\\W searches only which is not letter, numeric digit or underscore\n",
    "#\\S searches only which are not space, tab or new line character"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fd94d8a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#14. What is the difference between .*? and .*?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "fa444b4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# both are same and matches any character any number of times but returns blank string due to '?'"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "05056413",
   "metadata": {},
   "source": [
    "15. What is the syntax for matching both numbers and lowercase letters with a character class?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "788ecfbe",
   "metadata": {},
   "outputs": [],
   "source": [
    "#[0-9a-z]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6183cc54",
   "metadata": {},
   "source": [
    "16. What is the procedure for making a normal expression in regax case insensitive?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "665c9da0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Following 2 are the methods for making a normal  expression case sensitive:\n",
    "#1. Using CASE_SENSITIVE flag\n",
    "# 2. Using Modifier"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "02a411a2",
   "metadata": {},
   "source": [
    "17. What does the . character normally match? What does it match if re.DOTALL is passed as 2nd argument in re.compile()?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "37fc7fd2",
   "metadata": {},
   "outputs": [],
   "source": [
    "#character normally matches any character except the newline character. If re. DOTALL is passed as the second argument to re. compile(), then the dot will also match newline characters"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7990fa5b",
   "metadata": {},
   "source": [
    "18. If numReg = re.compile(r'\\d+'), what will numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen') return?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "9ac2bc9d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#X drummers, X pipers, five rings, X hens"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "edce8181",
   "metadata": {},
   "source": [
    "19. What does passing re.VERBOSE as the 2nd argument to re.compile() allow to do?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "6a905163",
   "metadata": {},
   "outputs": [],
   "source": [
    "#To ignore whitespace and comments inside the regular expression string."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eb7ab653",
   "metadata": {},
   "source": [
    "20. How would you write a regex that match a number with comma for every three digits? It must match the given following:\n",
    "'42'\n",
    "'1,234'\n",
    "'6,368,745'\n",
    "but not the following:\n",
    "'12,34,567' (which has only two digits between the commas)\n",
    "'1234' (which lacks commas)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "c4598552",
   "metadata": {},
   "outputs": [],
   "source": [
    "#numCommas = re.compile(r'(^\\d{1,3})(,\\d{3})*$') numCommas.search('12,34,567').group()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "65655c42",
   "metadata": {},
   "source": [
    "21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:\n",
    "'Haruto Watanabe'\n",
    "'Alice Watanabe'\n",
    "'RoboCop Watanabe'\n",
    "but not the following:\n",
    "'haruto Watanabe' (where the first name is not capitalized)\n",
    "'Mr. Watanabe' (where the preceding word has a nonletter character)\n",
    "'Watanabe' (which has no first name)\n",
    "'Haruto watanabe' (where Watanabe is not capitalized)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "eaae9ec6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#fullName = re.compile(r'[A-Z]\\w [A-Z]\\w') mo = fullName.findall('Haruto Watanbe, Alice Watanbe, Alice Nakamoto, Watanbe, Haruto Watanbe, Robocop watanbe') mo.group()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ba0ecc6c",
   "metadata": {},
   "source": [
    "22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:\n",
    "'Alice eats apples.'\n",
    "'Bob pets cats.'\n",
    "'Carol throws baseballs.'\n",
    "'Alice throws Apples.'\n",
    "'BOB EATS CATS.'\n",
    "but not the following:\n",
    "'RoboCop eats apples.'\n",
    "'ALICE THROWS FOOTBALLS.'\n",
    "'Carol eats 7 cats.'\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ba775bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "###senRegex = re.compile(r'(Alice|Bob|Carol)\\s(eats|pets|throws)\\s(apples|cats|baseballs).', re.I|re.DOTALL)\n",
    "\n",
    "senRegex.findall('''Alice eats apples.'\n",
    "\n",
    "'Bob pets cats.'\n",
    "\n",
    "'Carol throws baseballs.'\n",
    "\n",
    "'Alice throws Apples.'\n",
    "\n",
    "'BOB EATS CATS.'\n",
    "\n",
    "but not the following:\n",
    "\n",
    "'Robocop eats apples.'\n",
    "\n",
    "'ALICE THROWS FOOTBALLS.'\n",
    "\n",
    "'Carol eats 7 cats.''')\n",
    "\n",
    "Test result: [('Alice', 'eats', 'apples'), ('Bob', 'pets', 'cats'), ('Carol', 'throws', 'baseballs'), ('Alice', 'throws', 'Apples'), ('BOB', 'EATS', 'CATS')]"
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
