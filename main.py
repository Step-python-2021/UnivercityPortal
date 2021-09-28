from config import app
from views.home_controller import HomeController
from views.news_controller import NewsController
from views.users_controller import UsersController
from views.faculties_controller import FacultiesController


if __name__ == '__main__':
    hc = HomeController()
    nc = NewsController()
    uc = UsersController()
    fc = FacultiesController()

    app.run(debug=True)
