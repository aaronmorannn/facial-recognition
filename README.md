# Facial Recognition and Temperature Detection
[Aaron Moran](https://github.com/Moran98) &nbsp;
[Arnas Steponavicius](https://github.com/ArnasSteponavicius00) &nbsp;
[Thomas Kenny](https://github.com/KennyThomas)

## Step 1: Test the App Locally
	
1. Run your application locally:
```
	$ python index.py
```

2. You should be able to navigate in your browser to `http://localhost:5000' <http://localhost:5000/>`_ to view your hello world application. You'll notice for Flask the one unique portion is to attempt to read the port variable if it exists, this is to enable Heroku to know which port to listen to. 

3. Press `CTRL-C` to stop the process.

## Install the Project

1. Use pip to install your project in the virtual environment.

```
	$ pip install -e .
```

2. This tells pip to find setup.py in the current directory and install it in editable or development mode. The setup.py file describes your project and the files that belong to it.

3. You can observe that the project is now installed with pip list.

```
	$ pip list
```

## Accessing SQL database from Command Prompt

1. Access the Python terminal by typing the following :

```
	$ python 
```

2. Import the db to the main route file for the application as follows :

```
	$ from index import db
```

3. Display all the users and image file names by using the following command :

```
	$ User.query.all()
```

![](Research/Documentation/Images/db.png)