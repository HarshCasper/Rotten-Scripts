
## A PDF reordering script

This scrip can be used for reordering a pdf file which may have pages in wrong order.

We used **pdfrw** library for this script 

A more efficient,faster alternatives is PyMuPDF.
The PyMuPDF library can have dependency issues with versions of visual C++ hence we used a more simpler library pdfrw

 Download pdfrw using
	```pip install pdfrw```
	
[More information on pdfrw on PyPi page ](https://pypi.org/project/pdfrw/#id25)


**Now About the script pdf_reorder_.py

* It takes path of the file as an Input.
* Then it takes current page which is in the wrong order 
* and the right page no. it should be on seperate values by a comma ',' and line by line.
  * Example:- 
	1,2 
	3,1
	2,3
    *here the 1st page in the pdf should be on the 2nd page instead and so on.

* The script parses and sorts the input values by the function input_and_parse(n) 
  which takes no. of pages in pdf file as input.
* Then using the reorder() function we can get the desired file after rearranging

[See the code here for more information about how the script works](https://github.com/HarshCasper/Rotten-Scripts/Python/pdf_reorder/pdf_reorder_.py)

Also for testing the script one can use the [wrong.pdf](https://github.com/HarshCasper/Rotten-Scripts/Python/pdf_reorder/wrong.pdf) file. 
