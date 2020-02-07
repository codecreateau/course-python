# C< Courses: Python

Code Create's Python course provides both fundamental exercises and projects for
all student levels. This content is primarily targetted at teaching providers,
but can later be adapted to a student view.

## Pre-requisites

Make sure you have the following installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [virtualenv](https://pypi.org/project/virtualenv/)
- [git](https://git-scm.com/)
- [VSCode](https://code.visualstudio.com/download)

## Installation

Use [git](https://git-scm.com/) to download the course files

```bash
mkdir codecreate
cd codecreate
git clone https://github.com/codecreateau/course-python.git
cd course-python
code .
```

## Usage

### Setup and start a virtual environment

For any exercises or projects, create a virtual environment by using the
following commands:

```bash
cd <project-or-exercise-name>
virtualenv venv
source venv/bin/activate
```

**For more information about why virtual environments are useful, use the**
**following link**

### Install dependencies

Once you are in your virtual environment, you can install the dependencies using
the following command:

```bash
cd <project-or-exercise-name>
pip install requirements.txt
```
