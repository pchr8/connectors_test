from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import session

app = Flask(__name__)
app.secret_key = 'super secret key'

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run()

@app.route('/')
def hello():
    #app.logger.warning('A warning occurred (%d apples)', 42)
    #app.logger.error('An error occurred')
    return render_template('index.html');

@app.route('/res', methods=['GET', 'POST'])
def userres():
    error=None;
    if request.method == 'POST':
        name = request.form['myname']
        if not name:
                error='Username is required'; 
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
        if error is None:
            return render_template('res.html', name=name, l1=l1, l2=l2, l1l=l1len, l2l=l2len);
        flash(error);
        return render_template('res.html', name=name);

    else:
        return redirect(url_for('finalres'))

@app.route('/finalres')
def finalres():
    return render_template('results.html');
