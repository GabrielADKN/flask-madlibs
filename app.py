from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from random import choice, randint, sample
from stories import Story

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route('/story')
def home():
    """Show story page"""
    # place = request.args.get('place')
    # noun = request.args.get('noun')
    # verb = request.args.get('verb')
    # adjective = request.args.get('adjective')
    # plural_noun = request.args.get('plural')
    
    new_story = story.generate(request.args)
    return render_template('story.html', story=new_story)

@app.route('/')
def show_story():
    """Show home page"""
    return render_template('form.html', prompts=story.prompts)