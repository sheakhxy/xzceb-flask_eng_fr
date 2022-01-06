from machinetranslation import translator
from flask import Flask, render_template, request
import json
import os

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    frenchtext = translator.english_to_french(textToTranslate)
    return f'Translated text to French - {(frenchtext)}'
    #return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    englishtext = translator.french_to_english(textToTranslate)
    return f'Translated text to English - {(englishtext)}'
    #return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

#if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=8080)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)
