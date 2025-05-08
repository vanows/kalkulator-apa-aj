from flask import Flask, render_template, request

app = Flask(__name__)

def hitung_faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * hitung_faktorial(n - 1)

def hitung_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return hitung_fibonacci(n - 1) + hitung_fibonacci(n - 2)

def deret_aritmatika(a, d, n):
    if n == 1:
        return a
    else:
        return d + deret_aritmatika(a, d, n - 1)

def deret_geometri(a, r, n):
    if n == 1:
        return a
    else:
        return r * deret_geometri(a, r, n - 1)

def probabilitas(k, n):
    if n == 0:
        return 0
    return k / n

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hitung', methods=['POST'])
def hitung():
    operasi = request.form['operasi']
    if operasi == 'faktorial':
        angka = int(request.form['angka'])
        hasil = f"Hasil Faktorial dari {angka} adalah {hitung_faktorial(angka)}"
    elif operasi == 'fibonacci':
        angka = int(request.form['angka'])
        hasil = f"Bilangan Fibonacci ke-{angka} adalah {hitung_fibonacci(angka)}"
    elif operasi == 'aritmatika':
        a = int(request.form['a'])
        d = int(request.form['d'])
        n = int(request.form['n'])
        hasil = f"Suku ke-{n} dari deret aritmatika adalah {deret_aritmatika(a, d, n)}"
    elif operasi == 'geometri':
        a = int(request.form['a'])
        r = int(request.form['r'])
        n = int(request.form['n'])
        hasil = f"Suku ke-{n} dari deret geometri adalah {deret_geometri(a, r, n)}"
    elif operasi == 'probabilitas':
        k = int(request.form['k'])
        n = int(request.form['n'])
        hasil = f"Probabilitasnya adalah {probabilitas(k, n):.2f}"
    else:
        hasil = "Operasi tidak valid."
    return render_template('result.html', hasil=hasil)

if __name__ == '__main__':
    app.run(debug=True)