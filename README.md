# Facial Recognition and Temperature Detection

[Aaron Moran](https://github.com/Moran98)  &nbsp;

[Arnas Steponavicius](https://github.com/ArnasSteponavicius00)  &nbsp;

[Thomas Kenny](https://github.com/KennyThomas)


[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/Moran98/facial-recognition)

  

## Requirements

The requirements needed for this project are as follows :

* Python 3.3+

* Linux, Windows, MacOS

* Django

* Latest version of pip
  

## Installation
  

#### Installing Packages on Mac or Linux follow the instructions below

* https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf
  

Then you are required to install the following python module (Make sure you are using the latest version of pip):

```
pip3 install django
pip3 install opencv-python
pip3 install Pillow
pip3 install face_recognition
```
  

#### Installing Packages on Windows

Currently the packages for face_recognition are not fully supported on Windows, to get around this issue you must follows the instructions below.

* https://github.com/ageitgey/face_recognition/issues/175#issue-257710508

  

## Running the Application Locally

1. Navigate to directory

	```
	$ cd \facial-recognition\facialrecognition
	```
  

2. Make migrations of the required models and tables needed to run the program.
	```
	$ python manage.py makemigrations
	```
  

3. Perform Migrations.

	```
	$ python manage.py migrate
	```


4. Create a super user to access administrator controls and dashboard.

	```
	$ python manage.py createsuperuser
	```
  

5. Run the program.

	```
	$ python manage.py runserver
	```

6. Make sure to navigate in your browser to 'http://localhost:8000/' to view the application.
  

7. To access the admin type the following into the browser while the server is running - 'http://localhost:8000/admin'. This page will display the database and allow the admin to edit user's accounts.
  

8. Press `CTRL-C` to stop the process.

## Acknowledgments:
* [Daniel Cregg - Project Supervisor](https://github.com/danielcregg)
* [Adam Geitgey](https://github.com/ageitgey/face_recognition)
* [Links to articles used in the project](https://github.com/Moran98/facial-recognition/blob/master/doc's/References.txt)
