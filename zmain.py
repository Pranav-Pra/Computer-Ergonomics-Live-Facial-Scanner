from flask import Flask, render_template, Response
from zcam import cam

app = Flask(__name__)
#Access HTML Code
@app.route('/')
def index():
    return render_template('index.html')

    '''
    Citation for code for facescan() and vid()  
    Title: How I got my OpenCV Project on a web server
    Author: Misbah Mohammed
    Date:4/17/2021
    Program Version: Python 3.8.6
    Availability: 
    https://www.youtube.com/watch?v=-4v4A550K3w
    '''  

#Accesses Face Cam
def facescan(live):
    while True:
        frame = live.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame
              + b'\r\n\r\n')
    
@app.route('/vid')
def vid():
    return Response(facescan(cam()),
        mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
