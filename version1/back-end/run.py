from API import create_back_end_api
from Database import config

app = create_back_end_api(config)

if __name__ == "__main__":
    app.run(debug=True)
