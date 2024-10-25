import os
import cv2
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from google.oauth2 import service_account
import google_cloud.vision as vision_helper
import google_cloud.tts as tts_helper
from libs.database import save_metadata

class MedicationScannerApp(App):
    def build(self):
        self.title = 'Medication Scanner App'
        layout = BoxLayout(orientation='vertical')

        # Image widget to show captured image
        self.image_widget = Image(source='assets/captured_image.png', size_hint=(1, 0.7))
        layout.add_widget(self.image_widget)

        # Button to capture the image with styling
        capture_button = Button(
            text="Capture Image!", 
            size_hint=(1, 0.1),
            background_color=(0.9, 0.4, 0.3, 1),  # Red color background
            color=(1, 1, 1, 1),  # White text color
            bold=True
        )
        capture_button.bind(on_press=self.capture_image)
        layout.add_widget(capture_button)

        # Button for displaying extracted text with different styling
        self.result_label = Button(
            text="Extracted Text will appear here!", 
            size_hint=(1, 0.4),
            background_color=(0.2, 0.6, 0.9, 1),  # Blue color background
            color=(0.0, 0.8, 0.0, 1),  # White text color
            bold=True
        )
        layout.add_widget(self.result_label)

        return layout

    def capture_image(self, instance):
        # Use OpenCV to capture an image from the camera
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if ret:
            img_path = 'assets/captured_image.png'
            cv2.imwrite(img_path, frame)  # Save the image
            self.image_widget.source = img_path  # Update image widget
            self.image_widget.reload()

            # Perform OCR to extract text
            extracted_text = vision_helper.perform_ocr(img_path)
            self.result_label.text = extracted_text

            # Use Text-to-Speech to read the extracted text aloud
            audio_path = 'assets/output.mp3'
            tts_helper.text_to_speech(extracted_text)

            # Save metadata (image and audio file paths)
            save_metadata(img_path, audio_path)
        else:
            self.result_label.text = "Failed to capture image."
        cap.release()

if __name__ == '__main__':
    MedicationScannerApp().run()
