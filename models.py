from google.appengine.ext import ndb
from google.appengine.api import urlfetch
import webapp2
import os
import jinja2
import json


class User(ndb.Model):
    name = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    college = ndb.StringProperty(required=True)
    major = ndb.StringProperty(required=True)
    home_town = ndb.StringProperty(required=True)
    major = ndb.StringProperty(required=True)
    bio = ndb.StringProperty(required=True)
    pic = ndb.StringProperty(required=True) #later use blobstore
    college_pic = ndb.StringProperty(required=True) #later use blobstore
    connect_events = ndb.StringProperty(repeated=True)
    courses = ndb.StringProperty(repeated=True) #list of courses/subjects and (un)declared major
    friends = ndb.StringProperty(repeated=True, required=False)
    organizations = ndb.StringProperty(repeated=True, required=False)

class ConnectEvent(ndb.Model):
    time = ndb.StringProperty(required=True)
    location = ndb.StringProperty(repeated=True)
    users = ndb.StringProperty(repeated=True)
    #alert_time = ndb.StringProperty(required=True)

class FeedMessage(ndb.Model):
    post_type = ndb.StringProperty(required=True)
    content = ndb.StringProperty(required=True)
    connect_event = ndb.StringProperty(required=True)
    user = ndb.StringProperty(required=True)
    #alert_time = ndb.StringProperty(required=True)

class Course(ndb.Model):
    name = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    users = ndb.StringProperty(repeated=True)

class Organization(ndb.Model):
    name = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    users = ndb.StringProperty(repeated=True)
