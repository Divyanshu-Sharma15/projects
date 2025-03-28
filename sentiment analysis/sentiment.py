from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    polarity = None
    subjectivity = None
    
    if request.method == 'POST':
        text = request.form['text']
        analysis = TextBlob(text)
        polarity = analysis.polarity
        subjectivity = analysis.subjectivity
        
        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
    
    return render_template('index.html', sentiment=sentiment, polarity=polarity, subjectivity=subjectivity)

if __name__ == '__main__':
    app.run(debug=True)
