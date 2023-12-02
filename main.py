# import os
# import azure.ai.vision as sdk

# # def process_image(image_data):
# # try:
# service_options = sdk.VisionServiceOptions(os.environ["VISION_ENDPOINT"],os.environ["VISION_KEY"])

# script_directory = os.path.dirname(os.path.realpath(__file__))

# # Specify the filename of your image (replace "your_image.jpg" with the actual filename)
# image_filename = "image.jpg"

# # Create the full path to the image file
# image_path = os.path.join(script_directory, image_filename)

# # Create a VisionSource object with the local image file
# vision_source = sdk.VisionSource(image_path)


# analysis_options = sdk.ImageAnalysisOptions()

# analysis_options.features = (
#     sdk.ImageAnalysisFeature.CAPTION |
#     sdk.ImageAnalysisFeature.TEXT
# )

# analysis_options.language = "en"

# analysis_options.gender_neutral_caption = True

# image_analyzer = sdk.ImageAnalyzer(service_options, vision_source, analysis_options)

# result = image_analyzer.analyze()

# text_output = ['hello']
# if result.reason == sdk.ImageAnalysisResultReason.ANALYZED:

#     if result.text is not None:
#         for line in result.text.lines:
#             decoded_line = ""
#             for char in line.content:
#                 if isinstance(char, bytes):
#                     decoded_line += char.decode('utf-8', errors='replace')
#                 else:
#                     decoded_line += char
#             text_output.append(decoded_line)
#         print(text_output)
#     else:
#         error_details = sdk.ImageAnalysisErrorDetails.from_result(result)
#         print(" Analysis failed.")
#         print("   Error reason: {}".format(error_details.reason))
#         print("   Error code: {}".format(error_details.error_code))
#         print("   Error message: {}".format(error_details.message))
# # except Exception as e:
# #     return [f"An error : {str(e)}"]
    
