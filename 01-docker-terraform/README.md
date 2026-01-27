# Data Engineering Bootcamp Assignment 1

## Question 1

Ran the below command to run a bash shell in a Python 3.13 container:

```bash
docker run -it --rm --entrypoint=bash  python:3.13
```

Then checked the version of pip using the command:

```bash
pip --version
```

## Question 2

5432 is the port exposed to the client and the container name is postgres. So the answer is `postgres:5432`.

## Questions 3, 4, 5, 6

Created a virtual environment using the command:

```bash
uv init --python=3.13
```

Then installed the required packages using the command:

```bash
uv add pandas pyarrow
```

Then installed and ran jupyter notebook using the commands:

```bash
uv add --dev jupyter
uv run jupyter notebook
```

Manipulated the data as per the assignment using pandas. It can be found in the `homework.py` file, which was generated from the jupyter notebook homework.ipynb.