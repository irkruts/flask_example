from flask import Flask, render_template
from application.services import (
    create_bd,
    show_all_items,
    show_some_from_bd,
    delete_user,
    update_user,
)
from application.services import create_new_user

app = Flask("My site")


@app.route("/")
def hello():
    return "Hello, world!"


@app.route("/create-user/")
def new_users():
    create_bd.bd_creator()
    list_of_users = create_new_user()
    return render_template(
        "create_user.html", list_of_users=list_of_users, title="list_of_users"
    )


@app.route("/delete-user/<int:user_id>/")
def delete_user_from_bd(user_id):
    result = delete_user(user_id)
    return render_template("delete_user.html", rest_list=result, title="New List")
    # return f"You deleted user by id. The rest user list is {delete_user(user_id)}"


@app.route("/update-user/<int:user_id>")
def update_user_from_bd(user_id):
    result = update_user(user_id)
    return render_template("update_user_list.html", result=result, title="Updated List")


@app.route("/show-all/")
def show_all_bd():
    result = show_all_items()
    return render_template("show_all.html", result=result, title="Show All")


@app.route("/show-all/<int:user_id>/")
def show_by_id(user_id):
    result = show_some_from_bd(user_id)
    return render_template("show_by_id.html", result=result, title="Show By Id")


if __name__ == "__main__":
    app.run()
