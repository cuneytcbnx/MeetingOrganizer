from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meets.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    meets = Meet.query.all()
    return render_template("index.html", meets=meets)


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        baslik = request.form.get('baslik')
        konu = request.form.get('konu')
        tarih = request.form.get('tarih')
        baslangic_saati = request.form.get('baslangic_saati')
        bitis_saati = request.form.get('bitis_saati')
        katilimcilar = request.form.get('katilimcilar')

        newMeet = Meet(
            baslik=baslik,
            konu=konu,
            tarih=tarih,
            baslangic_saati=baslangic_saati,
            bitis_saati=bitis_saati,
            katilimcilar=katilimcilar,
        )
        db.session.add(newMeet)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/delete/<string:job_id>')
def deleted(job_id):
    meet = Meet.query.filter_by(id=job_id).first()
    db.session.delete(meet)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        meet = Meet.query.get(request.form.get('id'))
        print(meet)
        meet.konu = request.form['konu']
        meet.tarih = request.form['tarih']
        meet.baslangic_saati = request.form['baslangic_saati']
        meet.bitis_saati = request.form['bitis_saati']
        meet.katilimcilar = request.form['katilimcilar']
        db.session.commit()

        return redirect(url_for('index'))


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
