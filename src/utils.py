import requests
import datetime

from .config import config


def request() -> dict:
    """
    Функция делает запрос к API и возвращает ответ в виде JSON

    :return: JSON ответ от API
    """

    response = requests.get(
        config['api_url_states'], headers=config['headers'])

    return response.json()


def air_raids_status(active_alarms: bool) -> list:
    """
    Функция фильтрует API-ответ со статусами воздушных тревог

    :return: Список с активными тревогами
    """

    alarms = request()['states']

    filtered_alarms = list(
        filter(lambda element: element['alert'] is active_alarms, alarms))

    return filtered_alarms


def display_time(seconds: int) -> str:
    """
    Функция форматирует секунды в нормальный вид weeks, days, hours, seconds

    :param seconds: Секунды, которые нужно форматировать
    :return: Строка с отформатированным временем
    """

    result = []

    for name, count in config['intervals']:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')

            result.append("{} {}".format(int(value), name))

    return ', '.join(result[:2])


def parse_date(date: str) -> str:
    """
    Функция получает дату от API в виде строки,
    отнимает текущее время от полученного и возвращает разницу в секундах

    :param date: Дата
    :return: Разница в секундах текущей даты от полученной
    """

    parsed = datetime.datetime.now().astimezone() - \
        datetime.datetime.fromisoformat(date)

    return display_time(parsed.total_seconds())
