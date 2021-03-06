from . import *
import urllib2
import urllib
import re

_URL_RE = "(https?[^\s]*)"
#http://v.gd/create.php?format=simple&url=www.example.com


@privmsg
def shorten(who, what, where):
    res = re.search(_URL_RE, what)
    if not res:
        return

    url = res.group(0)
    if len(url) <= 18:
        return 

    content = urllib2.urlopen("http://v.gd/create.php?format=simple&url={}"
        .format(urllib.quote(url))).read()
    say(where, "<Shortened: {LINK}%s{} >" % content)
