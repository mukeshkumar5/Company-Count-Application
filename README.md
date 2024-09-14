# Company-Count-Application
This project is a Django-based web application that includes features such as data upload, query builder, user management, and user authentication. It integrates with PostgreSQL as the database and utilizes Bootstrap for front-end design.

## Features
File Upload: Allows users to upload CSV files and process them.  
Query Builder: Users can search and filter data based on multiple criteria.   
User Management: View, add, and delete users.   
Authentication: Login and logout functionality.   

# Prerequisites
Ensure you have the following installed on your system:    
Python 3.9 or above     
PostgreSQL      
pip (Python package manager)     
Git   

# Install Dependencies
pip install -r requirements.txt

# Update the DATABASES configuration in your settings.py file with your database credentials
DATABASES = {   
    'default': {   
        'ENGINE': 'django.db.backends.postgresql',    
        'NAME': 'your_db_name',    
        'USER': 'your_db_user',    
        'PASSWORD': 'your_db_password',    
        'HOST': 'localhost',    
        'PORT': '5432',    
    }   
}    

# Migrate the Database
python manage.py migrate

# Create a Superuser
python manage.py createsuperuser

# Run the Development Server
python manage.py runserver

# Access the Admin Interface
http://127.0.0.1:8000/admin/

#  Access the login Interface
http://127.0.0.1:8000/login/




