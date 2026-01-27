# Data Engineering Bootcamp Assignment 1

## Question 1

Ran the below command to run a bash shell in a Python 3.13 container:
    docker run -it --rm --entrypoint=bash  python:3.13

Then checked the version of pip using the command:
    pip --version

## Question 2

5432 is the port exposed to the client and the container name is postgres. So the answer is postgres:5432

## Questions 3, 4, 5, 6

Created a virtual environment using the command:
uv init --python=3.13

Then installed the required packages using the command:
uv add pandas pyarrow

Then installed and ran jupyter notebook using the commands:

uv add --dev jupyter
uv run jupyter notebook

Manipulated the data as 






uv init --python=3.13

uv add pandas pyarrow