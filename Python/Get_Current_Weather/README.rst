Get Current City Weather
========================

|checkout|

The script gives the weather of the city which you enter

How to use it
-------------

Go to the location where the script is on your local computer, then type

.. code-block:: bash

   python get_current_weather.py “cityname” “units format” “additional
   arguments”

--------------

-  For the cityname, enter the name of the city to get it’s weather
-  For the units format,

   1. Enter **1** if you want the data in **standard** format (e.g Kelvin scale)
   2. Enter **2** if you want the data in **imperial** format (e.g Fahrenheit scale)
   3. Enter **3** if you want the data in **metric** format (e.g Celsius scale) 
   
   .. note:: 
   
      If you enter anything other than 1, 2 or 3, then all the units will be in **metric** format

-  For additional arguments,

   1. Add **sun** if you want the time of sunrise and sunset
   2. Add **main** if you want the temperature data
   3. Add **weather** if you want the pressure, humidity and weather description
   4. Add **wind** if you want the wind speed and direction
   5. Add **clouds** if you want the cloudiness percentage 
   
   .. note:: 
      
      Ifyou do not add any additional arguments, all the data will be displayed.

.. |checkout| image:: https://forthebadge.com/images/badges/check-it-out.svg
  :target: https://github.com/HarshCasper/Rotten-Scripts/tree/master/Python/Get_Current_Weather/

