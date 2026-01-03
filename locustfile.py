from locust import HttpUser, task, between
import time

class WebsiteUser(HttpUser):
    wait_time = between(3, 7)  # Пользователь ждет 3-7 секунд между действиями
    
    @task(4)  # Самая частая операция (40% вероятности)
    def load_main_page(self):
        self.client.get("/")
        time.sleep(1)  # Имитация чтения страницы
    
    @task(3)  # Частая операция (30% вероятности)
    def load_news(self):
        # Запрашиваем раздел новостей (предполагаемый URL)
        self.client.get("/news")
        time.sleep(2)
    
    @task(2)  # Средняя частота (20% вероятности)
    def load_teachers(self):
        # Запрашиваем раздел преподавателей
        self.client.get("/teachers")
        time.sleep(3)
    
    @task(1)  
    def load_detail_page(self):
        self.client.get("/news/1")
        time.sleep(1.5)
    
    def on_start(self):
        """Выполняется один раз при старте каждого пользователя"""
        # Запрашиваем фавиконку (обычное поведение браузера)
        self.client.get("/favicon.ico")
