import requests
import datetime
import typing

from .config import config

SecondsT = typing.TypeVar('SecondsT', float, int)


def request() -> dict:
    """
    Функция делает запрос к API и возвращает ответ в виде JSON

    :return: JSON ответ от API
    """

    response = requests.get(config['api_url_states'], headers=config['headers'])
    return response.json()


def get_air_raid_status(active_alarms: bool) -> list[str]:
    """
    Функция фильтрует API-ответ со статусами воздушных тревог

    :return: Список с активными тревогами
    """

    alarms = request()['states']

    filtered_alarms = list(
        filter(lambda element: element['alert'] is active_alarms, alarms)
    )

    return filtered_alarms


def display_time(seconds: SecondsT, language: str) -> str:
    """
    Функция выполняет парсинг секунд и переводит результат в указанный язык

    :param seconds: Секунды, которые нужно форматировать
    :param language: Язык для вывода
    :return: Строка с отформатированным временем
    """

    parser = {'en': parse_en_time, 'ua': parse_ua_time}
    return parser[language](seconds)


def parse_en_time(seconds: SecondsT) -> str:
    result = []

    for name, count in config['intervals']:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')

            result.append('{} {}'.format(int(value), name))

    return ', '.join(result[:2])


def parse_ua_time(seconds: SecondsT) -> str:
    result = []

    for name, count in config['ua_intervals']:
        value = seconds // count
        if value:
            seconds -= value * count
            result.append('{} {}'.format(int(value), name))

    return ', '.join(result[:2])


def parse_date(date: str, language='en') -> str:
    """
    Функция получает дату от API в виде строки,
    отнимает текущее время от полученного и возвращает разницу в секундах

    :param date: Дата
    :return: Разница в секундах текущей даты от полученной
    """

    parsed = datetime.datetime.now().astimezone() - \
        datetime.datetime.fromisoformat(date)

    return display_time(parsed.total_seconds(), language=language)
