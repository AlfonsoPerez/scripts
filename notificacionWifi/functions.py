import urllib.request, base64
import subprocess
import re
regexp = re.compile('<td>(192\.168\.1\.[0-9]{1,3})</td><td>([0-9\:a-f]{17})</td>')

def getHtml():
    
    username = 'admin'
    password = '*****'
    url = 'http://192.168.1.1/Rg802dot11AccessFilterGN.asp'
    request = urllib.request.Request(url)
    string = ('%s:%s' % (username, password))
    base64string = base64.b64encode(string.encode('ascii')).decode('utf-8')
    request.add_header("Authorization", "Basic %s" % base64string)   
    return urllib.request.urlopen(request).read().decode('utf-8')


def getUsers(html):
   
    return regexp.findall(html)
    
  
def diff(a, b):
        b = set(b)
        return [aa for aa in a if aa not in b]
  
def notification(summary, note):
    
    subprocess.call(["notify-send", summary, note])
    

def print_user(listu):
    return str(listu[0] + ' with mac ' + listu[1])