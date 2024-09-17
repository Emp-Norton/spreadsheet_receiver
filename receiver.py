from flask import Flask

app = Flask(__name__)

@app.route('/')
def respond():
    return "<p> Ready to catch some sheet. </p>"

@app.route('/upload', methods=['POST'])
def upload():
    # Get the JSON data sent in the request
    data = request.get_json()
    if not data or 'spreadsheet' not in data:
        return jsonify({"error": "No valid JSON data provided"}), 400

    # Convert JSON stringified spreadsheet to a DataFrame
    try:
        df = pd.DataFrame(data['spreadsheet'])
    except Exception as e:
        return jsonify({"error": f"Failed to convert data to DataFrame: {str(e)}"}), 400

    # Create a PDF from the DataFrame
    pdf_io = BytesIO()
    c = canvas.Canvas(pdf_io, pagesize=letter)
    width, height = letter

    # Set up PDF document
    y_position = height - 50
    row_height = 20

    # Add DataFrame contents to PDF
    for i, (index, row) in enumerate(df.iterrows()):
        x_position = 50
        for value in row:
            c.drawString(x_position, y_position, str(value))
            x_position += 100  # Adjust spacing as needed
        y_position -= row_height
        if y_position < 50:  # Check if we need a new page
            c.showPage()
            y_position = height - 50

    c.save()

    # Save PDF to a file
    pdf_filename = 'spreadsheet.pdf'
    with open(pdf_filename, 'wb') as f:
        f.write(pdf_io.getvalue())

    return jsonify({"message": f"PDF saved as {pdf_filename}"}), 200

if __name__ == '__main__':
    app.run(debug=True)
