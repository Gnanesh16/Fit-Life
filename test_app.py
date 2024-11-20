import unittest
from app import app  # Import the Flask app from your main Python file

class FlaskAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Runs before any test is executed."""
        cls.client = app.test_client()

    def test_home_page(self):
        """Test that the home page loads correctly"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)  # Make sure 'Home' appears on the home page

    def test_health_benefits_page(self):
        """Test that the health benefits page loads correctly"""
        response = self.client.get('/health-benefits')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Health Benefits', response.data)

    def test_workouts_page(self):
        """Test that the workouts page loads correctly"""
        response = self.client.get('/workouts')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Workouts', response.data)

    def test_diet_page(self):
        """Test that the diet page loads correctly"""
        response = self.client.get('/diet')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Diet', response.data)

if __name__ == '__main__':
    unittest.main()
