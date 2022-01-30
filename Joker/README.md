# How to use
1. Install Django 4.0.1 on your local machine
2. Clone this repo to your local machine
3. In the current directory (same as `manage.py`), start a terminal and enter command: `python manage.py runserver`. Make sure your default python version is Python3, otherwise you need to specify it explicitly: `python3 manage.py runserver`
4. In your browser, enter the following URL: [http://127.0.0.1:8000/editor/]
5. You should be able to see the full example here.

# How to modify
1. Go to [./editor/templates/index.html](./editor/templates/index.html) This is the template file for full example.

# Save and load
- Find the `note-list.json` file in the `./editor/static/editor/json/` folder. It is an example of how my server side code will generate the format of json file.
- In the `index.html` page, create a sidebar (you can adjust the width of the editor, if it looks better), display the notes' title as a list, give the title a `<a href="path"> </a>` tag, where the `path` is the value of `path` property in json file.