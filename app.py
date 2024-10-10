
from flask import Flask, request, render_template, session, redirect, url_for
import mysql.connector

# Establish database connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Fatema@06',
    database='cms'
)

# Create Flask application
app = Flask(__name__, template_folder='templates')
app.secret_key = 'fatema'

# Route for the landing page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the home1 page
@app.route('/home1')
def home1():
    if 'firstname' in session and 'lastname' in session:
        firstname = session['firstname']
        lastname = session['lastname']
        return render_template('home1.html', firstname=firstname, lastname=lastname)
    else:
        return redirect(url_for('show_login'))

# Route for the signup page
@app.route('/s')
def signup():
    return render_template('signup.html')

# Route for the login page
@app.route('/l')
def show_login():
    return render_template('login.html')

# Route for the menu page
@app.route('/m')
def menu():
    return render_template('menu.html')

@app.route('/m1')
def menu1():
    return render_template('menu1.html')

# Route for the payment page
@app.route('/payment')
def payment():
    return render_template('payment.html')

# Route to handle form submission
@app.route('/submit', methods=["POST"])
def submit():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    password = request.form['password']

    cursor = conn.cursor()
    sql = "INSERT INTO signup (firstname, lastname, email, password) VALUES (%s, %s, %s, %s)"
    val = (firstname, lastname, email, password) 
    cursor.execute(sql, val)
    conn.commit()
    cursor.close()

    session['firstname'] = firstname
    session['lastname'] = lastname

    return redirect(url_for('home1'))

def check_login(email, password):
    try:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM signup WHERE email = %s AND password = %s"
        cursor.execute(query, (email,password))
        user_data = cursor.fetchone()
        if user_data:
            return user_data
        
    finally:
        cursor.close()

    return None

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == 'admin@gmail.com' and password == 'admin123':
            session['admin_logged_in'] = True
            return redirect(url_for('admin'))
        else:
            user_data = check_login(email, password)
            if user_data:
                session['logged_in'] = True
                session['email'] = email
                session['firstname'] = user_data['firstname']
                session['lastname'] = user_data['lastname']
                return redirect(url_for('home1'))
            else:
                return "Invalid login credentials. Please try again."

@app.route('/admin')
def admin():    
    admin_data = session.get('admin_data')
    print("Admin Data:", admin_data)
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT s.firstname, s.lastname, s.email, o.id, o.item, o.price, o.quantity 
                FROM `signup` s 
                JOIN `order` o ON s.email = o.cust_email
            """)
            orders = cursor.fetchall()

            cursor.execute("SELECT firstname, lastname, email FROM signup")
            users = cursor.fetchall()

            cursor.execute("SELECT fname, email, address, city, pincode, phone FROM payment")
            payments = cursor.fetchall()

            for order in orders:
                print(order)

    except Exception as e:
        print("Error occurred:", e)
        orders = []
        users = []
        payments = []

    return render_template('admin.html', orders=orders, users=users, payments=payments)

@app.route('/payment', methods=["POST"])
def process_payment():
    fname = request.form['fname']
    email = request.form['email']
    address = request.form['address']
    city = request.form['city']
    pincode = request.form['pincode']
    phone = request.form['phone']

    cursor = conn.cursor()
    dal = "INSERT INTO payment (fname, email, address, city, pincode, phone) VALUES (%s, %s, %s, %s, %s, %s)"
    vali = (fname, email, address, city, pincode, phone)
    cursor.execute(dal, vali)
    conn.commit()
    cursor.close()

    return render_template('home1.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
