import cv2
from flask import Flask, render_template, Response, request
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app)

class VideoCamera(object):
    def __init__(self, shirt_path, pant_path):
        self.video = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
        
        # Load shirt and pant images
        self.img_shirt = cv2.imread(shirt_path, cv2.IMREAD_UNCHANGED)
        self.img_pant = cv2.imread(pant_path, cv2.IMREAD_UNCHANGED)
        
        # Get original sizes
        self.orig_shirt_height, self.orig_shirt_width = self.img_shirt.shape[:2]
        self.orig_pant_height, self.orig_pant_width = self.img_pant.shape[:2]
        
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()
        if not ret:
            return None

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            # Shirt position and size calculation
            shirt_width = 3 * w
            shirt_height = int(shirt_width * self.orig_shirt_height / self.orig_shirt_width)
            x1s, x2s = x - w, x - w + 3 * w
            y1s, y2s = y + h, y + h + 4 * h

            # Pant position and size calculation
            pant_width = 3 * w
            pant_height = int(pant_width * self.orig_pant_height / self.orig_pant_width)
            x1p, x2p = x - w, x - w + 3 * w
            y1p, y2p = y + 5 * h, y + h * 10

            # Ensure dimensions are within the frame
            x1s, x2s = max(0, x1s), min(frame.shape[1], x2s)
            y1s, y2s = max(0, y1s), min(frame.shape[0], y2s)
            x1p, x2p = max(0, x1p), min(frame.shape[1], x2p)
            y1p, y2p = max(0, y1p), min(frame.shape[0], y2p)

            # Calculate the actual width and height for both shirt and pant
            actual_shirt_width = x2s - x1s
            actual_shirt_height = y2s - y1s

            actual_pant_width = x2p - x1p
            actual_pant_height = y2p - y1p

            # Resize and apply shirt
            if actual_shirt_width > 0 and actual_shirt_height > 0:
                shirt_resized = cv2.resize(self.img_shirt, (actual_shirt_width, actual_shirt_height))
                frame[y1s:y2s, x1s:x2s] = blend_images(frame[y1s:y2s, x1s:x2s], shirt_resized)

            # Resize and apply pant
            if actual_pant_width > 0 and actual_pant_height > 0:
                pant_resized = cv2.resize(self.img_pant, (actual_pant_width, actual_pant_height))
                frame[y1p:y2p, x1p:x2p] = blend_images(frame[y1p:y2p, x1p:x2p], pant_resized)

        # Encode frame as JPEG for streaming
        ret, jpeg = cv2.imencode('.jpg', frame)
        if not ret:
            return None

        return jpeg.tobytes()

def blend_images(background, overlay):
    # Create a mask and blend the overlay with the background
    overlay_gray = cv2.cvtColor(overlay, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(overlay_gray, 1, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    bg_part = cv2.bitwise_and(background, background, mask=mask_inv)
    overlay_part = cv2.bitwise_and(overlay, overlay, mask=mask)

    return cv2.add(bg_part, overlay_part)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        if frame:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    shirt_id = request.args.get('shirt_id', 'default_shirt_id')
    pant_id = request.args.get('pant_id', 'default_pant_id')

    shirt_path = f'media/shirts/{shirt_id}.jpg'
    pant_path = f'media/pants/{pant_id}.png'

    return Response(gen(VideoCamera(shirt_path, pant_path)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
