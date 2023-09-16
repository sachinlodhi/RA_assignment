import glob
from flask import Flask, render_template, request, render_template, Response,flash, redirect, url_for,send_from_directory, session, send_file
from werkzeug.utils import secure_filename
from utils import utility
import os
import threading
import pandas as pd
app = Flask(__name__)
app.debug = True
app.secret_key = "testing key"
# Directory to store the uploaded files
UPLOAD_DIR = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_DIR

# If directory does not exists make one
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

try:
    with open("status.txt", "r+") as file:
        file.truncate(0)
except:
    pass

read_func ={
    ".csv" : pd.read_csv,
    ".xls" : pd.read_excel,
    "xlsx" : pd.read_excel,
}

#extension validation for the uploaded file
ALLOWED_EXTENSIONS = {'xls', 'csv', "xlsx"}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# homepage
@app.route('/')
def index():
    return render_template('upload.html')
df = pd.DataFrame()

# file upload page and validation
@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    global df
    print("in upload")
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            print(request.url)
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            print(request.url)
            return redirect("/")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            col_lis = utility.load_file("./"+UPLOAD_DIR+"/"+filename)
            session["col_list"] = col_lis # storing data in session variable
            session["file_path"] = "./"+UPLOAD_DIR+"/"+filename
            df = read_func[filename[-4:]](session["file_path"])
            # print(type(col_lis))
            # print(col_lis)
            return redirect(url_for("show_file_content"))
            # return redirect(url_for('download_file', name=filename))
    return render_template('upload.html')

# function for the displaying columns name

@app.route('/extracted_data')
def show_file_content():
    global df
    col_list = session.get('col_list', [])# extracting the data from session variable
    print(f"stored path is : {session.get('file_path')}")
    # start mapping
    # df = pd.read_csv(session.get("file_path"))
    # df_info = df.info()
    # print(df_info)
    utility.mapping(session.get('file_path'))
    return render_template('file_content.html', content=col_list)

# to show full table
@app.route("/view_table", methods = ["GET", "POST"])
def show_table():
    global df
    return render_template("index.html", dataframe = df)
# function for downloading the mapped file(if user press download mapped file button)
@app.route('/download_mapping',methods=['POST'])
def download_file():
    file_path = session.get('file_path')
    _, file_extension = os.path.splitext(file_path)
    file_path= _ +"_mapping" + file_extension
    print(file_path)
    return send_file(file_path, as_attachment=True, download_name="mapping"+file_extension)

@app.route("/freqDstr")
@app.route("/scatterPlt")
@app.route("/ordCorrHM")
@app.route("/catCorrHM")
@app.route("/impactTrend")
def show_graphs():
    graph_lis = []
    if request.url.endswith('/freqDstr'):
        graph_lis = glob.glob("static/graphs/frequency_graphs/*.svg")

    elif request.url.endswith('/scatterPlt'):
        graph_lis = glob.glob("static/graphs/scatter_graphs/*.svg")

    elif request.url.endswith('/impactTrend'):
        graph_lis = glob.glob("static/graphs/impact/*.svg")

    elif request.url.endswith('/ordCorrHM'):

        graph_lis = glob.glob("static/graphs/heatmaps/ordinal.svg")

    elif request.url.endswith('/catCorrHM'):
        graph_lis = glob.glob("static/graphs/heatmaps/*.svg")
        graph_lis = [i for i in graph_lis if "ordinal" not in i]
    return render_template("display_graphs.html",image_urls = graph_lis)


@app.route('/start_visualizing', methods=['POST', "GET"])
def visualize():
    t1 = threading.Thread(target=utility.begin, args=(session.get("file_path"),), daemon=True  )
    t1.start()
    # return render_template('links.html')
    # print(f"Session path visualization : {session.get('file_path')}")
    return render_template("loading.html")
@app.route("/check_process_status")
def check_status():
    print("Checking statusssss")
    with open('status.txt', 'r+') as file:
        status = file.read()
        print("Status is", status)
        if status:
            file.truncate(0)
    return status

@app.route("/results")
def result():
    return render_template("links.html")
if __name__ == '__main__':
    app.run()

# main()

