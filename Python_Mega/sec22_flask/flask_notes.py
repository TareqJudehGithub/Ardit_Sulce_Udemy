"""
Flask notes

# installation


WSGI (Web Server Gateway Interface) is an interface between web servers and web
apps for python.

Web Development in Python.

How websites work?

    1. When a user enters a url, and the browsers sends a request to a server
       using HTTP/HTTPs protocol.
    2. The server has 3 files: HMTL, CSS, and the JS file.
        HTML is the building block, CSS is the styling, where JS is responsible
        for the website behavior and interactivity.
    3. The server responds to the browser request and send back any needed file.

    Python lays in the backend (server) side.

Flask official website:
https://flask.palletsprojects.com/en/1.1.x/installation/#installation


    A- Create an Virtual Environment

     1. Create a project folder and a venv folder within:

        $ mkdir myproject
        $ cd myproject
        $ python3 -m venv venv

        The 2nd venv is the name of the folder. So we can install venv on root
        of the project, or in a seperate folder.  venv folder is the standard.

        *** In case running paython3 -m ven venv command returned back an error, make usre you have
        python3-venv package is installed 1st, by running:
        $ sudo apt-get install python3-venv

     2. Activate the environment
        Before you work on your project, activate the corresponding environment:

        $ . venv/bin/activate
        Where venv is the folder name, and bin, is the sub-folder.

     B- Install Flask
        Within the activated environment, use the following command to install Flask:

        $ pip install Flask

        Output should be:
        >>Successfully installed Flask-1.1.2 Jinja2-2.11.3 MarkupSafe-1.1.1
          Werkzeug-1.0.1 click-7.1.2 itsdangerous-1.1.0

"""

