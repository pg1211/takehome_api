# Documentation on My Implementation

In this repo, I have built a basic derm clinic backend platform. Patient entries are booked with the correct provider based on their location and insurance information. Currently, `time`, `appointment_id` and `scheduled` are hardcoded based on the `schedule_with_provider` function.

## Schema Layout

### Models

#### Provider
- `id`: Integer, primary key
- `name`: String, required
- `states`: Many-to-many with `State` (licensed states)
- `insurances`: Many-to-many with `Insurance` (accepted insurances)

#### State
- `code`: String(2), primary key (e.g., "CA", "NY")

#### Insurance
- `name`: String, primary key (e.g., "Aetna")

Creating classes for State and Insurance will allow for easier scalability in the future if new attributes are required.

#### Patient
- `id`: Integer, primary key
- `name`: String, required
- `email`: String, required
- `state`: String(2), required
- `insurance`: String, required

#### Appointment
- `id`: Integer, primary key
- `patient`: String, required
- `scheduled`: Boolean
- `appointment_id`: String
- `provider`: String
- `time`: String

#### Association Tables
- `provider_states`: Links providers to states (`provider_id`, `state`)
- `provider_insurances`: Links providers to insurances (`provider_id`, `insurance`)

---

## Routes Layout

| Route                | Method | Description                                 | Input/Output Example                |
|----------------------|--------|---------------------------------------------|-------------------------------------|
| `/`                  | GET    | Health check                                | 200 OK                             |
| `/appointment`       | POST   | Book an appointment                        | See below                          |
| `/appointments`      | GET    | List all appointments                      | List of appointments               |
| `/provider`          | POST   | Add a new provider                         | See below                          |
| `/providers`         | GET    | List all providers                         | List of providers                  |
| `/clear`             | GET    | Clear all data from the database           | Status message                     |

### Book Appointment

When booking an appointment, there are three potential responses:
- Missing patient info (400)
- No matching provider (404)
- Appointment booked! (201)

---

## General Testing Layout

- **Manual Testing:**  
  Use tools like Postman or `curl` to hit the endpoints with example payloads as shown above.
- **Unit Tests:**  
  Place test files in the `tests/` directory.  
  Use Flask's test client to simulate requests and assert responses.
- **Database Reset:**  
  Use the `/clear` endpoint to reset the database between tests.
- **Seeding Data:**  
  Before running tests, ensure the database is seeded with all 50 states and any required insurances/providers.

---

## Notes

- I added `flake8` for linting and am using `black` for formatting
- The provider matching logic assigns a patient to a provider licensed in the patient's state and accepting their insurance.
- The `/clear` endpoint is useful for resetting the database during development and testing.

---

## Original Instructions

### 1. **POST /appointment**
Create an API endpoint to book an appointment.
**Input** (JSON):
```json
{
  "patient": {
    "name": "John Doe",
    "email": "john@example.com",
    "state": "CT",
    "insurance": "Aetna"
  }
}
```

### 2. **Provider Matching Logic**
Assign the patient to a provider that:
- Is licensed in the **same state** as the patient
- Accepts the patient’s **insurance**

### 3. **Scheduling Simulation**
Call a mocked external service to simulate appointment scheduling.

### 4. **Output**
```json
{
  "patient": "John Doe",
  "scheduled": true,
  "appointment_id": "apt_1234",
  "provider": "Dr. Jane Doe",
  "time": "2023-10-01T10:00:00Z"
}
```

---

## Users
This feature will be used by clinicians or by the ops team to schedule appointments for patients.

## Submission
- Fork this github repository and check in your code.
- Create a new branch with your name and start working on the assignment.
- Once you are done, push your changes to your forked repository and share the link with me.
- Please include any documentation of your implementation in your README file.
