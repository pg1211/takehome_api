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
            db.engine.dispose()

    def test_health_check(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_add_provider(self):
        data = {
            "provider": {
                "name": "Dr. Jane Doe",
                "states": ["CA", "NY"],
                "insurances": ["Aetna", "Blue Cross"],
            }
        }
        resp = self.client.post("/provider", json=data)
        self.assertEqual(resp.status_code, 201)
        self.assertIn("name", resp.get_json())

    def test_add_provider_success(self):
        data = {
            "provider": {
                "name": "Dr. John Smith",
                "states": ["TX", "FL"],
                "insurances": ["Cigna", "UnitedHealthcare"],
            }
        }
        resp = self.client.post("/provider", json=data)
        self.assertEqual(resp.status_code, 201)
        resp_json = resp.get_json()
        self.assertEqual(resp_json["name"], "Dr. John Smith")
        self.assertIn("TX", resp_json["states"])
        self.assertIn("Cigna", resp_json["insurances"])

    def test_book_appointment_success(self):
        # add provider first
        self.client.post(
            "/provider",
            json={
                "provider": {
                    "name": "Dr. Jane Doe",
                    "states": ["CA"],
                    "insurances": ["Aetna"],
                }
            },
        )
        # book appointment
        resp = self.client.post(
            "/appointment",
            json={
                "patient": {
                    "name": "John Doe",
                    "email": "john@example.com",
                    "state": "CA",
                    "insurance": "Aetna",
                }
            },
        )
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(resp.get_json()["scheduled"])

    def test_book_appointment_no_provider(self):
        resp = self.client.post(
            "/appointment",
            json={
                "patient": {
                    "name": "John Doe",
                    "email": "john@example.com",
                    "state": "TX",
                    "insurance": "Nonexistent",
                }
            },
        )
        self.assertEqual(resp.status_code, 404)

    def test_list_appointments(self):
        # Add a provider and book an appointment first
        self.client.post(
            "/provider",
            json={
                "provider": {
                    "name": "Dr. Jane Doe",
                    "states": ["CA"],
                    "insurances": ["Aetna"],
                }
            },
        )
        self.client.post(
            "/appointment",
            json={
                "patient": {
                    "name": "John Doe",
                    "email": "john@example.com",
                    "state": "CA",
                    "insurance": "Aetna",
                }
            },
        )
        resp = self.client.get("/appointments")
        self.assertEqual(resp.status_code, 200)
        appointments = resp.get_json()
        self.assertIsInstance(appointments, list)
        self.assertTrue(any(a["patient"] == "John Doe" for a in appointments))

    def test_list_providers(self):
        # Add a provider first
        self.client.post(
            "/provider",
            json={
                "provider": {
                    "name": "Dr. Jane Doe",
                    "states": ["CA"],
                    "insurances": ["Aetna"],
                }
            },
        )
        resp = self.client.get("/providers")
        self.assertEqual(resp.status_code, 200)
        providers = resp.get_json()
        self.assertIsInstance(providers, list)
        self.assertTrue(any(p["name"] == "Dr. Jane Doe" for p in providers))

    def test_clear_db(self):
        resp = self.client.get("/clear")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("status", resp.get_json())


if __name__ == "__main__":
    unittest.main()
