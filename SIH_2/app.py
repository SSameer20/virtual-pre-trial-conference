from flask import Flask, render_template, Request
from flask import * 

import json
app = Flask(__name__)

lawyers_path='lawyers.json'
cases_path='cases.json'
def read_lawyers():
    with open(lawyers_path, "r") as json_file:
        return json.load(json_file)

def read_cases():
    with open(cases_path, "r") as json_file:
        return json.load(json_file)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/client')
def client():
    cases = read_cases()
    return render_template('client_dashboard.html', user_type='Client', username='Khadeer',cases=cases)

@app.route("/appeal", methods=['POST'])
def show_result():
    result = request.form()
    file_path = 'appealed.json'

    with open(file_path, 'r', encoding='utf-8') as json_file:
        appeal = json.load(json_file)

    print(appeal)
    appeal.append(result)
    print(result.get('case_details'))

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(appeal, json_file)
        print('JSON file updated successfully')
    return "hello"

@app.route('/appeal')
def appeal():
    lawyers = read_lawyers()
    return render_template('appeal.html', lawyers=lawyers, username='Khadeer')

@app.route('/client_cases')
def client_cases():
    cases = read_cases()
    return render_template('client_cases.html', username = "Khadeer", cases = cases)

@app.route('/judge')
def judge():
    cases=read_cases()
    return render_template('judge_dashboard.html', user_type= "Judge",cases=cases)

@app.route('/meeting')
def meeting():
    return render_template('meeting.html',username='Khadeer')

@app.route('/meeting/client')
def meeting1():
    return render_template('meeting.html',username='Client')

@app.route('/meeting/lawyer')
def meeting2():
    return render_template('meeting.html',username='Lawyer')

@app.route('/meeting/judge')
def meeting3():
    return render_template('meeting.html',username='Judge')

@app.route('/calender')
def calender():
    return render_template('calender.html')

@app.route('/j_search')
def search():
    return render_template('search.html')

@app.route('/j_search', methods=['POST'])
def j_search():
    cases_data=read_cases()
    search_param = request.form.get('search_param')
    search_query = request.form.get('search_query')
    results = []

    for case in cases_data:
        if search_query.lower() in case.get(search_param, '').lower():
            results.append(case)

    return jsonify(results)

@app.route('/notepad')
def notepad():
    return render_template('notepad.html')

@app.route('/lawyer')
def lawyer():
    return render_template('lawyer.html')

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug = True)