from application import db


class Bid(db.Model):
    __tablename__ = 'bids'

    id = db.Column(db.Integer, primary_key=True)
    bidder_name = db.Column(db.String())
    bidder_email = db.Column(db.String())
    amount = db.Column(db.Float())
    street_address = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    zip_code = db.Column(db.String())
    receipt = db.Column(db.String())

    item_id = db.Column(
        db.Integer,
        db.ForeignKey('items.id'),
        nullable=False
    )

    def __repr__(self):
        return '<id {}>'.format(self.id)
