import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session
from model import Donor, Donation

app = Flask(__name__)
#app.secret_key = b'\xb6x(\xd67\x1f\xa7\x15\x92\xf1VqU\xe9|\xbcqu\xac\xf6\x16\xa8\x8f\xe5'
app.secret_key = os.environ.get('SECRET_KEY').encode()

@app.route('/')
def home():
	"""Redirects to home (http://localhost:6738/donations/)"""
	return redirect(url_for('all'))


@app.route('/donations/')
def all():
	"""All Donations (http://localhost:6738/donations/)"""
	donations = Donation.select()
	return render_template('donations.html', donations=donations)


@app.route('/create/', methods=['GET', 'POST'])
def create():
	"""Create Donation (http://localhost:6738/create/)"""
	if request.method == 'POST':
		donor = Donor(name=request.form['name'])
		donor.save()

		donation = Donation(donor=donor, value=int(request.form['donation']))
		donation.save()

		return redirect(url_for('all'))
	else:
		return render_template('create.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
