from locust import HttpUser, task, between


class MyUser(HttpUser):
    host = "https://test.api.pricing.safarbazi.com"  # Set the base host URL here
    wait_time = between(1, 1)  # Wait between 1 and 3 seconds between requests
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3NDU5ODIxLCJpYXQiOjE3MDcyODcwMjEsImp0aSI6ImUxZTFhYTBhMzk3NzQyOGY5ODc4NWMzNzQ5YjIxMGU4IiwidXNlcl9pZCI6N30.zQ7h1WgfUBG5zHk-ilV8oU2vljAWzyyJYVc9NClVJPU"
    }

    @task
    def get_root(self):
        self.client.get("/provinces?page_size=50", headers=self.headers)  # Send a GET request to the root API endpoint


    @task
    def get_properties(self):
        self.client.get("/properties/updated/rooms?property_status=all", headers=self.headers)  # Send a GET request to the root API endpoint

    # Add more tasks for other API endpoints you want to test
    # @task
    # def post_data(self):
    #     self.client.get("/some-endpoint", json={"data": "value"})