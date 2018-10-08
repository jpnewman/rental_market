
# Rental Market

This is a Flask based application for tracking rental viewings.

It designed to work on iOS application [Pythonista 3](http://omz-software.com/pythonista/)

## Setup Environment

### Install python 3.5 (Mac OS X)

~~~
brew install pyenv

pyenv install 3.5.0
~~~

### Create Virtual Environment (Desktop Environment)

~~~
virtualenv -p ~/.pyenv/versions/3.5.0/bin/python3.5 venv
~~~

## Activate Virtual Environment (Desktop Environment)

~~~
source venv/bin/activate
~~~

## Check python version (Desktop Environment)

~~~
python -V
~~~

## Install python requirements (Desktop Environment)

~~~bash
pip install -r requirements.txt
~~~

## Install python requirements (Pythonista) 

**TODO:**

~~~
pip install -r requirements_pythonista.txt
~~~

**NOTE:** For now, the following should packages be installed via ```pip``` command using [stash](https://github.com/ywangd/stash)

|Package|Description|Note|
|---|---|---|---|
|Flask-Scss|Adds support for scss files to Flask applications|Needs compiled scss, so not used for Pythonista|
|Flask-SQLAlchemy|Adds SQLAlchemy support to your Flask application||
|SQLAlchemy|Database Abstraction Library||
|requests|Python HTTP for Humans.||
|WTForm|WTForm is an extension to the django newforms library.||
|Flask-WTF|Simple integration of Flask and WTForms.||
|Flask-DebugToolbar|A toolbar overlay for debugging Flask applications.||
|Werkzeug|The Swiss Army knife of Python web development||
|WTForms|A flexible forms validation and rendering library for python web development.||
|blinker|Fast, simple object-to-object and broadcast signaling||

## Freeze requirements (Desktop Environment)

~~~
pip freeze > requirements.txt
~~~

## Run (Desktop Environment)

~~~bash
python run.py
~~~

~~~
./run.py
~~~

## Run (Pythonista)

Run the following script: -

~~~
run.py
~~~

## Deactivate Virtual Environment (Desktop Environment)

~~~
deactivate
~~~
