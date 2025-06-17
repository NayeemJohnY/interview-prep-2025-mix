# This example shows the various ways to run things before/outside of the normal task execution flow,
# which is very useful for fetching test data.
#
# 1. Locustfile parse time
# 2. Locust start (init)
# 3. Test start
# 4. User start
# 5. Inside a task
# ...
# 6. Test run stopping
# 7. User stop
# 8. Test run stop
# (3-8 are repeated if you restart the test in the UI)
# 9. Locust quitting
# 10. Locust quit
#
# try it out by running:
#  locust -f test_data_management.py --headless -u 2 -t 5
from locust.user.wait_time import constant
from locust import HttpUser, task
from locust import events
from locust.runners import MasterRunner
import requests
import datetime
from locust.event import EventHook

def email():
    print("email")
    print("ssssss")
    
def test(dd):
    print('stop')
    print('qqqqqq', dd)

send_email_notify = EventHook()    
send_email_notify.add_listener(email)

testssws = EventHook()
testssws.add_listener(test)

class User(HttpUser):
    host ="https://google.com"
    @task
    def t(self):
        send_email_notify.fire()
        print("dasdasa")  
        testssws.fire(dd='pola')