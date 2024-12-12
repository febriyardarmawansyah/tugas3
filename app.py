from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Halaman utama (Home)
@app.route('/')
def home():
    return render_template('home.html')

# Halaman About
@app.route('/about')
def about():
    return render_template('about.html')

# Halaman Contact
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Proses data yang diterima (misalnya kirim email, simpan ke database, dll)
        print(f"Message from {name} ({email}): {message}")
        # Redirect ke halaman yang sama setelah form disubmit
        return redirect(url_for('contact'))
    return render_template('contact.html')

# Halaman Products
@app.route('/products')
def products():
    return render_template('products.html')

if __name__ == '__main__':
    app.run(debug=True)
