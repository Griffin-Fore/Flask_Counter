from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] + 0
    else:
        session['count'] = 0
    return render_template("index.html")

@app.route('/count', methods=['POST'])
def count_session():
    print('Counting Session')
    session['count'] += 1
    print('session', session)
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def reset():
    session.clear()
    print('session', session)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)