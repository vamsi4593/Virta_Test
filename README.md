# Virta_Test

Virta_Test is built to test the APIs.

## Pre-requisites

Before you begin, ensure you have met the following requirements:
- You should have a `Windows/Linux/Mac` machine
- Install latest(stable) version of python.

Setup Virta_Test in your system.

- clone the repo
```
$$$ git clone https://github.com/vamsi4593/Virta_API_Test.git
```
- download the working module
```
$$$ git checkout main
```
- configure the libraries needed
```
$ pip install pytest library
$ pip install requests library
$ pip install html-report
```
- Running Virta_Test
```
pytest -v --html=reports/test-report.html
```