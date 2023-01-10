from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MYSQL_HOST'] = 'sql10.freesqldatabase.com'
app.config['MYSQL_USER'] = 'sql10581776'
app.config['MYSQL_PASSWORD'] = 'Thaj7NANnu'
app.config['MYSQL_DB'] = 'sql10581776'

mysql = MySQL(app)


@app.route('/',methods=['GET','POST'])
def index():
    print("INSIDE LOGIN")
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:   
        email = request.form['email']
        password = request.form['password']
        print(email,password)
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO Login(email,password) VALUES(%s,%s)",(email,password))
        mysql.connection.commit()
        cursor.close()

    if request.method == 'POST' and 'email' in request.form and 'psw' in request.form and 'psw-repeat' in request.form:   
        email = request.form['email']
        password = request.form['psw']
        RepeatPassword =request.form['psw-repeat']
        print(email,password,RepeatPassword)
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO Account(email,password,RepeatPassword) VALUES(%s,%s,%s)",(email,password,RepeatPassword))
        mysql.connection.commit()
        cursor.close()
    if request.method == 'POST' and 'country' in request.form and 'country1' in request.form  and 'adultDiv' in request.form and 'childDiv' in request.form and 'infantDiv' in request.form:
        Begin = request.form['country']
        End = request.form['country1']
        Adult =request.form['adultDiv']
        Children =request.form['childDiv']
        Infant =request.form['infantDiv']
        print(Begin,End,Adult,Children,Infant)
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO Flights(Begin,End,Adult,Children,Infant) VALUES(%s,%s,%s,%s,%s)",(Begin,End,Adult,Children,Infant))
        mysql.connection.commit()
        cursor.close()
    if request.method == 'POST' and 'start' in request.form and 'end' in request.form  and 'class' in request.form and 'trainad' in request.form and 'trainch' in request.form and 'trainsm' in request.form and 'trainw' in request.form:
        Begin = request.form['start']
        End = request.form['end']
        comfort =request.form['class']
        adult =request.form['trainad']
        children =request.form['trainch']
        SeniorMen =request.form['trainsm']
        SeniorWomen =request.form['trainw']
        print(Begin,End,comfort,adult,children,SeniorMen,SeniorWomen)
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO Train(Begin,End,comfort,adult,children,SeniorMen,SeniorWomen) VALUES(%s,%s,%s,%s,%s,%s,%s)",(Begin,End,comfort,adult,children,SeniorMen,SeniorWomen))
        mysql.connection.commit()
        cursor.close()
    if request.method == 'POST' and 'selectCity' in request.form and 'travelRoom' in request.form:
        spot = request.form['selectCity']
        room =request.form['travelRoom']
        print(spot,room)
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO Hotels(spot,room) VALUES(%s,%s)",(spot,room))
        mysql.connection.commit()
        cursor.close()
    return render_template('index.html')
@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/activities')
def activities():
    return render_template('activities.html')

@app.route('/cancellation',methods=['GET','POST']) 
def cancellation():
    if request.method == 'POST' and 'id' in request.form and 'trip' in request.form:   
        emailId = request.form['id']
        tripId = request.form['trip']
        print(emailId,tripId)
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO Cancellation(emailId,tripId) VALUES(%s,%s)",(emailId,tripId))
        mysql.connection.commit()
        cursor.close() 
    return render_template('cancellation.html')

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

@app.route('/flightdeals')
def flightdeals():
    return render_template('flight-deals.html')

@app.route('/flightdetails')
def flightdetails():
    return render_template('flight-details.html')

@app.route('/hotelbooking')
def hotelbooking():
    return render_template('hotel-booking.html')

@app.route('/hoteldetails')
def hoteldetails():
    return render_template('hotel-details.html')


@app.route('/chennai')
def chennai():
    return render_template('chennai.html')

@app.route('/bangalore')
def bangalore():
    return render_template('bangalore.html')

@app.route('/mumbai')
def mumbai():
    return render_template('mumbai.html')

@app.route('/delhi')
def delhi():
    return render_template('delhi.html')

@app.route('/goa')
def goa():
    return render_template('goa.html')

if __name__=="__main__":
    app.run(debug=True)