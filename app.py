from flask import Flask, render_template, url_for, flash, redirect, request

from user_models import create_user_table, insert_user, find_user_by_identity, get_user
import sqlite3


app = Flask(__name__)
app.secret_key = "Y3cFAcSbRi"

my_user = {
    "name": "admin",
    "phone": "25392008",
    "check_in": "2021-09-01",
    "check_out": "2021-09-02",
    "identity": "admin",
    "guests": 1
}

with app.app_context():
   create_user_table()  # Create the user table if it doesn't exist

   print("Checking user existence...")
   user_exist = get_user(my_user["identity"], my_user["name"])
   print("User exists:", user_exist)

   if not user_exist:
      print("Inserting new user...")
      insert_user(my_user["name"], my_user["phone"], my_user["check_in"],
                  my_user["check_out"], my_user["identity"], my_user["guests"])
      print("User inserted.")
   else:
      print("User already exists.")


@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/reservation", methods=["GET", "POST"])
def reservation_page():
    if request.method == "POST":
        # Get form data
        name = request.form["name"]
        phone = request.form["phone"]
        check_in = request.form["in"]
        check_out = request.form["out"]
        identity = request.form["id"]
        guests = request.form["guests"]

        # Save the user data to the database
        insert_user(name, phone, check_in, check_out, identity, guests)
        flash('Database Updated')  # Flash a success message
        return redirect(url_for("home_page"))  # Redirect to another page or the same page

    return render_template("reservation.html")


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/services")
def services_page():
    return render_template("services.html")


@app.route("/news")
def news_page():
    return render_template("news.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True)
