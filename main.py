from flask import Flask, request, jsonify
import columner, playfair, railfence, hill, vernam
import string

app = Flask(__name__)

def caesar_encrypt(text, shift):
   alphabet = string.ascii_lowercase
   shifted_alphabet = alphabet[shift:] + alphabet[:shift]
   table = str.maketrans(alphabet, shifted_alphabet)
   return text.translate(table)

def caesar_decrypt(text, shift):
   return caesar_encrypt(text, -shift)

@app.route('/encrypt/caesar', methods=['POST'])
def encrypt_caeser():
   data = request.get_json()
   text = data['text']
   shift = data['shift']
   encrypted_text = caesar_encrypt(text, shift)
   return jsonify({'encrypted_text': encrypted_text})

@app.route('/decrypt/caesar', methods=['POST'])
def decrypt_caeser():
   data = request.get_json()
   text = data['text']
   shift = data['shift']
   decrypted_text = caesar_decrypt(text, shift)
   return jsonify({'decrypted_text': decrypted_text})

@app.route('/encrypt/rowcolumn' , methods=['POST'])
def encrypt_rowcolumn():
   data = request.get_json()
   text = data['text']
   key = data['key']
   cipher = columner.columnarEncrypt(text, key)
   return jsonify({'encrypted_text': cipher})

@app.route('/decrypt/rowcolumn' , methods=['POST'])
def decrypt_rowcolumn():
   data = request.get_json()
   text = data['text']
   key = data['key']
   plain = columner.columnarDecrypt(text, key)
   return jsonify({'decrypted_text': plain})

@app.route('/encrypt/playfair' , methods=['POST'])
def encrypt_playfair():
   data = request.get_json()
   text = data['text']
   key = data['key']
   cipher = playfair.playfaireEncrypt(text, key)
   return jsonify({'encrypted_text': cipher})

@app.route('/decrypt/playfair' , methods=['POST'])
def decrypt_playfair():
   data = request.get_json()
   text = data['text']
   key = data['key']
   plain = playfair.playfaireEncrypt(text, key)
   return jsonify({'decrypted_text': plain})

@app.route('/encrypt/railfence' , methods=['POST'])
def encrypt_railfence():
   data = request.get_json()
   text = data['text']
   key = data['key']
   cipher = railfence.railfenceEncrypt(text, key)
   return jsonify({'encrypted_text': cipher})

@app.route('/decrypt/railfence' , methods=['POST'])
def decrypt_railfence():
   data = request.get_json()
   text = data['text']
   key = data['key']
   plain = railfence.railfenceDecrypt(text, key)
   return jsonify({'decrypted_text': plain})

@app.route('/encrypt/hill' , methods=['POST'])
def encrypt_hill():
   data = request.get_json()
   text = data['text']
   key = data['key']
   cipher = hill.ecnryptHillCipher(text, key)
   return jsonify({'encrypted_text': cipher})

@app.route('/decrypt/hill' , methods=['POST'])
def decrypt_hill():
   data = request.get_json()
   text = data['text']
   key = data['key']
   plain = hill.decryptHillCipher(text, key)
   return jsonify({'encrypted_text': plain})


@app.route('/encrypt/vernam' , methods=['POST'])
def encrypt_vernam():
   data = request.get_json()
   text = data['text']
   key = data['key']
   cipher = vernam.encryptVernam(text, key)
   return jsonify({'encrypted_text': cipher})

@app.route('/decrypt/vernam' , methods=['POST'])
def decrypt_vernam():
   data = request.get_json()
   text = data['text']
   key = data['key']
   plain = vernam.decryptVernam(text, key)
   return jsonify({'decrypted_text': plain})


if __name__ == '__main__':
   app.run(debug=True)
