from flask import Blueprint, request, jsonify, render_template, send_file
import csv
import processor

backend_bp = Blueprint('backend', __name__)

@backend_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@backend_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('index.html', message='No file part')
    
    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', message='No selected file')
    
    # Process the uploaded file
    rows = []
    with file.stream as csvfile:
        csvreader = csv.reader(csvfile.read().decode('utf-8').splitlines(), delimiter=',', quotechar='"')
        for row in csvreader:
            rows.append(row)
            
    data = processor.clean_data(rows)
    grouped_data = processor.group_people_by_address(data)
    text_content = ''
    for addresses, people in sorted(grouped_data.items()):
        sorted_people = sorted(people)
        line = ','.join(sorted_people) + '\n'
        text_content += line
    sorted_text_content = '\n'.join(sorted(text_content.splitlines()))

     # Create a text file for download
    with open('grouped_data.txt', 'w') as file:
        file.write(sorted_text_content)
    file.close()
    
    
    # here we should add the grouped people for vizualisation
    return render_template('index.html', message='File uploaded successfully', grouped_data=sorted_text_content)


@backend_bp.route('/submit', methods=['POST'])
def submit_text():
    data = request.form['data']
    
    # Split the input into lines and clean up each line
    lines = [line.strip().replace('”', '') for line in data.split('\n')]
    
    # Split each line into an array
    processed_data = [line.split(',') for line in lines]
    for entry in processed_data[1:]:
        entry[1] = ', '.join(entry[1:])

    # Remove extra address components
    for entry in processed_data[1:]:
        entry[2:] = []

    data = processor.clean_data(processed_data)

    grouped_data = processor.group_people_by_address(data)
    text_content = ''
    for addresses, people in sorted(grouped_data.items()):
        sorted_people = sorted(people)
        line = ','.join(sorted_people) + '\n'
        text_content += line
    sorted_text_content = '\n'.join(sorted(text_content.splitlines()))

    # Create a text file for download
    with open('grouped_data.txt', 'w') as file:
        file.write(sorted_text_content)
    

    # Render the template with the grouped data displayed in the UI
    return render_template('index.html', message='Text submitted successfully', grouped_data=sorted_text_content)

@backend_bp.route('/download', methods=['GET'])
def download_file():
    file_handle = 'grouped_data.txt'
    return send_file(file_handle, as_attachment=True)