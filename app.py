from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# ===== EMAIL CONFIG =====
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "yourcompanyemail@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # Gmail App Password

def send_email(name, email, message):
    body = f"""
    New Customer Enquiry:

    Name: {name}
    Email: {email}
    Message: {message}
    """

    msg = MIMEText(body)
    msg["Subject"] = "New Enquiry - Brother's Smart Surveillance AI"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.send_message(msg)
    server.quit()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        send_email(name, email, message)

        return "Thank you! We will contact you shortly."

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
