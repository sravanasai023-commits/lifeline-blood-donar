from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "lifelink123"

DATABASE = "lifelink.db"

# -----------------------------
# Home
# -----------------------------
@app.route('/')
def home():
    return render_template('index.html')

# -----------------------------
# Login
# -----------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            flash("Login Successful!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid Email or Password", "danger")

    return render_template("login.html")

# -----------------------------
# Signup
# -----------------------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        blood = request.form['blood_group']
        city = request.form['city']

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO users(name,email,password,blood_group,city)
        VALUES(?,?,?,?,?)
        """, (name,email,password,blood,city))

        conn.commit()
        conn.close()

        flash("Account Created Successfully!", "success")
        return redirect(url_for("login"))

    return render_template("signup.html")

# -----------------------------
# Register Donor
# -----------------------------
@app.route('/register', methods=['GET','POST'])
def register():

    if request.method == 'POST':

        data = (
            request.form['name'],
            request.form['email'],
            request.form['phone'],
            request.form['gender'],
            request.form['age'],
            request.form['blood_group'],
            request.form['city'],
            request.form['address'],
            request.form['last_donation'],
            request.form['availability']
        )

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO donors
        (name,email,phone,gender,age,blood_group,city,address,last_donation,availability)
        VALUES (?,?,?,?,?,?,?,?,?,?)
        """, data)

        conn.commit()
        conn.close()

        flash("Donor Registered Successfully!", "success")
        return redirect(url_for('home'))

    return render_template("register.html")

# -----------------------------
# Find Blood
# -----------------------------
@app.route('/find_blood', methods=['GET','POST'])
def find_blood():

    donors=[]

    if request.method=="POST":

        blood=request.form['blood_group']
        city=request.form['city']

        conn=sqlite3.connect(DATABASE)
        cursor=conn.cursor()

        cursor.execute("""
        SELECT * FROM donors
        WHERE blood_group=? AND city=?
        """,(blood,city))

        donors=cursor.fetchall()

        conn.close()

    return render_template("find_blood.html", donors=donors)

# -----------------------------
# Emergency
# -----------------------------
@app.route('/emergency', methods=['GET','POST'])
def emergency():

    if request.method=="POST":

        conn=sqlite3.connect(DATABASE)
        cursor=conn.cursor()

        cursor.execute("""
        INSERT INTO blood_requests
        (patient_name,blood_group,hospital,city,phone,required_date,notes)
        VALUES (?,?,?,?,?,?,?)
        """,(
            request.form['patient_name'],
            request.form['blood_group'],
            request.form['hospital'],
            request.form['city'],
            request.form['phone'],
            request.form['required_date'],
            request.form['notes']
        ))

        conn.commit()
        conn.close()

        flash("Emergency Request Submitted!", "success")

        return redirect(url_for('home'))

    return render_template("emergency.html")

# -----------------------------
# About
# -----------------------------
@app.route('/about')
def about():
    return render_template("about.html")

# -----------------------------
# Contact
# -----------------------------
@app.route('/contact', methods=['GET','POST'])
def contact():

    if request.method=="POST":

        conn=sqlite3.connect(DATABASE)
        cursor=conn.cursor()

        cursor.execute("""
        INSERT INTO contacts(name,email,message)
        VALUES(?,?,?)
        """,(
            request.form['name'],
            request.form['email'],
            request.form['message']
        ))

        conn.commit()
        conn.close()

        flash("Message Sent Successfully!", "success")

    return render_template("contact.html")

# -----------------------------
# Dashboard
# -----------------------------
@app.route('/dashboard')
def dashboard():

    conn=sqlite3.connect(DATABASE)
    cursor=conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM donors")
    donors=cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM blood_requests")
    requests=cursor.fetchone()[0]

    conn.close()

    return render_template(
        "dashboard.html",
        donors=donors,
        requests=requests
    )

# -----------------------------
if __name__=="__main__":
    app.run(debug=True)