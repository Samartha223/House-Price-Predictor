import pandas as pd
from flask import Flask,request,render_template,redirect,url_for
import pickle
from num2words import num2words

app=Flask(__name__)

df = pd.read_csv('Bangalore_dataset.csv')

def amount_to_indian_rupee_words(amount: float, lang: str = 'en_IN') -> str:
        rupees = int(amount)
        paise = int(round((amount - rupees) * 100))
    
        words_rupees = num2words(rupees, lang=lang)
        if paise > 0:
            words_paise = num2words(paise, lang=lang)
            return f"{words_rupees} rupees and {words_paise} paise"
        else:
            return f"{words_rupees} rupees"

@app.route("/",methods=['GET','POST'])
def home():

    #location=sorted(df['location'].unique())
    locations= sorted(df['location'].unique())
    prediction=request.args.get('prediction')
    price=request.args.get('price')
    

    if request.method=='POST':
        location=request.form.get('location')
        bhk=request.form.get('bhk')
        bath=request.form.get('bath')
        sqft=request.form.get('sqft')

        input_data=pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])

        model=pickle.load(open('House.pkl','rb'))
        pred_value=model.predict(input_data)[0] *1e5
        rupees_text=amount_to_indian_rupee_words(pred_value)
        rupees_text=rupees_text.split(',')
        rupees_text=' '.join(rupees_text).title()
        price_value=round(pred_value,2)

        return redirect(url_for('home',prediction=rupees_text,price=price_value))

    return render_template('index.html', locations=locations,prediction=prediction, price=price)
    


if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
