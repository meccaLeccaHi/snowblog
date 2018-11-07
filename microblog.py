from app import app, db
from app.models import Resort, Post

# Assign relationships between database and tables
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Resort': Resort, 'Post': Post}
