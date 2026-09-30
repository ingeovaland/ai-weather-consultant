from flask import Flask, render_template, request, redirect, url_for, session
from theagent import agent
import uuid

app = Flask(__name__)
app.secret_key = "app.secret_key"
#eh necessario criar uma app.secret_key quando usamos a var session



@app.route('/')
def home():
    session['thread_id'] = str(uuid.uuid4()) #vai gerar um id unico para cada user
    if 'messages' not in session:
        session['messages'] = []
    print('home', session)
    return render_template('chat.html', messages=session['messages'])

@app.route('/send', methods=['POST'])
def send():
    user_message = request.form['message']
    user_lat = request.form.get('latitude')
    user_lon = request.form.get('longitude')
    print(user_lat, user_lon)

    if user_lat and user_lon:
        session['user_location'] = {'lat': user_lat, 'lon': user_lon}

    response = agent.invoke({"messages": [{'role': 'user', 'content':user_message}]},
    {"configurable": {"thread_id": session['thread_id']}})

    session['messages'].append({'type': 'human', 'content': user_message})
    session['messages'].append({'type': 'ai', 'content': response['messages'][-1].content[0]['text']})
    session.modified = True
    print(session)
    return redirect(url_for('home'))

app.run(debug=True)

#@app.route('/clear')
#def clear():