import unittest
from takehome_api.src.main import create_app
from takehome_api.src.database import db


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("development")
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_health_check(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_add_provider(self):
        data = {
            "provider": {
                "name": "Dr. Jane Doe",
                "states": ["CA", "NY"],
                "insurances": ["Aetna", "Blue Cross"]
            }
        }
        resp = self.client.post("/provider", json=data)
        self.assertEqual(resp.status_code, 201)
        self.assertIn("name", resp.get_json())

    def test_book_appointment_success(self):
        # add provider first
        self.client.post("/provider", json={
            "provider": {
                "name": "Dr. Jane Doe",
                "states": ["CA"],
                "insurances": ["Aetna"]
            }
        })
        # book appointment
        resp = self.client.post("/appointment", json={
            "patient": {
                "name": "John Doe",
                "email": "john@example.com",
                "state": "CA",
                "insurance": "Aetna"
            }
        })
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(resp.get_json()["scheduled"])

    def test_book_appointment_no_provider(self):
        resp = self.client.post("/appointment", json={
            "patient": {
                "name": "John Doe",
                "email": "john@example.com",
                "state": "TX",
                "insurance": "Nonexistent"
            }
        })
        self.assertEqual(resp.status_code, 404)

    def test_clear_db(self):
        resp = self.client.get("/clear")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("status", resp.get_json())


if __name__ == "__main__":
    unittest.main()
