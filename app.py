'''
Flask Web app to upload the resume and save it locally in the uploads folder.
'''
#importing the required libraries
import os
from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import FileField,SubmitField
from wtforms.validators import InputRequired
from werkzeug.utils import secure_filename

#initialise the app and configurations
app = Flask(__name__)
app.config['SECRET_KEY'] = "mulasaag"
app.config['UPLOAD_FOLDER'] = "uploads\\files"

ALLOWED_EXTENSIONS = {'pdf', 'docx', 'doc'}

def allowed_file(filename):
    '''
    This function checks if the file extension is allowed
    '''
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class UploadFileForm(FlaskForm):
    '''
    This class creates the form for uploading files
    '''
    file = FileField("File",validators=[InputRequired()])
    submit = SubmitField("Upload File")

#route to the home page
@app.route('/', methods = ['GET','POST'])
@app.route('/home', methods = ['GET','POST'])

def home():
    '''
    This function renders the home page to upload the file from the user
    and save it locally in the uploads folder.
    '''
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data #grabs the file from the form
        if file and allowed_file(file.filename):
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
            return "File has been successfully uploaded"
        else:
            return "File extension not allowed"
    return render_template('index.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
