# Near Earth Objects Exploration
Near Earth Object Exploration using Python from Udacity Intermediate Python Nanodegree

## Dataset
This project contains two important data sets, and our first step will be to explore and understand the data contained within these structured files.

One dataset (neos.csv) contains information about semantic, physical, orbital, and model parameters for certain small bodies (asteroids and comets, mostly) in our solar system. The other dataset (cad.json) contains information about NEO close approaches - moments in time when the orbit of an astronomical body brings it close to Earth.

Importantly, these datasets come directly from NASA. [neo.csv](https://ssd.jpl.nasa.gov/tools/sbdb_query.html) and [cad.json](https://ssd-api.jpl.nasa.gov/doc/sbdb.html)

## Tasks
We will breakdown this project into small tasks as follows:
* Task 0: Inspect the data. (data/neos.csv and data/cad.json).
* Task 1: Build models to represent the data. (models.py)
* Task 2: Extract the data into a custom database (extract.py and database.py)
* Task 3: Create filters to query the database to generate a stream of matching CloseApproach objects, and limit the result size. (filters.py and database.py)
* Task 4: Save the data to a file. (write.py)

## Links
* Link to the main repository unsolved:
```
git clone https://github.com/udacity/cd0010-advanced-python-techniques-project-starter.git
```
* Link to a reference code solutions: [Near-Earth-Objects](https://github.com/stanleydukor/Near-Earth-Objects.git)

## Results
```
PS D:\Courses\Intermediate-Python-Nanodegree\NEO> python -m unittest
.........................................................................
----------------------------------------------------------------------   
Ran 73 tests in 5.784s

OK
PS D:\Courses\Intermediate-Python-Nanodegree\NEO> 
```
