# E-Commerce Website


### **Description** 
A clone of e-commerce website with three actors Admin, Seller & User. All of three actors has their own functionality and services. This WebApp based on django framework. I have used Bootstrap 4.6 for designing.



### **Installation**

- Extract zip file 
- Open extracted folder and open **CMD** where **manage.py** file exist
- Copy paste the following commands listed below one by one


> Install virtualenv module

	pip install virtualenv


> Create virtual environment

	virtualenv venv


> For a windows system.

	cd venv/Scripts
	activate


> For linux or mac system

	source/bin/active


> Install requirements
		
	pip install -r requirement.txt


> Migrate database schemas
		
	python manage.py makemigrations
    python manage.py migrate


> Run django development server

	python manage.py runserver


Enter URL on your browser ```http://localhost:8000```
