from flask import Flask, request, jsonify
import os
import azure.ai.vision as sdk
import tempfile
import requests

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
service_options = sdk.VisionServiceOptions(os.environ['VISION_ENDPOINT'], os.environ['VISION_KEY'])

def process_image(image_path):
    try:
        vision_source = sdk.VisionSource(image_path)
        # vision_source = sdk.VisionSource(url="https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png")
        # print(image_path)
        # print("VISION_ENDPOINT:", os.environ.get("VISION_ENDPOINT"))
        # print("VISION_KEY:", os.environ.get("VISION_KEY"))

        analysis_options = sdk.ImageAnalysisOptions()

        analysis_options.features = (
            sdk.ImageAnalysisFeature.CAPTION |
            sdk.ImageAnalysisFeature.TEXT
        )

        analysis_options.language = "en"
        analysis_options.gender_neutral_caption = True

        image_analyzer = sdk.ImageAnalyzer(service_options, vision_source, analysis_options)

        result = image_analyzer.analyze()
        text_output = []
        if result.reason == sdk.ImageAnalysisResultReason.ANALYZED:
            # print("Image analyzed.")
            if result.text is not None:
                for line in result.text.lines:
                    text_output.append(line.content)
            else:
                error_details = sdk.ImageAnalysisErrorDetails.from_result(result)
                print("Analysis failed.")
                print("Error reason: {}".format(error_details.reason))
                print("Error code: {}".format(error_details.error_code))
                print("Error message: {}".format(error_details.message))
        return text_output
    except Exception as e:
        print("Error processing image:", str(e))
        return jsonify({'error': 'Failed to process image'})

@app.route('/', methods=['POST'])
def upload_image():
    image_url = request.form.get('url') or request.args.get('url')
    image_file = request.files.get('file')

    if image_url:
        try:
            # Download the image from the URL
            response = requests.get(image_url)
            if response.status_code == 200:
                image_data = response.content

                # Save the byte data to a temporary file
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    temp_file.write(image_data)
                    temp_file_path = temp_file.name

                try:
                    # Process the image using the file path
                    output = process_image(temp_file_path)
                    return jsonify(output)
                finally:
                    # Remove the temporary file
                    os.remove(temp_file_path)
            else:
                return jsonify({'error': 'Failed to download image from URL'})
        except Exception as e:
            return jsonify({'error': str(e)})

    elif image_file:
        try:
            # Save the uploaded file to a temporary file
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                image_file.save(temp_file)
                temp_file_path = temp_file.name

            try:
                # Process the image using the file path
                output = process_image(temp_file_path)
                return jsonify(output)
            finally:
                # Remove the temporary file
                os.remove(temp_file_path)
        except Exception as e:
            return jsonify({'error': str(e)})

    else:
        return jsonify({'error': 'No URL or file provided'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)

