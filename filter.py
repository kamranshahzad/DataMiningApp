__author__ = 'kamran'

from jobsearch.models import dictionary_exceptions
import json

class Filter:

    def __init__(self):
        a=10

    def fill(self):
        filter_sets = {}
        exceptions_entries = dictionary_exceptions.objects.all()
        for i in exceptions_entries:
            filter_sets[i.exception_id] = json.loads(i.word_pairs)

        return filter_sets


