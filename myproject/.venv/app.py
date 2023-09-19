from flask import Flask, render_template

# Replace 'myflaskapp' with your desired app name
app = Flask('myflaskapp')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
