from locust import HttpUser, task


class MyUser(HttpUser):    # nazwy klas powinno się definiować z wielkiej litery
    @task
    def get_posts(self):
        self.client.get("/posts")


'''
w terminalu wpisać: locust -f locustfile.py --host=https://jsonplaceholder.typicode.com
url po host mozesz zastapic url-em czegokolwiek, co testujesz
'''