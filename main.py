from flask import Flask, render_template
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship


engine = create_engine("mysql+mysqlconnector://root:Lizuna777!@localhost/test", echo=True)
connection = engine.connect()
Base = declarative_base()


app = Flask(__name__)

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer,autoincrement=True,primary_key=True )
    name = Column(String(30) )
    age = Column(Integer)
    semester = Column(Integer)

    def __repr__(self):
        return self.name
Base.metadata.create_all(engine)

@app.route("/")
def index():
    with sessionmaker(bind=engine)() as session:
        students = session.query(Student).all()
        for student in students:
            print(student.name,student.age)
        print(students)
    return render_template("index.html", title="indexpafe", students=students)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html", data=[4394892,4244954,5939342,23942012], title="indexpafe")

if __name__ == "__main__":
    app.run(debug=True)
    