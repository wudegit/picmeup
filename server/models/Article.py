#-*-coding:utf-8-*-

from server import db
from datetime import datetime
import models

class Article(db.Model):
    __tablename__ = 'articles'
    __public__=('id','title','description','created_time','updated_time')
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text,nullable=True)
    origin = db.Column(db.String(255),nullable=True)
    file_name = db.Column(db.String(255),nullable=True)
    origin_url = db.Column(db.Text,nullable=True)
    pic_url = db.Column(db.Text,nullable=True)
    author_id = db.Column(db.Integer,nullable=True)

    created_time = db.Column(db.DateTime, default=datetime.now)
    updated_time = db.Column(db.DateTime, default=datetime.now)
    status = db.Column(db.Integer, nullable=False,default=1)
    order =  db.Column(db.Integer,nullable=True,default=0)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id'         : self.id,
            'title'         :   self.title,
            'created_time'  :   models.dump_datetime(self.created_time),
            # # This is an example how to deal with Many2Many relations
            # 'many2many'  : self.serialize_many2many
        }