from models import Vendor
from . import bcrypt, db


def vendor_exists(email):
    vendor = Vendor.query.filter_by(email=email).first()
    if not vendor:
        return False
    return True


def add_vendor(form):
    try:
        vendor = Vendor(email=form.get("email"), password=form.get("password"))
        db.session.add(vendor)
        db.session.commit()
    except Exception as e:
        return None

    return vendor


def get_vendor_list():
    vendors = Vendor.query.all()
    return vendors


def get_vendor(vendor_id):
    vendor = Vendor.query.filter_by(id=vendor_id).first()
    return vendor
