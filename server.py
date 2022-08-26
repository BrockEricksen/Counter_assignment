from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "therknplsdn"

@app.route('/')
def main():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def clear_count():
    session['count'] = 0
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
