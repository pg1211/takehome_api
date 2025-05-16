from subprocess import check_call

def server() -> None:
    """Run the Flask server"""
    check_call(["python", "app.py"])
