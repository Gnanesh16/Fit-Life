import unittest
from app import app

class TestFitLifeApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to FitLife!', response.data)

    def test_health_benefits_page(self):
        response = self.app.get('/health-benefits')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Health Benefits', response.data)

    def test_workouts_page(self):
        response = self.app.get('/workouts')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Workouts', response.data)

    def test_diet_page(self):
        response = self.app.get('/diet')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Diet Plans', response.data)

if __name__ == '__main__':
    unittest.main()
