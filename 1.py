from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import session
from flask import g
from sqlite3 import dbapi2 as sqlite3
from datetime import datetime
import functions as f

app = Flask(__name__)
app.secret_key = 'super secret key'

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run()

# SERVICE FUNCTIONS
# Database
# {{
def init_db():
    """Initializes the database."""
    db = get_db();
    with app.open_resource('schema.sql', mode='r') as f:
        script=f.read();
        db.cursor().executescript(script);
    db.commit();

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect("sqlite.db")
    rv.row_factory = sqlite3.Row
    return rv

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
# }}

# BASIC FUNCTIONS

def workon(request):
    """ Get user input, save it, and send to thank you page """
    error=None;

    name = request.form.get('myname')
    fage = request.form.get('age')
    gender = request.form.get('gender')
    fnoshare = request.form.get('noshare')
    
    if not name:
        error='Username is required'; 
    if not gender:
        # TODO: Sanitize it based on expected values
        gender='na'
    if not fage:
        age="N/A";
    else:
        try:
            # TODO: something smarter
            # Do I have to be so aggressive?
            t=int(fage)
            if (t<120):
                age=str(t)
            else:
                age="N/A"
        except ValueError:
            age="N/A"

    if not fnoshare:
        noshare=False;
    elif (fnoshare=="noshare"):
        noshare=True;
    else:
        noshare=False;

    l1 = request.form.getlist("nlist1[]");
    l1len=len(l1);
    l2 = request.form.getlist("nlist2[]");
    l2len=len(l2);

    #except KeyError:
    #    app.logger.warning('keyerror');
    #    l2len=0;
    #    l2=[];

    # Save the results
    db = get_db()
    db.execute('insert into entries (name, age, gender, nlist1, n1, nlist2, n2, ip, date, noshare) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
               [name, age, gender, str(l1), l1len, str(l2), l2len,  "127.9.9.91", datetime.now(), noshare])
    db.commit()
    if error is None:
        return render_template('res.html', name=name, nn1=l1len, nn2=l2len);
    flash(error);
    return render_template('res.html', name=name);

# ROUTES


@app.route('/res', methods=['GET', 'POST'])
def userres():
    if request.method == 'POST':
        return workon(request);
    else:
        return redirect(url_for('finalres'))

@app.route('/finalres')
def finalres():
    """ We calculate and output the final results and statistics"""
    db = get_db()
    cur = db.execute('select name, gender, age, n1, n2, noshare from entries order by id desc')
    entries = cur.fetchall()
    print(format(entries))
    app.logger.warning(entries)
    return render_template('results.html', entries=entries);

@app.route('/')
def generate():
    n1, n2 = f.generate_names(50);
    return render_template('index.html', names1=n1, names2=n2);

# TODO
# security
# rate limiting
# Nice words formatting
