# Setting up
In order to run program it is required to have >= python 3.6. And execute pip install -r requirements.txt
in terminal.
After installing requirements one has to run:

- python manage.py runserver
- in order to upload data.csv into database use method upload_data_file. It can be done by simply 
going to: http://127.0.0.1:8000/polls/upload_data_file in brwoser or using REST client like Insomnia
 (link: https://insomnia.rest/)
 #Methods
 Available functions:
 - data_get
 - data_browse
 - data_get_specific
 - data_post
 - upload_data_file
 #Usage
 ##data_get (GET method)
 Going to a browser http://127.0.0.1:8000/polls/data_get
 It will render a Html web page with rendered previously data with POST method data_get_specific
 with specific parameters. 
 
 If data_get_specific was not previously executed it will return all data.
 ##data_get_specific (POST method)
 In order to execute send json with specific informations,
  ie. how to filter data,
  how by what to sort it, what is the order (note - before the parameter in order means
  we want to sort it in a descending order, ascending is taken by default), by which 
  parameters do we want to group it. It is shown in an example below like in the exmple below:

```
{"filter_by":  
    {"date_from":"2017-05-17",
         "date_to": "2017-05-18",
         "channel":"",
         "country":"",
         "os":""},
  "sort_by": ["-channel", "country"],
  "order": "descending",
  "group_by": ["channel"]
}
```
##data_browse (GET method)
Function that streams data to front end. IMPORTANT: Please go to url: http://127.0.0.1:8000/polls/data_browse.
Here one can manualy change the input and when clicking update it will update table in a html!!!
Using data_get_specific() method!

## data_post (POST method)
Posts single record to database. One as to specify all the fields in json data i.e.
```
{   
"date": "1992-01-27", 
"channel": "test", 
"country": "test", 
"os": "test", 
"impressions": "29387", 
"clicks": "3321",
"installs": "321321",
"spend": "3213",
"revenue": "32131543"
}
```
## upload_data_file (GET method)
Go to http://127.0.0.1:8000/polls/upload_data_file
