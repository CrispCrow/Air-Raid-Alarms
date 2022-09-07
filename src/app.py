from flask import Flask, render_template

from .utils import get_air_raid_status, parse_date

app = Flask(__name__)


@app.route('/')
def main_page() -> str:
    return render_template(
        template_name_or_list='main_page.html',
        alarms=get_air_raid_status(active_alarms=True),
        parse=parse_date
    )


@app.route('/last_alarms')
def last_alarms() -> str:
    return render_template(
        template_name_or_list='last_alarms.html',
        alarms=get_air_raid_status(active_alarms=False),
        parse=parse_date
    )


@app.route('/ua/main_page')
def active_ua_alarms() -> str:
    return render_template(
        template_name_or_list='ua/main_page.html',
        alarms=get_air_raid_status(active_alarms=True),
        parse=parse_date
    )


@app.route('/ua/last_alarms')
def last_ua_alarms() -> str:
    return render_template(
        template_name_or_list='ua/last_alarms.html',
        alarms=get_air_raid_status(active_alarms=False),
        parse=parse_date
    )
