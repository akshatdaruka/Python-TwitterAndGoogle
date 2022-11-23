import re
def logs():
    with open("qu1.txt", "r") as file:
        logdata = file.read()

    pattern='''
    (?P<host>[\d.]*)                #host
    (\s\-\s)
    (?P<user_name>[\w-]*)           #user name
    (\s\[)
    (?P<time>[\w\s].*)           #time
    (\]\s\")
    (?P<request>[\w].+)         #request
    (\"\s[\d]*\s[\d]*)
    '''
    final=list()
    for items in re.finditer(pattern,logdata,re.VERBOSE):
        final.append(items.groupdict())
    return final
assert len(logs()) == 979

one_item={'host': '146.204.224.152',
  'user_name': 'feest6811',
  'time': '21/Jun/2019:15:45:24 -0700',
  'request': 'POST /incentivize HTTP/1.1'}
assert one_item in logs(), "Sorry, this item should be in the log results, check your formating"
