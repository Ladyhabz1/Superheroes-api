from app import app, db
from models import Hero, Power, HeroPower

with app.app_context():
    db.create_all()

    hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    power1 = Power(name="flight", description="gives the wielder the ability to fly")
    
    db.session.add(hero1)
    db.session.add(power1)
    db.session.commit()

    hero_power1 = HeroPower(strength="Strong", hero_id=hero1.id, power_id=power1.id)
    db.session.add(hero_power1)
    db.session.commit()

print("Database seeded!")
