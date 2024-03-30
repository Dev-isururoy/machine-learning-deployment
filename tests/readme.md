
## Unit Tests

The `unit_tests` directory contains test scripts for unit testing individual components of the project, such as data preprocessing and model training.

- [test_data_preprocessing.py](tests/unit_tests/test_data_preprocessing.py): Unit tests for data preprocessing functions.
- [test_model_training.py](tests/unit_tests/test_model_training.py): Unit tests for model training functions.

## Integration Tests

The `integration_tests` directory contains test scripts for integration testing, which test the interactions between different components of the project.

- [test_model_evaluation.py](tests/integration_tests/test_model_evaluation.py): Integration tests for model evaluation functions.

## Running Tests

To run the tests, navigate to the project directory and use the following commands:

```bash
# Run all unit tests
python -m unittest discover -s tests/unit_tests

# Run all integration tests
python -m unittest discover -s tests/integration_tests


Dependencies to : install the required dependencies for running tests, use the following command

pip install -r requirements.txt

License : This project is licensed under the MIT License.


In this README:

- We provide an overview of the project and its directory structure.
- We describe the purpose of the `unit_tests` and `integration_tests` directories.
- We list the available test scripts and their respective functionalities.
- We provide instructions for running the tests.
- We mention the dependencies required for running the tests.
- We include licensing information for the project. 

Feel free to customize the README further to include more specific information or instructions based on your project's requirements.
