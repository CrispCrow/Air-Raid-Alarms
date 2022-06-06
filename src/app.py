from flask import Flask, render_template

from .utils import air_raids_status, parse_date

app = Flask(__name__)


@app.route('/')
def main_page() -> render_template:
    return render_template('main_page.html',
                           alarms=air_raids_status(active_alarms=True),
                           parse=parse_date)


@app.route('/last_alarms')
def last_alarms() -> render_template:
    return render_template('last_alarms.html',
                           alarms=air_raids_status(active_alarms=False),
                           parse=parse_date)
