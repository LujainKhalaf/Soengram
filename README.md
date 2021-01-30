# SOEN341
SOEN 341 Project

## Features

Our instagram clone is a modern web app which gives users full functionality to post, follow, comment and more. There is an intuitive user interface from the signup, to the profile, to the feed. A full feature list is as follows:

- Post pictures with description
- Follow other users on the platform
- Comment on other users posts

## Getting Started

### Requirements

- [Python 3](https://www.python.org/)
- [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/)
- [PostgreSQL >= 13.0](https://www.postgresql.org/)
- [Jinga 2.11.2](https://jinja.palletsprojects.com/en/2.11.x/)

### Setup

1. Make sure all the requirements mentioned above are installed
2. Clone the repository 
    ```sh
    $ git clone https://github.com/LujainKhalaf/SOEN341.git
    ```
3. Create a virtualenv and activate it
    ```sh
    $ cd SOEN341

    # Windows
    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat
    ```
4. Instal all packages
    ```sh
    $ pip install -r requirements.txt
    ```
5. Setup a local PostgreSQL database
6. Copy `.env.sample`, rename to `.env` and change any values as needed.
7. Start application
    ```sh
    $ flask run
    ```

## Team

- Domenic Seccareccia [(@domsec)](https://github.com/domsec)
- Lea Lakkis [(@lea)](https://github.com/lealakkis)
- Jason Gerard [(@jason-gerard)](https://github.com/jason-gerard)
- Mahmoud Elsayed [(@mnashat)](https://github.com/mnashat)
- Fadi Albasha [(@fadi-albasha)](https://github.com/fadi-albasha)