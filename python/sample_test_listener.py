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


def timestring():
    now = datetime.datetime.now()
    return datetime.datetime.strftime(now, "%m:%S.%f")[:-5]


print("1. Parsing locustfile, happens before anything else")

# If you want to get something over HTTP at this time you can use `requests` directly:
global_test_data = requests.post(
    "https://postman-echo.com/post",
    data="global_test_data_" + timestring(),
).json()["data"]

test_run_specific_data = None


@events.init.add_listener
def init(environment, **_kwargs):
    print("2. Initializing locust, happens after parsing the locustfile but before test start")


@events.quitting.add_listener
def quitting(environment, **_kwargs):
    print("9. locust is about to shut down")


@events.test_start.add_listener
def test_start(environment, **_kwargs):
    # happens only once in headless runs, but can happen multiple times in web ui-runs
    global test_run_specific_data
    print("3. Starting test run")
    # in a distributed run, the master does not typically need any test data
    if not isinstance(environment.runner, MasterRunner):
        test_run_specific_data = requests.post(
            "https://postman-echo.com/post",
            data="test-run-specific_" + timestring(),
        ).json()["data"]


@events.quit.add_listener
def quit(exit_code, **kwargs):
    print(f"10. Locust has shut down with code {exit_code}")


@events.test_stopping.add_listener
def test_stopping(environment, **_kwargs):
    print("6. stopping test run")


@events.test_stop.add_listener
def test_stop(environment, **_kwargs):
    print("8. test run stopped")


class MyUser(HttpUser):
    host = "https://postman-echo.com"
    wait_time = constant(180)  # be nice to postman-echo
    first_start = True

    def on_start(self):
        if MyUser.first_start:
            MyUser.first_start = False
            # This is useful for similar things as to test_start, but happens in the context of a User
            # In the case of a distributed run, this would be run once per worker.
            # It will not be re-run on repeated runs (unless you clear the first_start flag)
            print("X. Here's where you would put things you want to run the first time a User is started")

        print("4. A user was started")
        # This is a good place to fetch user-specific test data. It is executed once per User
        # If you do not want the request logged, you can replace self.client.<method> with requests.<method>
        self.user_specific_testdata = self.client.post(
            "https://postman-echo.com/post",
            data="user-specific_" + timestring(),
        ).json()["data"]

    @task
    def t(self):
        # self.client.get(f"/get?{global_test_data}")
        # self.client.get(f"/get?{test_run_specific_data}")
        self.client.get(f"/get?{self.user_specific_testdata}")

        print("5. Getting task-run-specific testdata")
        # If every iteration is meant to use new test data this is the most common way to do it
        task_run_specific_testdata = self.client.post(
            "https://postman-echo.com/post",
            data="task_run_specific_testdata_" + timestring(),
        ).json()["data"]
        self.client.get(f"/get?{task_run_specific_testdata}")
        
    @task
    def t2(self):
        self.client.get(f"/get?{global_test_data}")
        self.client.get(f"/get?{test_run_specific_data}")
        # self.client.get(f"/get?{self.user_specific_testdata}")

        print("5. Getting task-run-specific testdata")
        # If every iteration is meant to use new test data this is the most common way to do it
        task_run_specific_testdata = self.client.post(
            "https://postman-echo.com/post",
            data="task_run_specific_testdata_" + timestring(),
        ).json()["data"]
        self.client.get(f"/get?{task_run_specific_testdata}")

    def on_stop(self):
        # this is a good place to clean up/release any user-specific test data
        print("7. a user was stopped")