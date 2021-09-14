from config import app
from views.home_controller import HomeController


if __name__ == '__main__':
    hc = HomeController()

    app.run(debug=True)
