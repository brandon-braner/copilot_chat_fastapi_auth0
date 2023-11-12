# My FastAPI App

This is a FastAPI application that uses Auth0 for user authentication.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python 3.6+ installed on your machine. You can download it from [here](https://www.python.org/downloads/).

### Installing

1. Clone the repository
```
git clone https://github.com/yourusername/my-fastapi-app.git
```

2. Change the directory
```
cd my-fastapi-app
```

3. Install the requirements
```
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and update the following variables with your Auth0 details:
```
AUTH0_DOMAIN=your_auth0_domain
AUTH0_CLIENT_ID=your_auth0_client_id
AUTH0_CLIENT_SECRET=your_auth0_client_secret
```

5. Run the application
```
uvicorn app.main:app --reload
```

The application will be available at `http://localhost:8000`.

## Running the tests

You can run the tests using the following command:

```
pytest
```

## Built With

* [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
* [Auth0](https://auth0.com/) - User authentication

## Authors

* **Your Name** - *Initial work* - [YourUsername](https://github.com/yourusername)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc