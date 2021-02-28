# Python Contribution Guidelines

Welcome Contributors!!!

This guide is all about Python, how to code clean, quick and most importantly smart.

There is a lot of Python scripts in this repository, and we are constantly trying to update the code quality and guess
what!!! You can help us!!!.

__How?__ Just follow the below mentioned steps and you are good to go!

## Steps

- Check our [Styling Guide](../STYLE_GUIDELINES.md)
- Check our [_how to start_](../CONTRIBUTING.md)
- Check our [Troubleshoot Guide](../.github/linters/Troubleshoot.md)

### More Tips

Below you can find some important tips that will help you with your contributions.

#### Python->README

As you might have observed we have a `README` for Python which contains a curated list of scripts available on the
directory. You are requested to make changes in the file with every pull request you make for scripts in Python.

#### Naming Convention

Contributors are required to follow the specified convention for naming their directories `Uppercase_with_Underscore`,
for detailed naming convention check our styling guide.

#### Images and GIFs

We recommend that screenshots and images be added as test cases for better understanding of code. But as the size of
repository is getting out of hand, we suggest that these images be first hosted on a cloud hosting service like Imgur,
ImageShack etc. For more information read our styling guide.

#### Security Vulnerabilities

Whenever you are working with any API, or a GitHub secret, it is never recommended to hardcode them in your script.
This can lead to various security threats for the users and Repository as well.

Below we have listed out steps, which should be followed in when working with such information:

- Make a file `.env` in your project directory.
- Add the API token/key/secret and assign it any name, e.g. API_KEY. The `.env` file should look like this:

```text
API_KEY="XXXXXXXXXXXXX"

// Example:
// REACT_APP_GOOGLE_API_KEY=123456
```

- Now install the package `decouple` use:

```bash
pip install python-decouple
```

- Import config from decouple in your script:

```python
from decouple import config
```

- Go to the line where you used your API key. Call your API key like this:

```python
var_name = config("API_KEY")
```

Refer to this [script](Github_Traffic) for a working example.

- You are good to go and your code is more safer than ever.
- You wont be able to push your `.env` file (it is ignored by `.gitignore`), and **one should never do that in the first
place**
- But as an example you should push a `.env.example` (It is a must). The file should be exactly similar to your `.env`
file but the API secret is replaced by `x` or anything.
  - Note this file serves only as an example, it cant cause any security issue, unless you push your API key, kindly
  double check everytime.
  
#### Auto Styling

Any script without the proper styling technique is a problem for us, we again request you to kindly check out Style Guide. It will take only a few minutes.

After ensuring that your script follow all the rules, you can also cross check and rectify any remaining issue (extra
whitespaces, missing or extra blank lines etc) using a few tools.

Below we have explained the steps that one should follow.

We recommend using these auto formatting tools:

- autopep8
- yapf
- black

In order to auto format your files, follow these steps:

- Setup a `python 3.x virtual` environment.
- Activate the environment.
- Install the dependencies using

```py
pip3 install yapf black autopep8
```

- Copy paste your python file in the Virtual environment, say the name of file is `main.py`.
- Now you can run

```bash
autopep8 --in-place main.py
yapf --in-place main.py
black main.py
```

You can use any of the above code formatter or any combination to auto format your code as well.
In order to determine whether your code is up to the mark or not, we suggest using `PyLint`.

- Install `PyLint` using

```bash
pip3 install pylint
```

- Run on CLI

```bash
pylint simplecaeser.py
```

This will generate a PyLint score along with possible errors, deprecated modules and other code standards.

We also have a PyLint Github Action where we monitor the score of the script, kindly ensure that you check your script
thoroughly and format it so it has the best possible score before publishing the PR, it might even get rejected if the
standards are not met at all.
