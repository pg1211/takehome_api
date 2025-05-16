# Take home assignment
You are building an internal API for a simple appointment booking service for a virtual dermatology clinic. 
The system should allow patients to request appointments, and behind the scenes, your API will assign the appointment to a provider using a 3rd party scheduling service.

## Goal
- Design a minimal database schema.
  - I have added a couple of tables, but you can add more if you think it is necessary.
- Implement relevant endpoints to show available appointments, book an appointment.
- Integrate with a mock third-party scheduling API.
  - I've included a mock api for you to use. You can use a real 3rd party scheduling API if you want to.

## Users
This feature will be used by clinicians or by the ops team to schedule appointments for patients.

## Submission
- Fork this github repository and check in your code.
- Create a new branch with your name and start working on the assignment.
- Once you are done, push your changes to your forked repository and share the link with me.
- Please include a screen recording or any documentation of the functionality in your README file.


## Getting started
- Fork this repository and clone it to your local machine.
- Setup/configure python3.12, poetry.
- Install packages: Run `poetry install`. This will install the required dependencies/packages and create a virtual environment.
- Find your Python interpreter: Run `poetry shell` to find your Python interpreter. It will spawn a shell within your virtual environment and should print the interpreter path to the screen.

### Activate shell
- To activate shell run `poetry shell`
- Run `poetry run server` from the command line to start the server.

## Bonus (not necessary)
Write 1-2 unit tests using pytest for the endpoint using mock for external API.
