from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted_text = ""
    decrypted_text = ""
    if request.method == 'POST':
        if 'encrypt' in request.form:
            plaintext = request.form['text']
            encrypted_text = cipher_suite.encrypt(plaintext.encode()).decode()
        elif 'decrypt' in request.form:
            encrypted_text = request.form['text']
            try:
                decrypted_text = cipher_suite.decrypt(encrypted_text.encode()).decode()
            except:
                decrypted_text = "Invalid or corrupted encrypted text!"
    
    return render_template('index.html', encrypted_text=encrypted_text, decrypted_text=decrypted_text)

if __name__ == '__main__':
    app.run(debug=True)
