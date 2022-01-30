

from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('login.html')




x = 0
questions = []
monies = []

@app.route('/first', methods=['GET', 'POST'])
def first():
    if request.method == 'POST':
        questions.append(request.form)
        return render_template('budget.html', questions=questions)


data = {'Task' : 'Hours per Day'}
stop = 0
@app.route('/work', methods=['GET', 'POST'])
def work():
    global stop
    global tinc
    global rinc1
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        data[ request.form['City']] = int(request.form['Name'])
        if stop == 0:
            tinc = int(request.form['tinc'])
            stop +=1        

        sum = 0
        for elem in data:
            try:
                sum += int(data[elem])
            except:
                continue
        rinc1 = tinc - sum

        return render_template('pie-chart.html', data=data, tinc = tinc, rinc1=rinc1)


data2 = {'Task' : 'Hours per Day'}
help = 0
@app.route('/work2', methods=['GET', 'POST'])
def work2():
    global help
    global sum
    litplease = 0 
    if help == 0: 
        if request.method == 'GET':
            return f"The URL /data is accessed directly. Try going to '/form' to submit form"
        if request.method == 'POST':
            help += 1

            return render_template('budget2.html')

    elif help >= 1:
        if request.method == 'GET':
            return f"The URL /data is accessed directly. Try going to '/form' to submit form"
        if request.method == 'POST':
            data2[ request.form['City']] = int(request.form['Name'])

            sum = 0
            for elem in data:
                try:
                    sum += int(data2[elem])
                except:
                    continue
            
            return render_template('budget3.html',data2=data2, sum=sum)
    elif help < 0:
        if request.method == 'GET':
            return f"The URL /data is accessed directly. Try going to '/form' to submit form"
        if request.method == 'POST':
            return render_template('budget3.html',data2=data2, sum=sum)


@app.route('/work4', methods=['GET', 'POST'])
def work4():
    global help
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        help = -1
        return render_template('pie-chart.html', data=data, rinc1=rinc1,tinc=tinc)
