# gs-meter-djsngo

just run the server
127.0.0.1:8000/gsec/home    for home page
to visit page of particular gensec
127.0.0.1:8000/gsec/name/(username) (username given while registration)
127.0.0.1:8000/gsec/login   login url

How to run locally
Repo link - https://github.com/swciitg/gsec-meter.git
Install all the packages specified in requirements.txt

After cloning the repository go to folder containing manage.py 
Run following commands
Use python3

python manage.py makemigrations
python manage.py migrate

Now you can run the server
python manage.py runserver 
Run this url in browser 127.0.0.1:8000/gsec 

How to add new user
You must login with a CIS member account 
http://127.0.0.1:8000/register/
If the new member is a cis member then choose cis
Else GS

A CIS person is a person who will have access to add new agenda and new user and admin rights
A GS member is a general secretary i.e gymkhana member

Add agenda

Get data from every gs in xsls file in following format
https://docs.google.com/spreadsheets/d/1jyzBnzP9UmcaeZ1RA2KN-9yClfRcbONVpPkdFiP0JAA/edit?usp=sharing
Fields 
User - This will contain the pk value of user which can be seen by going in admin portal opening then opening users table .
Go and click on user id for which u want to get pk value the u will see a link of following format
http://127.0.0.1:8000/admin/auth/user/17/change/
So in above link the pk value for the user is 17  - Enter this in user column

How to upload data from xlsx to database
Find python file named xls_to_json.py
Enter the name of xlsx sheet in which you have agenda details(without file extension)
Enter json file name you want to create where you will transfer data from xlsx file to json and then from json to database
Enter sheet index counting start from counting starts from zero for which you have to update data
Now u r asked to enter maximum pk index till now - there u have to enter the maximum pk value till which data has been inserted to find this go to database admin portal open Agendas database go to the first entry of database and the link will be of form
http://127.0.0.1:8000/admin/gsecWorkStatus/agenda/430/change/?_changelist_filters=p%3D0

So here 430 is the required value,(This is a method which works because entries are sorted in pk value order so the first one has highest pk value ) 
It is not necessary the max pk value is equal to number of entries as some some entries might have been deleted. You really need to be concerned about this part


It is advised that before proceeding to further steps u backup the data
To backup data u can use the commad 

 python manage.py dumpdata > ./gsecWorkStatus/fixtures/filename.json


For more details look in following link
https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata
After applying above steps 
Now u have to run command 
python manage.py loaddata “Json file path”
Currently json file is stored in fixtures folder

If some error occur then just use the backup file restore the database by using command
Python manage.py loaddata “backup file path”


# Gsec_Final_1
