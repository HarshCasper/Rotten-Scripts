# QR Code Generator

## Script generates QR code for data listed in a csv file

How to use

```
python qrcode_generator.py --f <csv input file>
```

Example:

```
python qrcode_generator.py --f input.csv
```

### Format of input file

extension: `.csv`<br>
contains 2 columns(without headings, i.e. data starts from row 0)<br>
1st column = file name with which qr code should be saved.<br>
2nd column = data for which qr code should be generated.<br>

#### snap of sample input

![alt](Capture.PNG)