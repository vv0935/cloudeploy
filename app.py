from flask import Flask,render_template

app = Flask(__name__)

jobs=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi, India',

  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
    'salary':'Rs. 12,00,000'
  }
]
@app.route("/")
def hello():
  return render_template('home.html',JOBS=jobs,company_name='Jovian')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
