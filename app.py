from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
from translate_text import translate_text
import os
app = Flask(__name__)

@app.route('/extract-text', methods=['POST'])
def extract_text_route():
    try:
        # Get the uploaded image file from the POST request
        image_file = request.files['image']
       
        target_language = request.form.get("lang")
        if image_file:
            # Open the image using Pillow (PIL)
            image = Image.open(image_file)

            # Perform OCR using pytesseract
            text = pytesseract.image_to_string(image)
            if text:
                # Perform translation using your function and pass the input text
                translated_text = translate_text(text, target_language)  # Call the translation function

                # Return the translated text as a JSON response with the "Content-Type" header set to application/json
                return jsonify({"translated_text": translated_text}), 200, {'Content-Type': 'application/json'}
            else:
                return jsonify({"error": "No text provided."}), 400
        else:
            return jsonify({'error': 'No image file uploaded'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)