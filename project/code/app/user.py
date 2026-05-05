import logging
import os

# Set up absolute path for the log file in the same directory as this script
log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app.log')

logging.basicConfig(
    filename=log_path, 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def register(username, password):
    logging.info(f"Register attempt for username: '{username}'")
    if username == "" or password == "":
        logging.warning("Registration failed: Empty username or password")
        return False
    logging.info("Registration successful")
    return True

def login(username, password):
    logging.info(f"Login attempt for username: '{username}'")
    if username == "admin" and password == "1234":
        logging.info("Login successful")
        return True
    logging.warning("Login failed: Invalid credentials")
    return False

def update_profile(name):
    logging.info(f"Profile update attempt for name: '{name}'")
    if len(name) < 2:
        logging.warning("Profile update failed: Name too short")
        return False
    logging.info("Profile update successful")
    return True

if __name__ == "__main__":
    # Test the functions so we can see the output and populate the log file
    print(f"Running user.py! Logs will be saved to: {log_path}")
    
    register("john", "1234")
    login("admin", "1234")
    login("admin", "wrong")
    update_profile("a")
    
    print("Execution finished. Open app.log to see the logs.")