from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for the About page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the Skills page
@app.route('/skills')
def skills():
    return render_template('skills.html')

# Route for the Goals page
@app.route('/goals')
def goals():
    return render_template('goals.html')

# Route for the Partners page
@app.route('/partners')
def partners():
    return render_template('partners.html')

# Route for the Work (portfolio) page
@app.route('/work')
def work():
    return render_template('work.html')

# Route for the Contact page with form submission
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data (name, email, message)
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Process the form data here (e.g., send an email or store in a database)
        print(f"Received message from {name} ({email}): {message}")
        
        # Redirect to a thank-you page or back to contact with a success message
        return redirect('/contact?success=1')
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
