from flask import Flask, render_template

app = Flask(__name__)

# Sample employee data
employees = [
    {"employee_nm": "Roderg", "email": "employee1@example.com", "employee_id": 1},
    {"employee_nm": "Roderg", "email": "employee2@example.com", "employee_id": 2},
    {"employee_nm": "Roderg", "email": "employee3@example.com", "employee_id": 3},
    {"employee_nm": "Roderg", "email": "employee4@example.com", "employee_id": 4},
    {"employee_nm": "Roderg", "email": "employee5@example.com", "employee_id": 5},
    {"employee_nm": "Roderg", "email": "employee6@example.com", "employee_id": 6},
]

@app.route('/')
def index():
    return render_template('index.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)
