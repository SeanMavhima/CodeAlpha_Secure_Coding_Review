from flask import Flask, render_template, request, jsonify
import cv2
import mediapipe as mp
import time

app = Flask(__name__)

class FaceMeshDetector():
    def __init__(self, staticMode=False, maxFaces=2, minDetectionCon=0.5, minTrackCon=0.5):
        self.staticMode = staticMode
        self.maxFaces = maxFaces
        self.minDetectionCon = minDetectionCon
        self.minTrackCon = minTrackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        # Convert minDetectionCon and minTrackCon to float as they are supposed to be
        self.faceMesh = self.mpFaceMesh.FaceMesh(
            static_image_mode=self.staticMode,
            max_num_faces=self.maxFaces,
            min_detection_confidence=self.minDetectionCon,
            min_tracking_confidence=self.minTrackCon
        )
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)

    def findFaceMesh(self, img, draw=True):
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)
        faces = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_TESSELATION,
                                        self.drawSpec, self.drawSpec)

                face =[]
                for id, lm in enumerate(faceLms.landmark):
                    #print(lm)
                    ih, iw, ic = img.shape
                    x,y = int(lm.x*iw), int(lm.y*ih)
                    #############--jrnkt
                    cv2.putText(img,str(id), (x ,y), cv2.FONT_HERSHEY_PLAIN, 0.5, (0, 255, 0), 1)
                    #print(id, x, y)
                    face.append([x,y])
                faces.append(face)
        return img, faces

# Instantiate your face mesh detector
detector = FaceMeshDetector()

# Route to handle face mesh detection when button is clicked
@app.route('/detect_face_mesh', methods=['POST'])
def detect_face_mesh():
    # Capture video or image here and perform face mesh detection
    # Example:
    # cap = cv2.VideoCapture(0)
    # success, img = cap.read()
    # img, faces = detector.findFaceMesh(img, False)
    # Your further processing goes here...
    # You can return a response if needed
    return "Face mesh detected successfully!"

# Route for rendering the HTML template
@app.route('/home')
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
