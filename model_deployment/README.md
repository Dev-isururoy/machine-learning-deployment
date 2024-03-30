# Model Deployment

This directory contains files related to deploying machine learning models.

## App

The "app/" directory hosts the web application files.

- **templates/**: Directory containing HTML templates used by the web application.
  - [index.html](app/templates/index.html): HTML template for the main page of the web application.

- **static/**: Directory containing static files used by the web application, such as CSS and JavaScript files.
  - **css/**: Directory for CSS files.
    - [style.css](app/static/css/style.css): CSS file for styling the web application.
  - **js/**: Directory for JavaScript files.
    - [script.js](app/static/js/script.js): JavaScript file for client-side interactions.

- [app.py](app/app.py): Python script for running the Flask web application.

## Dockerfile

The "Dockerfile" defines the instructions to build a Docker image for running the Flask web application.

## Requirements

The [requirements.txt](requirements.txt) file lists all the Python dependencies required for the Flask web application.

## Usage

To deploy the machine learning model using Docker:

1. Make sure you have Docker installed on your system.
2. Build the Docker image using the provided Dockerfile:
3. Run the Docker container:
4. Access the web application in your browser at `http://localhost:5000`.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).


