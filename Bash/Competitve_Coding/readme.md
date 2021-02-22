
_Note: You'll have to clone the template.cpp gist before running the script, or you can make a cpp-template file by yourself in the home folder_

- ## Follow through the steps:
    - First clone this gist by pasting ``` git clone https://gist.github.com/cfe5522469cef7fcaa44c308ee814d69.git ~ ```
    - Now you can alias the script to a word or phrase ``` alias letscode="sh ~/_path_to_the_script/createTemp.sh ```
    ---
    - Now all you have to do to start coding is type in ``` letscode $name ``` .
        - It will create a folder of the name you provided.
        - And in that folder it will create three files, 
            - ``` input.txt ``` 
            - ``` output.txt ``` 
            - ```code.cpp```
            - And then open VSCode in this folder by running ``` code . ``` which you can change in the ```createTemp.sh``` file
        - The ```code.cpp``` contains the template which was cloned in the first step which can be edited at ``` ~/template.cpp```
        - The code after running will take input form ```input.txt``` and write the ouput in ```output.txt```.


### Here's a Demo:

![ezgif com-gif-maker](https://user-images.githubusercontent.com/69139607/108329219-2532a600-71f3-11eb-891b-ff16d2b08a50.gif)
