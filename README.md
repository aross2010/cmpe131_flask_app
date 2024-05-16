# cmpe131_flask_app

## Description

This is a simple Flask application that provides a flight book interface where users can book flights. The application allows users to search for flights by entering the departure and destination cities, as well as the departure date. The application will then display a list of available flights that match the search criteria.

## Installation

To run this application, you will need to have Python installed on your computer. You can download Python from the official website: https://www.python.org/. Once you have Python installed, you can follow these steps to run the application:

1. Clone the repository to your local machine:

```
git clone https://github.com/aross2010/cmpe131_flask_app.git
```

2. Navigate to the project directory:

```
cd cmpe131_flask_app
```

3. Create a virtual environment:

```
python3 -m venv venv
```

4. Activate the virtual environment:

````
source venv/bin/activate
```$

5. Install the required Python packages:

````

pip install -r requirements.txt

```

6. Set Up the Database

Run the seeds.py script to populate the database with initial data:

```

python seeds.py

```

7. Run the application:

```

flask run

```

8. Open a web browser and go to http://
```
