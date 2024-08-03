from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML form template
form_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Product Enquiry Form</title>
</head>
<body>
    <h1>Product Enquiry Form</h1>
    <form action="/submit" method="post">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email"><br><br>
        <label for="product">Product:</label><br>
        <input type="text" id="product" name="product"><br><br>
        <label for="message">Message:</label><br>
        <textarea id="message" name="message"></textarea><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
'''

# Route to display the form
@app.route('/')
def form():
    return render_template_string(form_template)

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    product = request.form.get('product')
    message = request.form.get('message')

    # Here, you can process the form data as needed
    # For now, we'll just return a simple response
    return f'''
    <h1>Form Submitted</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Product:</strong> {product}</p>
    <p><strong>Message:</strong> {message}</p>
    '''

if __name__ == '__main__':
    app.run(debug=True)
