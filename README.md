
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

|Package|Version|Description|Note|
|---|---|---|---|
|Flask-Scss|0.5|Adds support for scss files to Flask applications|Needs compiled scss, so not used for Pythonista|
|Flask-SQLAlchemy|2.2|Adds SQLAlchemy support to your Flask application||
|SQLAlchemy|1.1.6|Database Abstraction Library||
|requests|2.13.0|Python HTTP for Humans.||
|WTForm|1.0|WTForm is an extension to the django newforms library.||
|Flask-WTF|0.14.2|Simple integration of Flask and WTForms.||
|Flask-DebugToolbar|0.10.1|A toolbar overlay for debugging Flask applications.||
|Werkzeug|0.9.6|The Swiss Army knife of Python web development||
|WTForms|2.1|A flexible forms validation and rendering library for python web development.||
|blinker|1.4|Fast, simple object-to-object and broadcast signaling||

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
