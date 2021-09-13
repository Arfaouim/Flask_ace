from app import create_app

app = create_app()

 # Admin Section 

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.models import User, Note
from app.__init__ import db

# Create admin. In this block you pass your custom admin index view to your admin area 
admin = Admin(app, 'Admin Area', template_mode='bootstrap4')      
admin.add_views(ModelView(User, db.session))
admin.add_views(ModelView(Note, db.session))

######################################################

if __name__ == "__main__":
    app.run(debug=True)