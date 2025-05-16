# This is a mock implementation of a 3rd party scheduling API.
# It simulates the behavior of a scheduling service that confirms appointments.
# In a real-world scenario, this would involve making HTTP requests to the actual API.
# If you want to use a real 3rd party API, please feel free to try.

def get_available_provider(preferred_time):
    return {
        "provider_id": 101,
        "provider_name": "Dr. Smith",
        "confirmed_time": preferred_time
    }
