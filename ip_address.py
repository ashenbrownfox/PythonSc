import os

def get_ip_address(url):
    command = "host "+url
    process = os.popen(command)
    result = str(process.read())
    marker = result.find('has address') + 12 #returns the location of beginning of has address
    return result[marker:].splitlines()[0]

print(get_ip_address('thenewboston.com'))