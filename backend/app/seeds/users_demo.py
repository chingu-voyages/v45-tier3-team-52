from app.models import db, User, environment, SCHEMA
from sqlalchemy import text


def seed_users():
    users = [{
        "first_name": "Cassey",
        "last_name": "Antuk",
        "email": "cantuk0@harvard.edu",
        "password": "zF8*wiaMl"
    }, {
        "first_name": "Alli",
        "last_name": "Voules",
        "email": "avoules1@ebay.com",
        "password": "cI9\\DfEsNZp"
    }, {
        "first_name": "Melisandra",
        "last_name": "Kalderon",
        "email": "mkalderon2@ameblo.jp",
        "password": "zO5`c$Ks6KmViB"
    }, {
        "first_name": "Romy",
        "last_name": "Raitt",
        "email": "rraitt3@gnu.org",
        "password": "sU6_jyQ\\l"
    }, {
        "first_name": "Dulsea",
        "last_name": "Kither",
        "email": "dkither4@google.co.uk",
        "password": "tK5>vq4q"
    }, {
        "first_name": "Dory",
        "last_name": "Brimilcombe",
        "email": "dbrimilcombe5@google.com.br",
        "password": "jG7!8)\"t%"
    }, {
        "first_name": "Ladonna",
        "last_name": "Parfitt",
        "email": "lparfitt6@sogou.com",
        "password": "bA5%rml1'jL(AY"
    }, {
        "first_name": "Petey",
        "last_name": "Danne",
        "email": "pdanne7@t.co",
        "password": "rX3|c9Jm6wQ0~"
    }, {
        "first_name": "Henrietta",
        "last_name": "Welfare",
        "email": "hwelfare8@yahoo.co.jp",
        "password": "eI3{r{0GzvKhF"
    }, {
        "first_name": "Ronald",
        "last_name": "Schulkins",
        "email": "rschulkins9@admin.ch",
        "password": "pO3!3\\QR2C/je"
    }, {
        "first_name": "Alonzo",
        "last_name": "Stuchberry",
        "email": "astuchberrya@macromedia.com",
        "password": "wI7/DK+yr?1`j"
    }, {
        "first_name": "Barbabas",
        "last_name": "Dany",
        "email": "bdanyb@engadget.com",
        "password": "eS5}E2B}S#{PBtv"
    }, {
        "first_name": "Enriqueta",
        "last_name": "Trotman",
        "email": "etrotmanc@latimes.com",
        "password": "wF0>ND36J@"
    }, {
        "first_name": "Flo",
        "last_name": "Placidi",
        "email": "fplacidid@dyndns.org",
        "password": "nL9'JK%q8_5"
    }, {
        "first_name": "Jorie",
        "last_name": "Cadwell",
        "email": "jcadwelle@europa.eu",
        "password": "nL5=@n7UGLAR/"
    }, {
        "first_name": "Kial",
        "last_name": "Jost",
        "email": "kjostf@wordpress.org",
        "password": "eE4?gql9I\\9"
    }, {
        "first_name": "Jorrie",
        "last_name": "Jessett",
        "email": "jjessettg@netvibes.com",
        "password": "oI7%bO~k?v\"KI!"
    }, {
        "first_name": "Engelbert",
        "last_name": "Bagwell",
        "email": "ebagwellh@utexas.edu",
        "password": "nL5=17!2t?nG*"
    }, {
        "first_name": "Kristofor",
        "last_name": "Bodell",
        "email": "kbodelli@java.com",
        "password": "xG1~>y&7C1h,"
    }, {
        "first_name": "Bogey",
        "last_name": "Kippen",
        "email": "bkippenj@msu.edu",
        "password": "oZ8?qRs~0_JFP3"
    }]
    db.session.add_all([User(**user)for user in users])
    db.session.commit()


def undo_users():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
