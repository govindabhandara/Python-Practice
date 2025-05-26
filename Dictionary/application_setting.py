# Application settings
app_config = {
    "debug_mode": True,
    "max_connections": 10,
    "allowed_file_types": [".jpg", ".png", ".gif"],
    "database": {
        "host": "localhost",
        "port": 5432,
        "username": "admin"
    }
}

if app_config["debug_mode"]:
    print("Running in debug mode")
