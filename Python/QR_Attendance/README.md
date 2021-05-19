# QR-code-based-Excel-Attendace

## How to generate QR code?

- In the `QR Codes` folder

1. Update the data base in file [Data_base.txt](./Data_base.txt). Make sure each students name resides in a new line without any space.  
![data_base](https://user-images.githubusercontent.com/43489758/118450130-7f1f0b00-b711-11eb-96f6-6d967f9cdc74.jpg)
 

2. Run the [Generate_QR.py](./Generate_QR.py) file by double clicking on it.  
![Generate_QR](https://user-images.githubusercontent.com/43489758/118450199-8f36ea80-b711-11eb-8c32-32aada7b1cfa.jpg)


3. Required QR code for the data base will be created.  
![QR_code](https://user-images.githubusercontent.com/43489758/118450219-96f68f00-b711-11eb-9a3a-143c548e6921.jpg)


## How to take Attendace?

To Take attendace run the [QR_Attendance.py](./QR_Attendance.py) file by double clicking on it.  

![take_attendance](https://user-images.githubusercontent.com/43489758/118450258-a07ff700-b711-11eb-827e-35f509e6b3fe.jpg)
 

A terminal will pop up. Fill in the details to set the Attandace sytem for your class.  

![GUI](https://user-images.githubusercontent.com/43489758/118450315-b097d680-b711-11eb-88f6-7baf55de436a.jpg)


Once the information is filled, checkout the box and click `Ready to Scan QR`. This will open up the terminal for conformation and camera to scan the QR. 
![ready_scan](https://user-images.githubusercontent.com/43489758/118450354-bbeb0200-b711-11eb-97a7-d2e0f6581e31.jpg)

![QR_scan](https://user-images.githubusercontent.com/43489758/118450370-c1484c80-b711-11eb-923e-04cb08b86e17.jpg)


You will recive the conformation on terminal on successful scan.

Once everyone has scanned their QR, press `q` to quit the process. This will close the camera and save the attendance record in `.xls` format.

![xl](https://user-images.githubusercontent.com/43489758/118450419-cc02e180-b711-11eb-86b1-1d290f519c7c.jpg)


At the end this excel sheet is mailed to respective teacher in encoded format.

![mail](https://user-images.githubusercontent.com/43489758/118450453-d58c4980-b711-11eb-9dd9-4700506a14a8.jpg)


## How to Decode the Excel sheet ?
To decode the excel sheet , just download the file and save it with `.xls` extension.

![save](https://user-images.githubusercontent.com/43489758/118450488-e0df7500-b711-11eb-900d-a48ad7f5934d.jpg)


That's it you got your required file.
![decoded](https://user-images.githubusercontent.com/43489758/118450531-ec32a080-b711-11eb-9639-6afb236a9e84.jpg)



>By : Yuvraj Kadale with ❤