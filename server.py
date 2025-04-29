from flask import Flask, render_template, request, send_file
import base64


from preprocess import classes, original_rows_len, classified_df_len
from model import predict_tariff

class_list = [key for key in classes]

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html', classes=class_list, original_rows_len=original_rows_len, classified_df_len=classified_df_len)

@app.route('/plot_img')
def plot_img():
    return send_file("./templates/graph.png", mimetype='image/png')

@app.route('/submit', methods=['POST'])
def submit():
    class_name = request.form['class_name']
    mfn_ad_val_rate = request.form['mfn_ad_val_rate']
    mfn_other_rate = request.form['mfn_other_rate']
    mfn_rate_type_code = request.form['mfn_rate_type_code']

    predict = predict_tariff(mfn_ad_val_rate, mfn_other_rate, mfn_rate_type_code, class_name)
    return f"Received: class_name={class_name}, mfn_ad_val_rate={mfn_ad_val_rate}, predict={predict}"

if __name__ == '__main__':
    app.run(debug=True)
