from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route('/')
def hello():
    #app.logger.warning('A warning occurred (%d apples)', 42)
    #app.logger.error('An error occurred')
    return render_template('index.html');

@app.route('/res', methods=['GET', 'POST'])
def userres():
    if request.method == 'POST':
        name = request.form['myname']
        try:
            l1 = request.form.getlist("name[]");
            l1len=len(l1);
        except KeyError:
            app.logger.warning('keyerror');
            l1len=0;
            l1=[];
        try:
            l2 = request.form.getlist("name2[]");
            l2len=len(l2);
        except KeyError:
            app.logger.warning('keyerror');
            l2len=0;
            l2=[];

        return render_template('res.html', name=name, l1=l1, l2=l2, l1l=l1len, l2l=l2len);
    else:
        return redirect(url_for('finalres'))

@app.route('/finalres')
def finalres():
    return render_template('results.html');
