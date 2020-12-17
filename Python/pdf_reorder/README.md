
## A pdf reorder or Rearranging Script

#### I used the pdfrw library 
It is built purely in python

A more efficient,faster and non python built alternatives is PyMuPDF.
The PyMuPDF library can dependency issues hence we will go for a more simpler **pdfrw library

You can download pdfrw using
	pip install pdfrw
	
[more information on pdfrw on PyPi page ](https://pypi.org/project/pdfrw/#id25)


####Now About the script pdf_reorder.py

It takes path of the file as an Input
Then it takes current page and the page you want it to be on seperate values by a comma ','
It parses and sorts the input values by the function input_and_parse(n) 
which takes an input of length of the pdf.

Then using the reorder() function we can get the desired file after rearranging

[See the code here for more information about how the script works]()

Also for testing the script you can make your own pdf using the **generate_pdf.py script

Using this script you will get A pdf with wrong pages like the wrong.pdf in this folder
In the wrong.pdf file The pages have info about the current page but in wrong order.

[wrong.pdf]()
