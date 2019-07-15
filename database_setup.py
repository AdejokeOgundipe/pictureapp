from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import sys

from sqlalchemy import Column,ForeignKey,Integer,String
#from sqlalchemy.ext.declaration import declarative_base