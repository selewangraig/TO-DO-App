from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#initialize an empty list to store tasks
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    #get the task from the form
    task = request.form.get('task')
    #add the task to the list
    tasks.append(task)
    #redirect to the index page
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    if task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
