# This is a mock implementation of a 3rd party scheduling API.
# It simulates the behavior of a scheduling service that confirms appointments.
# In a real-world scenario, this would involve making HTTP requests to the actual API.
# If you want to use a real 3rd party API, please feel free to try.

def schedule_with_provider(provider_name, patient_name):
    return {
        "scheduled": True,
        "appointment_id": "12345",
        "provider": provider_name,
        "time": "2023-10-01T10:00:00Z",
        "patient": patient_name,
    }

