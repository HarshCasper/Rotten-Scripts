# first install pyjokes library using pip install pyjokes 
# then import it using import pyjokes
import pyjokes

try:
    print("Jokes for you-\n")

    # to get a single joke
    joke = pyjokes.get_joke()
    print(joke)

    # to get multiple jokes
    jokes = pyjokes.get_jokes()
    print(jokes)

    # to get specific number of jokes
    jokes = pyjokes.get_jokes()
    for i in range(5, 10):
      print(jokes[i], end="\n\n")

    # to get a single joke in particular language, example es - Spanish
    # category is for what type of jokes you want
    joke_lang = pyjokes.get_joke(language="es", category="neutral")
    print(joke_lang)

    # to get multiple jokes in a particular language, example es - Spanish
    # category is for what type of jokes you want
    jokes_lang = pyjokes.get_jokes(language="es", category="neutral")
    print(jokes_lang)

except Exception as e:
    pass
