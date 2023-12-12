from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# Load your emotion detection model here
# Example:
# emotion_model = load_emotion_detection_model()

cap = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = cap.read()  # Read frame from webcam

        if not success:
            break
        else:
            # Process the frame using OpenCV and your emotion detection model
            # Example:
            # result_frame = detect_emotion(frame)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
