# Stying Guidelines

These are the sets of rules that **must** be followed before making any contributions in _Rotten-Scripts_.

Kindly note the fact, that even your working pull request might be rejected if it doesn't follow the below-mentioned
rules.

The maintainers are here to help you at any point in time, In case you have doubts, questions, and/or suggestions, 
feel free to start a discussion [here](https://github.com/HarshCasper/Rotten-Scripts/discussions).

Go though our [Code of conduct](CODE_OF_CONDUCT.md).

We have tried our best to keep the guideline beginner-friendly and reasonable, but do note the fact that a minimal
understanding of styling is a must if you want to contribute to bigger projects and organizations.

## Flow 

1. [Prerequisites](#prerequisites) 
2. [Basics](#basics)
3. [Language Specific README](#Langauge-Specefic-README)
4. [Python](#python)
5. [MarkDown](#markdown)
6. [JavaScript](#javascript)
7. GitHub Actions

### Prerequisites

Every pull request you make for adding a new script, fixing/upgrading an old script, fixing a bug must contain
these things - 

- Script file with the proper extension (.py|.js|.go).
- `README.md` explaining the working of the script.
- Proof of work (In form of test cases, screenshots, GIFs).

It is highly recommended to follow the styling guidelines of this project for every script,
Click [here](#Flow) to find your guide.

Follow this [template](TEMPLATE_README.md) for making a state-of-art `README` file. Do read our
[contribution guidelines](CONTRIBUTING.md) beforehand.

It is highly recommended not to save images locally as this might lead (is leading) to an oversize and heavy repository.
Use an online image sharing and hosting platform like
[Imgur](https://imgur.com/), [ImageShack](https://imageshack.com/), [Postimage](https://postimages.org/)
for hosting images over the cloud and paste the link in `README`.

### Basics

The Repository follows a strict directory naming scheme i.e. capital case with underscores, e.g. `Directory_Name`.
Auxiliary verbs, propositions, conjunctions, and other similar words should be in lower case (excluding the first word),
e.g. `This_is_Directory`.

It is recommended to follow the proper _Project Structure_ of whatever framework you are coding in.

### Language-Specific-README

The Repository contains separate `README` files in the directory of a particular language, which contains a curated list
of all the scripts in the directory, **the contributors are requested to update this list with every PR they make,
failing to which will lead to a delay in merging the PR, or worse might lead to rejection as well.**

A list of Language-specific README can be found here:

- Python
- JavaScript
- Go
- Bash
- Powershell

Contributors are requested to ensure that they are updating these README files with proper format, to maintain the
aesthetics of the Repository.

#### Actions
This Repository is driven by multiple styles checking actions. The actions focus on -

1. Styling of Python file
2. Styling of JavaScript file
3. Styling of Markdown file
4. Links in Markdown file
5. Spellings in Markdown file

It is always recommended that you check the output of these Actions, and
**positively get rid of all the possible errors**.

The reviewer might reject your Pull-Request if you fail to check the output of Actions or the errors reported is not
nullified. By following the styling guide, you can reduce the number of errors substantially. A detailed overview of
workaround over errors that pop-up in GitHub actions can be found [here](./.github/linters/Troubleshoot.md).

### Python

Contributors are requested to follow the [`PEP-8`](https://www.python.org/dev/peps/pep-0008/) guidelines.
Although at Rotten-Scripts we highly recommend contributors to follow the guidelines strictly,
we do understand that this might get overwhelming for beginners. Hence we have a more lenient styling guide for
our project. We would like to clarify that this guideline is for this project only and other projects might differ
from our styling rules.

The below-mentioned rules should be followed without any exceptions, this will not help us in keeping the Repo well
maintained but also will help the contributors by encouraging them towards clean code.

#### Rules

- **Indentation** - Use _4 spaces_,  ~~never tabs~~ for indentation. This is a strict rule and ignoring this can
(has) cause(d) bugs.
- **Line-Length** - Limit all lines to a maximum of 79 characters. (Although this is highly debated, but is a standard
of PEP-8), this rule is not strict but is still recommended as multiple popular projects stick to this rule.

For Example - 

```py
# BAD:  
my_variable = my_method.method(argument1, argument2, argument3, argumnet4)

# GOOD: 
my_variable = my_method.method (
                argument1, 
                argument2, 
                argument3, 
                argumnet4)
```

- **Splitting-Lines** - For every line exceeding the limit, it is recommended to split lines using continuation inside
parentheses, brackets, and braces.

Backslash can also come in handy, for example -

```py
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```

- **Binary Operators** - It's a common practice to break a line after a binary operator, although it is not recommended
at all.

For example -

```py
# BAD:
sum(positive1 +
    positive2 +
    positive3 -
    negative1 -
    negative2 +
    positive4)

# GOOD:
sum(positive1
    + positive2
    + positive3
    - negative1
    - negative2
    + positive4)
```

- **Naming Conventions** - At _Rotten-Scripts_ we follow this naming convention:

  - _Class names_ :  `CamelCase`, and capitalize acronyms, for e.g. `ClassName` and `IEEEPaper` not ~~`IeeePaper`~~
  - _Variable names_ :  `lower_with_underscores`, for e.g. `postive_num`
  - _Method and function names_ :  `lower_with_underscores`, for e.g. `sum_of_first_five`
  - _Modules_ :  `lower_with_underscores.py`, although it is preferred not to use names that contain underscore in
  the first place.
  - _Constants_ :  `UPPER_WITH_UNDERSCORES`.
  - It is highly recommended not to use trailing, leading, and double underscores as they have a separate meaning in
  Python. If you know what you are doing, then you are more than welcome to do that. Just notice that if the
  underscores don't align with their probable meaning, the actions will complain.
  - Although `single_trailing_underscores` are used to distinguish variable/method names from keywords,
  e.g. `Class` is a keyword, `Class_` is not. It is still recommended to use different terminology.
  - It is a **strict** rule, not to use `Capitalized_Words_With_Underscores` as it looks bad.
  - Contributors are hereby informed that using **meaningless variable names**
  (like l in place of len for length, a, s, d, etc will lead to a **straight rejection** of the pull request).
  - Never use the characters 'l' (lowercase letter L), 'O' (uppercase letter O), or 'I' (uppercase letter I)
  as single-character variable names. In some fonts, they are not distinguishable.

Overriding these rules is not recommended unless it is done for a reason, in that case, a separate comment
is a must to explain the name.
 
- **Comments** - Writing comments should be a common habit for everyone, they are helpful for writer, viewer, reviewer,
and user. But comments that contradict the code are worse than no comments. For Rotten-Scripts comments are really
important as the repository comprises scripts written by different people and used by many others. The styling of
comments is of utmost importance.

  - Write as many comments as necessary, don't go overboard, but ensure to explain the much-needed parts.
  - Use block comments for a long comment.
  - Although inline comments are recommended according to the guidelines of PEP-8, we generally don't prefer an
  inline comment.
  - Do write your comments in the proper English language.
  - Follow proper indentations if writing comments in classes or methods.
    
  For example:

```py
"""Block Comment"""

# This is looking better, I bet even you can't argue the fact that
# Block comments are more sensible, I don't know what to write anymore
# but I needed this one line, thank you for reading.

"""Inline Comment"""

# BAD:
x = x + 1		# Some comment

# GOOD:

# Some comment
x = x + 1
```

- **DocStrings** - Docstrings are an important part of Python clean code. PEP-257 guidelines are followed for
Docstrings. Although PEP-257 contain a long  list of rules, we generally stress these rules:

  - Docstring, is a string literal, and it is used in the class, module, function, or method definition. and is
  denoted using a fence of three 'double quotes' like this, `"""docstring """`.
  - Writing docstrings for all functions, classes, and methods are **mandatory**, we will
  reject the PR if there is no proper docstring.
  - Docstring convention:

```py
     def function(arg1, arg2):
 """Write a summary of the function
 
 Arguments:
 arg1: What is arg1?
 arg2: What is arg2?

:return: What function returns?
  """
```
	
	 Example:
	 
```py
def build_similarity_matrix(sentences, stop_words):  
"""  
 Build the similarity index of words in sentences  
 
:param sentences: Clean sentences
:param stop_words: Words to be ignored in Vectors (Read README.md)
:return: Similarity index (Tokenized words)  
 """
```
	
- **Top of the file** - A shebang i.e. `#!/usr/bin/python` is not required **_unless_** the python file is meant
to be executable.
- **Imports** - Imports should be on top of the file, after a comment `# Imports`, it is recommended that the
standard imports are at the top, then the libraries that the user installed. It is always recommended to follow an
alphabetical scheme.
e.g.

```py
# standard library
import collections
import functools
import os
import sys

# installed libraries
import requests

from web3 import (
    Web3,
)

# local
from my_module import (
    something,
)
from my_module.subsystem import (
    others,
)

from my_module.utils.encoding import (
    encode_thing,
)
```
	
- **Parsing** - It is highly recommended that programmers should use the python method `input('Input something')` and
[Argument Parser](https://docs.python.org/3/howto/argparse.html) module for making the code more interactive and
flexible.
- **Paths** - It is advised not to enter local paths at all in your code, this can lead to security vulnerabilities,
rather use relative paths.
- In our contributing guidelines specific for `Python` we have mentioned some tools, which should be used for proper
spacing between lines, and other minor formatting rules. Quick Link - [Click here](Python/CONTRIBUTION-GUIDELINE.md).

### Markdown

`README.md` files are an important feature of this repository which makes it different from others. Programmers are
encouraged to write a good  README file, failing to which the Pull Request will be **rejected**. Here is the
[Template](TEMPLATE_README.md) which we usually follow for this project, feel free to make any edit,
but ensure that the backbone structure remains as it is.

We have 3 GitHub Action which looks after the quality of all the `README` files. A list of possible errors can be
found in [TROUBLESHOOT](./.github/linters/Troubleshoot.md). Refer to the guide to understand the errors.

Here rather than focusing on errors, we will focus on steps to solve them.

- It is recommended to ensure that all the spellings in the README are correct, and all the links, whether relative or
absolute are working.

The Markdown Styling for this Repo follows the style guide of
[markdownlint](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md).
Follow this link for a detailed style guide.

Here we have mentioned the most basic rules, which a `README` must have so that it is even considered for a review.

- **Headings** - Follow the hierarchical heading levels.
Follow a particular heading style and ensure that there is 1 whitespace after `#`.

```text
BAD:
# Heading 1
# Heading 2
#Heading 4

[//]: # (Missed the Heading 3)
[//]: # (Missing the whitespace in Heading 4)

## Another Heading 2 ## [//]: # (This is also called ATX heading format)
# Heading 3

[//]: # (Don't mix heading format, it is recommended not to use any other format than Markdown.)

#     Heading 4
[//]: # (Extra whitespaces in Heading 4)

```

- Headings should be enclosed by 1 blank line.

```text
BAD:
# Heading 1
Text

Text
# Heading 2
```

```text
GOOD:

#  Heading 1

Some text

Some more text

##  Heading 2
```

- There should be only 1 top-level heading and no heading should contain any trailing punctuation marks.
- **Lists** - The list should have consistent uniform symbols and should be indented with 2 spaces
(as 4 spaces are used for a code block).
- List should be enclosed within black lines.

```text
BAD:
- item1
* item2
+ item3

1) numbered1
1. numbered2
1) numbered3

GOOD:
- item1
    + subitem
        * sub-subitem
- item 2

1. numbered1
1. numbered2
1. numbered3
```

- **Line Length** and **Spacing** - There should not be more than 1 line spacing and the maximum length of a line
is capped to 80 characters.
- **Codeblocks** - All the code blocks should be enclosed by blank lines and the fence should have a
language assigned to it.

```text
```py
The language is specified with the code fence.
Results in proper syntax highlighting.
```

### JavaScript

**TODO**

[//]: # (This is a Markdown Comment!!! How are you? If you are editing this file for the JS style guide,
can you follow the markdown styling strictly as well? In case you have questions, find my GitHub at @vybhav72954.
Thank you for helping.)

### GitHub Action

The Repository contains multiple actions meant for purpose of styling and tooling. A list can be found here:

1. Styling of Python file (Using DeepSource and pyLint)
2. Styling of JavaScript file (Using DeepSource)
3. Styling of Markdown file
4. Links in Markdown file
5. Spellings in Markdown file

We have covered Python. JavaScript and Markdown styling already.

#### Spell-Check

Rotten Scripts uses the `pysepelling` module for spell checking.  It is recommended to double-check your files for
spelling discrepancies.

The algorithm might complain about proper and common nouns. It is recommended to follow the steps in
[TROUBLESHOOT](./.github/linters/Troubleshoot.md) for steps to enter such things in the wordlist.
Contributors are requested to follow the steps.

#### Link Check

Link checking of an `md` file can result in several status codes:

- 200: Active code
- 206: Partial success
- 400: Bad Request
- 404: Not Found
- 429: Too many requests
- 999: Blocked by agent

Follow [TROUBLESHOOT](./.github/linters/Troubleshoot.md) for reporting errors.
