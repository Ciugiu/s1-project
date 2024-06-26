# S1-Project

This project is a Python application that retrieves data from a local MySQL database and displays it on a website created by the app itself.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of Python.
- You have a MySQL server running on your machine, containing the database and its' data.

## Installing S1-Project

To install S1-Project, follow these steps:

1. ### Set up the project
   - Extract all folders from the downloaded zip file into a directory of your choice. This directory will be referred to as the 'root directory', which will contain the main project files.
   - Move the folders from the 'site' directory into the root directory.
   - Move the 'app.py' file from the 'src' directory to the root directory.
   - Open the 'data_requests_ids.py' file in the 'src' directory with a text or code editor and insert your database credentials. For example:
     ```python
     host = 'localhost'
     user = 'root'
     password = '123456'
     database = 'project'
     ```
   - Save the file and close it.

2. ### Install the required Python packages:

   - Open a terminal in the root directory and run the following command.

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. ### Start the Application

   - Ensure you are in the root directory of the project in your terminal.
   - Start the application by running the following command:

   ```bash
   python app.py
   ```

2. ### Access the Application

   - After executing the command, you should see an output similar to the following:

   ```bash
    * Serving Flask app 'app'
    * Debug mode: off
   WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
   Press CTRL+C to quit
   ```

   - The application is now running on your local machine. You can access it by opening a web browser and navigating to `http://127.0.0.1:5000` or simply hold `CTRL` and click on the `http://127.0.0.1:5000` link. This action will open the website in your default web browser.

## Using the Application

- While using the website, ensure that the terminal running the application remains open. Closing the terminal will shut down the website.
- When you want to stop the website, you can either close the terminal or press `CTRL+C` in the terminal to stop the application. After stopping the application, you can safely close the terminal.
