from django.contrib.auth.models import User
from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint

def run():
    # enter code below


    pprint(connection.queries)
