# flask-samurai

[![Build Status](https://secure.travis-ci.org/rdegges/flask-samurai.png?branch=master)](http://travis-ci.org/rdegges/flask-samurai)

Easily create Heroku addons in Flask.


## Meta

* author: Randall Degges
* email:  rdegges@gmail.com
* status: maintained, in development


## Audience

So, you use [Heroku](http://www.heroku.com/) to host your Flask apps. You like
the [addons](http://addons.heroku.com/), and you feel good, but your favorite
(API / service / tool / whatever) doesn't yet have an addon, and that makes you
upset.

- You: "I thought the cloud was supposed to have *everything*! (grumble)"
- You: "I know! I'll make my own addon! I'll even get rich in the process!"

So you google "How can I create a Heroku addon?" and find the official
[docs](https://addons.heroku.com/provider), but you're intimidated.

- You: "There's too much stuff to do. I give up. (grumble)"
- You: "I hate *the cloud* :("

**Don't feel bad! Stop whining!**

I've got you covered.


## Purpose

`flask-samurai` basically makes building Heroku addons in Flask easier than it
already is, and probably easier than it even should be. If you've ever wanted
to make a Heroku addon, but didn't feel like doing a lot of work,
`flask-samurai` is probably just the thing you need.

Among other things, `flask-samurai` will:

- Handle all Heroku API call authentication.
- Run local tests against your Heroku API calls to make sure you didn't fuck
  anything up.
- Make adding / removing / changing Heroku addon users insanely easy.


## Installation

From the command line, run `pip install -U flask-samurai`. If you don't have
`pip` installed, and you're on Ubuntu (or Debian), try running `sudo apt-get -y
install python-pip` first.


Next, you need to add two settings to your Flask configuration:

``` python
# flask-samurai settings:
SAMURAI_USERNAME = 'myaddonname'
SAMURAI_PASSWORD = 'somelongpassword'
```

Those two settings should be identical to what you've defined in your
`addon-manifest.json` file that Heroku requires you to generate. If you have no
idea what the hell I'm talking about, [read
this](https://addons.heroku.com/provider/resources/technical/build/getting-started)..

If you don't know how to configure your Flask app, you should probably [read
this](http://flask.pocoo.org/docs/config/).


## Usage

Right now, there's only a single decorator to help you do stuff: `heroku`. This
decorator basically lets you wrap a Flask view, and ensures that all incoming
HTTP requests are coming from Heroku directly.

To use it, do the following:

``` python
from flask import Flask
from samurai.decorators import Heroku

app = Flask(__name__)
app.config.from_pyfile('settings.py')

# ...

@app.route('/heroku/blah')
@heroku
def blah():
    """This view will return a 401 if the request is NOT originated by Heroku."""
    return 'hi'
```

Make sure that the `@heroku` decorator goes beneath the `@app` decorator, as
order matters.
