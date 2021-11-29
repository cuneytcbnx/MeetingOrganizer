from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meets.db'
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


class Meet(db.Model):
    __tablename__ = "meet"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    baslik = db.Column(db.String(80))
    konu = db.Column(db.Text)
    tarih = db.Column(db.Text)
    baslangic_saati = db.Column(db.Text)
    bitis_saati = db.Column(db.Text)
    katilimcilar = db.Column(db.Text)

    def __init__(self, baslik, konu, tarih, baslangic_saati, bitis_saati, katilimcilar):

        self.baslik = baslik
        self.konu = konu
        self.tarih = tarih
        self.baslangic_saati = baslangic_saati
        self.bitis_saati = bitis_saati
        self.katilimcilar = katilimcilar


if __name__ == '__main__':
    app.run()
