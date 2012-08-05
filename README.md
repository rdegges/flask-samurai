# flask-samurai

[![Build Status](https://secure.travis-ci.org/rdegges/flask-samurai.png?branch=master)](http://travis-ci.org/rdegges/flask-samurai)

Easily create Heroku addons in Flask.


## Audience

So, you use [Heroku](http://www.heroku.com/) to host your Flask apps. You like
the [addons](http://addons.heroku.com/), and you feel good, but your favorite
(API / service / tool / whatever) doesn't yet have an addon, and that makes you
upset.

You: "I thought the cloud was supposed to have *everything*! (grumble)"
You: "I know! I'll make my own addon! I'll even get rich in the process!"

So you google "How can I create a Heroku addon?" and find the official
[docs](https://addons.heroku.com/provider), but you're intimidated.

> You: "There's too much stuff to do. I give up. (grumble)"
> You: "I hate *the cloud* :("

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
