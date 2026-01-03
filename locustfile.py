cat > locustfile.py << 'EOF'
from locust import HttpUser, task, between
import time

class WebsiteUser(HttpUser):
    wait_time = between(3, 7)
    
    @task(4)
    def load_main_page(self):
        self.client.get("/")
        time.sleep(1)
    
    @task(3)
    def load_news(self):
        self.client.get("/news")
        time.sleep(2)
    
    @task(2)
    def load_teachers(self):
        self.client.get("/teachers")
        time.sleep(3)
    
    @task(1)
    def load_detail_page(self):
        self.client.get("/news/1")
        time.sleep(1.5)
    
    def on_start(self):
        self.client.get("/favicon.ico")
EOF