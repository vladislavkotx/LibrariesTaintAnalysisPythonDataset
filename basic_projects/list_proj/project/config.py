def get_user_input():
    """Gets user input and returns it."""
    taint_var = input("Enter a value: ") # Tainted variable from user input
    return taint_var

def configure_environment():
    """Configures the environment for the application."""
    pass