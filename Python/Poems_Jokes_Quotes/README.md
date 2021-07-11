# Poems Automation
For Poem Automation we are using `poetpy` library which is an unofficial Python wrapper for the PoetryDB API. 
The PoetryDB API allows users to find a vast amount of poetry and poet data and is free to use without any authentication required.

### Installation

Install with `pip` command in any terminal
```python
pip install poetpy
```

### Working

Import the `poetpy` library in the Python file that you are going to get the poems and then use the `get_poetry()` function to easily get poems into your console/application.

For example, we are interested in finding all of William Shakespeare’s poems and sonnets available in the PoetryDB API then

```python
import poetpy

poems = poetpy.get_poetry('author', 'William Shakespeare')

print(poems)

```

### Screenshots
[Image 1](https://imgur.com/xBJiZKK)

[Image 2](https://imgur.com/GQuiYzZ)

[Image 3](https://imgur.com/lntamwU)

[Image 4](https://imgur.com/0zCzNQj)

# Jokes Automation
In this we are using pyjokes which is a python library used to get jokes for programmers. 
We can also call it as a fun python library that can be used simply with some lines of code.    

**Note:** It requires proper Internet connection for its working.

### Installation

Install with `pip` using any terminal

```python
pip install pyjokes
```

### Working

Import the `pyjokes` module in the Python file that you are going to get the jokes and then use the `get_joke()` function to easily get a random joke into your console/application.

```python
import pyjokes

joke = pyjokes.get_joke()

print(joke)
```
To get jokes in a specific language and for a particular category though there are not many categories and language but we can use those that are available.

```
import pyjokes

joke = get_joke(language="es",category="neutral")

print(joke)
```

#### Options available for Language

|Value|Language Name|
|---|---|
|en|English|
|de|German|
|es|Spanish|
|it|Italian|
|gl|Galician
|eu|Basque|
    
#### Options available for Category

|Value|Category Detail|
|---|---|
|neutral|Neutral geeky jokes|
|twister|Tongue-twister|
|all|All types of joke|

### Screenshots
[Image 1](https://imgur.com/X0em4os)

[Image 2](https://imgur.com/EUWEePI)

[Image 3](https://imgur.com/UFvJSf8)

[Image 4](https://imgur.com/u5yRZwj)

# Quotes Automation
For this we are using `quote` library which is a python wrapper for the Goodreads Quote API. 
To generate a random quote we will be using the quote function from the quote module.

### Installation

Install with `pip` command in any terminal
```python
pip install poetpy
```

### Working

It is simple to use and `quote` library can also be used from the command line tool.

```python
from quote import quote

author = 'Albert Einstein'

result = quote(author, limit=2)

print(result)
```

### Screenshots
[Image 1](https://imgur.com/m1QwZ8X)

[Image 2](https://imgur.com/RYB1YAy)

[Image 3](https://imgur.com/zcbuGXv)

[Image 4](https://imgur.com/BFb3z0A)

## Contributor

[Umesh Singh](https://github.com/Umesh-01)
