# Book App(Test)
Django-Rest Book App with Vue JS



## Project structure 
├── bookproject        <- Applications main project folder
├── bookapp            <- Project App(Database layer)
├── book_api           <- projects APIs end points

## Requirements
* Python
* Django
* Django-rest
* Install all packages in the requirements.txt file

## How to run the application

* clone this repository and cd inside your project root directory and create a virtual environment. Run - `python -m venv ./venv` This will install your virtual environment.
* Activate the virtual environment by using the command - `. venv/scripts/activate` 
* Install django with the following command `pip install django`
* Now open project requirement.txt file you will find the packages used for this application. Kindly `pip install` all packages in the requirements.txt file.
* Run `py manage.py makemigrations`.
* Run `py manage.py migrate`.
* Start development server by running the command `py manage.py runserver` 
* Type into your browser url the following command `localhost:8000` and the application index page will be up.

##Admin user/password:
* username: Bookapp
* password: Bookapp123

**N.B:-** Kindly go through the apidoc.txt
