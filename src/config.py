import os

config = {
    'api_url_states': os.environ.get('API_URL_STATES'),
    'headers': {
        'X-API-Key': os.environ.get('API_KEY')
    },
    'intervals': (
        ('weeks', 604800),
        ('days', 86400),
        ('hours', 3600),
        ('minutes', 60),
        ('seconds', 1)
    ),
    'ua_intervals': (
        ('неділі', 604800),
        ('дні', 86400),
        ('години', 3600),
        ('хвилини', 60),
        ('секунди', 1)
    )
}
