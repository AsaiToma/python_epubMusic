from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def data():
    text_list = ["aaa","bbb","ccc","ddd","eee"]
    return render_template('get_data.php', text_list=text_list)



## おまじない
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8082)