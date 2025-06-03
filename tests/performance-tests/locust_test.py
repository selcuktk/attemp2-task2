from locust import HttpUser, task, between
from tests.helpers import predict_test


class PerformanceTests(HttpUser):
    # wait_time = between(1, 3)

    @task
    def test_internship_predict(self):
        res = predict_test(self.client, "/predict/internship/")
        print(res.json())

