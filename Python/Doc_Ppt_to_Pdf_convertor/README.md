# Convert your Doc and PPT files to Pdf files (offline)

### Requirement

- Python
- [comtypes](https://pypi.org/project/comtypes/)

### Instructions

```sh
### run #1 or #2 both will work fine
$ pip install -r requirements.txt #1
### or 
$ pip install comtypes #2

### first Doc to pdf convertor
$ python doctopdf.py "file1.docx" "file2.pdf" # 'file1.docs' is the Doc file you want to convert into pdf and 'file2.pdf' is target file and then it will generate a new pdf file in same directory with name of target file in few seconds

### second Ppt to pdf convertor
$ python ppttopdf.py "file1.pptx" "file2.pdf" # 'file1.pptx' is the PPT file you want to convert into pdf and 'file2.pdf' is target file and then it will generate a new pdf file in same directory with name of target file in few seconds

...
```

It will create a new file with target name so no need to copy your source file

