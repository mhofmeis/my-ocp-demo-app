from flask import Flask, request # render_template, redirect, url_for
import pandas as pd
from tinydb import TinyDB, Query
import json

app = Flask(__name__)
db = TinyDB('db.json')
query = Query()

index_tmplt = '''
<html>
    <body>
        <form action = "/api/data" method = "POST" enctype = "multipart/form-data">
            <input type="file" name="file" />
            <input type="submit"/>
        </form>   
    </body>
</html>
'''

output_tmplt = "<html><body><pre>{}</pre></body></html>"


@app.route('/')
def index():
#    return render_template('index.html')
    return index_tmplt


@app.route('/api/data', methods=['POST'])
def retrieve_file():    
    f = request.files['file']

    if f.filename != '':
        #f.save(f.filename)
        print("Received file name: " + f.filename)
        df = pd.read_csv(f, sep=';')
        print(df.head())

    #db.insert(df.to_dict(orient='index'))
    records = df.to_dict(orient="records")
    
    for record in records:
        db.insert(record)
        print(record)
    
    return output_tmplt.format(df.to_json(orient='index', indent=2))



@app.route('/api/data', methods=['GET'])
def provide_data():
    return output_tmplt.format(db.search(query.Name == "Michael Hofmeister"))
    #return output_tmplt.format(db.all())


if __name__=="__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
