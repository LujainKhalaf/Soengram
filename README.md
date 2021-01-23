# SOEN341
SOEN 341 Project

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