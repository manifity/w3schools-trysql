# pytest + selenium + allure: web automation example

## Setup instructions (this assumes that you already have Python and pip installed)

- If you clone this repo, you can do `pip install -r requirements.txt` to install both pytest and
selenium at once. Otherwise, you can install them one by one. 


### pytest

- Install [pytest](http://doc.pytest.org/en/latest/getting-started.html) via pip or easy_install:
```
pip install -U pytest or easy_install -U pytest
```
- After installation, you can check the installed version by running:
```
pytest --version
```

### selenium webdriver

- Install [selenium](http://selenium-python.readthedocs.io/installation.html) via pip:
```
pip install -U selenium
```

### chromedriver

#### Unix

- Download tar file from [chromedriver](https://chromedriver.chromium.org/)
- Go to download location and extract the file from archive.
- Create local file with system user name and `.env` format, like `username.env`. Add your local path to this file `CHROME_PATH=/Path/to/driver` and save in `settings` directory.

#### Windows

- Download and extract zip file from [chromedriver](https://chromedriver.chromium.org/)
- Get the executable file's location and add it to your Environment Variables. Instructions on
setting the path can be found [here](http://www.computerhope.com/issues/ch000549.htm)
- Create local file with system user name and `.env` format, like `username.env`. Add your local path to this file `CHROME_PATH=/Path/to/driver` and save it in the `settings` directory.

## How to run the tests

- To run all tests inside the test directory, simply run this command:
```
pytest
```
- To run a specific test, do
```
pytest <module name> <test name>
e.g. pytest test_w3_trysql.py::test_check_city
```
- To run a test with allure report, do
```
pytest <module name> --alluredir=<directory name>
e.g. pytest test_w3_trysql.py --alluredir=reportdir
```
- To see allure report, do
```
allure serve <directory name>
e.g. allure serve reportdir
```
- It is recommended to run the tests with verbosity by invoking `-v` during the test run.

