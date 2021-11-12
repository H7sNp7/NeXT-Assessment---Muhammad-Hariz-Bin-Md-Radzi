# NeXT-Assessment-Muhammad Hariz Md Radzi

1.###To run: the ipynb file…
 
You will need to install Anaconda and Jupyter Notebook.

Inside the .ipynb file:

Import dependencies

```bash
	import pandas as pd
	import datetime
	import datetime as dt
	import numpy as np
	import plotly.express as px
```

2.Make sure to enter the date and time using the correct format. No data validation is in place so if the date format is wrong, the program will encounter an error.


------------------------------

```bash
	url3='https://b708-2001-d08-d7-c97d-d143-3e59-40c7-3e45.ngrok.io/tarikh/?tarikh='+a

	df3=pd.read_json(url3, typ='series')

	df3

output:

Owner                               MUHAMMAD HARIZ BIN MD RADZI
Date Received :    Date received from the user UwU = 12/05/2001
dtype: object
```


The above code will only run successfully if the API in the backend is running.
The API is stored in the “simpleApi-ReturngivenDate.py” file.
To run said file, You will need to have  Node.js Express installed.

Install express in your terminal by using command ```bash:npm install express```
