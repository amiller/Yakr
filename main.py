from yakr.network import simple_connect, record, replay
from yakr.util import set_procname
from yakr.bot import Bot
import yakr.config as botconfig
import sys
set_procname("yakr")

config = botconfig.read("yakr.cfg")

connect_host = config["connection"]["host"]
connect_port = int(config["connection"]["port"])
nick = config["bot"]["nick"]
name = config["bot"]["name"]


net = None
if len(sys.argv) == 2:
    if sys.argv[1] == "record":
        conn = simple_connect((connect_host, connect_port))
        net = record(conn, "RECORD")
    if sys.argv[1] == "replay":
        net = replay("RECORD")
else:
    net = simple_connect((connect_host, connect_port))

b = Bot(net)
b.nick = nick
b.real_name = name
plugins = """alias
alarm
chance
colorize
date
fortune
gayify
google.define
google.search
google.youtube
invite
joiner
m528
maths
numbers
ping
repeater
replacements
sed
shortener
tell
titles
weather""".split("\n")
map(b.load, plugins)
b.run()
