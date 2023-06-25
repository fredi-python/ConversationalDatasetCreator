from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/save_file.php', methods=['POST'])
def save_file():
    file_data = request.data.decode('utf-8')

    # Append the data to the file
    file_name = 'conversational_data.jsonl'
    file_path = '' + file_name

    with open(file_path, 'a') as file:
        file.write(file_data)
        file.write('\n')  # Add a newline after each entry for proper JSONL formatting

    return 'File saved on the server.'

if __name__ == '__main__':
    app.run()

