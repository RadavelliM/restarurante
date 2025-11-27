from app import app_mount

app = app_mount.create_app()

if __name__ == "__main__":
    app.run(debug=True)