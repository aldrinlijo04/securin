from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Securin(db.Model):
    __tablename__ = 'securin'

    id = db.Column(db.Integer, primary_key=True)
    cpe_title = db.Column(db.String(255))
    cpe_23_uri = db.Column(db.String(255))
    reference_links = db.Column(db.Text)
    cpe_23_deprecation_date = db.Column(db.String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "cpe_title": self.cpe_title,
            "cpe_23_uri": self.cpe_23_uri,
            "reference_links": self.reference_links,
            "cpe_23_deprecation_date": self.cpe_23_deprecation_date
        }


