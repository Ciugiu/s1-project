from flask import Flask, render_template, request, redirect, url_for
from src import data_request, first_chart, second_chart

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the connection details from the form
        host = request.form.get('host')
        user = request.form.get('user')
        password = request.form.get('password')
        database = request.form.get('database')

        # Save the connection details in a file
        with open('data_request.py', 'w') as f:
            f.write(f"host = '{host}'\n")
            f.write(f"user = '{user}'\n")
            f.write(f"password = '{password}'\n")
            f.write(f"database = '{database}'\n")

        # Redirect to the home page
        return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/index')
def index():
    # Get the data for active_population
    with open('src/active_population', 'r') as file:
        raw_student_population = data_request.retrieve(file.read())

    # Process the data for active_population
    student_population = []
    for item in raw_student_population:
        new_item = (item[0], item[1], item[2], item[3])
        student_population.append(new_item)

    student_population_sorted = sorted(student_population, key=lambda x: x[0])

    # Create the chart for active_population
    first_chart.create_chart(raw_student_population)

    # Get the data for overall_attendance
    with open('src/overall_attendance', 'r') as file:
        raw_overall_attendance = data_request.retrieve(file.read())

    # Process the data for overall_attendance
    overall_attendance = []
    for item in raw_overall_attendance:
        new_item = (item[0], item[1], item[2],f"{round(item[-1])}%")
        overall_attendance.append(new_item)

    # Sort the data for overall_attendance
    overall_attendance = sorted(overall_attendance, key=lambda x: x[0])

    # Create the chart for active_population
    second_chart.create_chart(raw_overall_attendance)

    course = request.args.get('course')
    year = request.args.get('year')
    period = request.args.get('period')

    if course and year and period:
        # If all parameters exist, redirect to another page
        return redirect(url_for('populations/<course>/<period>/<year>'))

    # Render the template
    return render_template('index.html', student_population=student_population_sorted, overall_attendance=overall_attendance)

@app.route('/populations/<course>/<period>/<year>', methods=['GET'])
def other_page(course, period, year):
    # This is the other page you want to redirect to
    return render_template('other_page.html')

if __name__ == '__main__':
    app.run(debug=True)
