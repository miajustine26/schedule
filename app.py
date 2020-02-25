from flask import Flask, render_template, url_for, flash, redirect
from datetime import datetime
from dictionary import *
import helper
from forms import LogInForm, RegistrationForm, ScheduleMakerForm

app=Flask(__name__)
app.config['SECRET_KEY']='98dbbe3f67bcb7583b15d5fd0494c8cd'

@app.route('/time')
def timeDisplay():
    timeData=helper.time()
    return render_template('time.html', time=timeData, posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form=LogInForm()
    if form.validate_on_submit():
        if form.email.data=="bob@bob.com" and form.password.data=="bob123456":
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Please check your username and password', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/schedulemaker')
def schedulemaker():
    form=ScheduleMakerForm()
    return render_template('schedulemaker.html', form=form)

if __name__=='__name__':
    app.run(debug=True)
