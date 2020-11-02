import fbchat
import re
fbchat._util.USER_AGENTS    = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"]
fbchat._state.FB_DTSG_REGEX = re.compile(r'"name":"fb_dtsg","value":"(.*?)"')

def login(fb_id, fb_pw):
    client = Client(fb_id, fb_pw)

def send(fb_msg):
    client.send(Message(text=fb_msg), thread_id=client.uid, thread_type=ThreadType.USER)