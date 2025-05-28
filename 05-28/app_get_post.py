from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form['username']
    else:
        name = request.args.get('username', '손님')
    return f'안녕하세요, {name}님!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10031)
