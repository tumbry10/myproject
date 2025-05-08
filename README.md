# myproject
 Assignment for my UDEMY course

 2. First App & Templates Configurations
    1. Create the first app - main
    2. Register the app in settings.py under installed apps
    3. Create the main app urls.py file and link it to the main project's urls.py file
    4. Create the index view, url & template
    5. Configure the templates in settings.py
    6. Runserver to test, 
 
 3. Define & Manage ur First Model
    1. Create the Book model in the model.py and add its diff fields. 
    2. Create and apply migrations
    3. Register the Book model to the Admin Site. 
    4. Create the superuser
    5. Login to the admin site and create some Book records
    6. Retrieve and Display Book records in an html template(For this I use the home page)

 4. Django Views and URL routing.
    1. Much has been done in the previous section
    2. Here we focus on the View & Url for displaying details of a single instance of a model 

 5. Django Templates & Static Files
    1. Design the responsive layout for the base html file
    2. Extends the base.html to other html files to list the books and to view single book details
    3. Design the Navbar and footer.
    3. Download bootstrap and configure the static files. 
    4. Link the static files to the html file.

 6. Handling Forms and User Inputs.
    1. Create a form in forms.py to handle user feedback
    2. Create feedback model and migrate, register the model inadmin.py
    3. Create feedback view to process both GET & POST request
    4. Create feedback_form.html template for rendering the form 
    5. Configured the url to map the Feedback view

 7. User Authentication & Authorization
    1. Create a new app (user_auths), to handle user authentication procedures
    2. Configure URLs for user authentication (Registration, Login & Logout)
    3. Create Registration forms
    4. Build authentication views, (Registration, Login & Logout)
    5. Create Authentication Templates 

8. Create a User Registration & Login System
    1. Setup Django Authentication
    2. Create Registration Form
    3. Build Registration View
    4. Create Login View
    5. Setup Logout View
    6. Use decorators to protect pages. 