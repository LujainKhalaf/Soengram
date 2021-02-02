# SOEN341
SOEN 341 Project

## Objectives / Description

The goal of this app is to allow our users to post photos and interact with others. Our users are anyone who wants to use social media to interact with others. With features such as following and commenting we allow for a lot of interaction. A user can signup/login and immediately start posting, following, and commenting.

## Features

Our instagram clone is a modern web app which gives users full functionality to post, follow, comment and more. There is an intuitive user interface from the signup, to the profile, to the feed. A full feature list is as follows:

- Post pictures with description
- Follow other users on the platform
- Comment on other users posts

## Built With

- [Python 3](https://www.python.org/)
- [PostgreSQL 13.0 or later](https://www.postgresql.org/)
- [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/)
- [Jinga 2.11.2](https://jinja.palletsprojects.com/en/2.11.x/)

## Getting Started

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
    $ venv\Scripts\activate
    ```
4. Instal all packages
    ```sh
    $ pip install -r requirements.txt
    ```
5. Setup a local PostgreSQL database
6. Copy `.env.sample`, rename to `.env` and edit the following lines
    ```
    DB_TYPE="postgresql"
    DB_HOST="localhost"
    DB_PORT="5432"
    DB_USERNAME="your_username"
    DB_PASSWORD="your_password"
    DB_DATABASE="soen-341"
    ```
7. Start application
    ```sh
    $ flask run
    ```

### Running the Tests

Run all tests with the following command in the project virtual environment.

```
$ pytest
```

## Contributing

See `CONTRIBUTING.md` detailing basic guidlines for pushing new code to the repo and a basic workflow example.

## Team

- Domenic Seccareccia [(@domsec)](https://github.com/domsec)
- Lea Lakkis [(@lea)](https://github.com/lealakkis)
- Jason Gerard [(@jason-gerard)](https://github.com/jason-gerard)
- Mahmoud Elsayed [(@mnashat)](https://github.com/mnashat)
- Fadi Albasha [(@fadi-albasha)](https://github.com/fadi-albasha)
- Lujain Khalaf [(@lujainkhalaf)](https://github.com/LujainKhalaf)
- David Lemme [(@David)](https://github.com/davrine)