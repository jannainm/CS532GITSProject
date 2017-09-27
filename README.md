# GITS – Graffiti Incident Tracking System 
__Description:__ A Django powered MYSQL online website database and offline graphical user interface (GUI).

## Languages/Plugins: 
	-Python
	-HTML/CSS
	-sqlite3/MYSQL 
	-Django

## IDE: Eclipse with Pydev & Django Support

### IMPORTANT FILES:
To run the program you will be concerned with the Program_Files folder, please:
	1) Open the OnlineUI folder and run OnlineUI to see the Python Tkinter GUI (and socket server)
	2) Everything inside /Program_Files/GITSdb_NEW is the Django database, the most relevant files
	   are models.py, admin.py, settings.py, and urls.py.

## About:
 This app is GITS: Graffiti Incident Tracking System and it has two parts. The first is the
 local (offline) portion that Law Enforcement uses to pull in pictures and other information
 via socket connection to the MYSQL database. Then, the offline GUI reads from the file when
 a user selects the update button. Load button allows cases and their information to be displayed.
 The online database resides at localhost/gits/ - but you need an admin or staff account to sign
 in. Once signed in, crew members update "Incidents" which serve as case files for graffiti
 cleanups that result. This is the data the server will send to the local GUI over socket.

 Most of the Django setup was learned in this [tutorial](https://docs.djangoproject.com/en/1.9/intro/tutorial03/).
