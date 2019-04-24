from lib.journals import *
import re

PARENS = '(%s)'
NUMBER_SEPARATED = u', \d+ %s \d+[, \u2013]'

## TODO: add ", %s ," around all journal names for citations, to avoid things like Transactions being cited everywhere.
## TODO: check for journal misspellings?
## TODO: add check for spacing errors with \s+
def all_journals_regex():
    return PARENS % (
        '|'.join(map(lambda x: NUMBER_SEPARATED % JOURNALS[x].short.replace('.', '\\.'), range(len(JOURNALS)))))

def extract_cites(case):
    cites = []

    if len([m for m in re.finditer(all_journals_regex(), case['casebody']['data'])]) == 0:
        return cites

    for i in JOURNALS:
        j_cites = [m for m in re.finditer(PARENS % (NUMBER_SEPARATED % (JOURNALS[i].short)), case['casebody']['data'])]
        for cite in j_cites:
            cites.append([i, cite])

    return cites
