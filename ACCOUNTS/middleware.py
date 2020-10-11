import pytz

from django.utils.timezone import activate


class TimezoneMiddleware(object):
    def process_request(self, request):
        activate(pytz.timezone('Asia/Kolkata'))
