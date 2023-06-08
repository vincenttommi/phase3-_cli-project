from datetime import datetime
from sqlalchemy import Column, Date, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///fitness.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    email = Column(String(50))
    password = Column(String(70))
    enrolled_date = Column(Date)
    guidelines = relationship("Guidelines", back_populates="user", cascade="all, delete-orphan")
    exercises = relationship("Exercise", back_populates="user", cascade="all, delete-orphan")
    diets = relationship("Diet", back_populates="user", cascade="all, delete-orphan")
    instructors = relationship("Instructor", back_populates="user", cascade="all, delete-orphan")
    admins = relationship("Admin", back_populates="user", cascade="all, delete-orphan")


class Guidelines(Base):
    __tablename__ = 'guidelines'
    id = Column(Integer, primary_key=True)
    day_of_week = Column(String)
    exercise_details = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="guidelines")


class Exercise(Base):
    __tablename__ = 'exercises'
    id = Column(Integer, primary_key=True)
    exercise_name = Column(String)
    description = Column(String)
    instructions = Column(String)
    exercise_time = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="exercises")


class Diet(Base):
    __tablename__ = 'diets'
    id = Column(Integer, primary_key=True)
    day_of_week = Column(String)
    instruction = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="diets")


class Instructor(Base):
    __tablename__ = 'instructors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    specialization = Column(String)
    password = Column(String)
    experience = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="instructors")


class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    logged_date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="admins")


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


if __name__ == '__main__':
    # CLI application that generates prompts
    while True:
        print("1. Create User")
        print("2. Assign Instructor to User")
        print("3. Add Exercise for User")
        print("4. Update Exercise for User")
        print("5. Generate Report for User")
        print("6. Add Diet for User")
        print("7. Update Diet for User")
        print("8. Delete Diet for User")
        print("9. Provide Guidelines to User")
        print("10. Add User by Admin")
        print("11. Update User by Admin")
        print("12. Delete User by Admin")
        print("13. Add Instructor by Admin")
        print("14. Update Instructor by Admin")
        print("15. Delete Instructor by Admin")
        print("16. Add Guidelines by Admin")
        print("17. Update Guidelines by Admin")
        print("18. Delete Guidelines by Admin")
        print("19. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Creating a user
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            password = input("Enter user password: ")
            enrolled_date = datetime.now().date()

            user = User(
                name=name,
                email=email,
                password=password,
                enrolled_date=enrolled_date
            )
            session.add(user)
            session.commit()
            print("User created successfully!")

        elif choice == '2':
            # Assigning an Instructor to a user
            pass
# assiging a user exercise
        elif choice == '3':
            user_id = input("Enter User ID: ")
            exercise_name = input("Enter exercise name: ")
            description = input("Enter exercise description: ")
            instructions = input("Enter exercise instructions: ")
            exercise_time = input("Enter exercise time: ")
            user = session.query(User).filter_by(id=user_id).first()

            if user:
                exercise = Exercise(
                    exercise_name=exercise_name,
                    description=description,
                    instructions=instructions,
                    exercise_time=exercise_time,
                    user=user
                )
                session.add(exercise)
                session.commit()
                print("Exercise added for user successfully!")
            else:
                print("User not found!")
            
            # updating exercises

        elif choice == '4':
            exercise_id = input("Enter Exercise ID: ")
            exercise = session.query(Exercise).filter_by(id=exercise_id).first()

            if exercise:
                exercise_name = input("Enter new exercise name: ")
                description = input("Enter new exercise description: ")
                instructions = input("Enter new exercise instructions: ")
                exercise_time = input("Enter new exercise time: ")

                exercise.exercise_name = exercise_name
                exercise.description = description
                exercise.instructions = instructions
                exercise.exercise_time = exercise_time

                session.commit()
                print("Exercise updated successfully")
            else:
                print("Exercise not found")

                # generating report

        elif choice == '5':
            user_id = input("Enter User ID: ")
            user = session.query(User).filter_by(id=user_id).first()

            if user:
                # Generate the report for the user
                # You can customize this logic based on your specific report requirements
                report = f"User ID: {user.id}\n"
                report += f"Name: {user.name}\n"
                report += f"Email: {user.email}\n"
                report += "Exercises:\n"
                for exercise in user.exercises:
                    report += f"- Exercise Name: {exercise.exercise_name}\n"
                    report += f"  Description: {exercise.description}\n"
                    report += f"  Instructions: {exercise.instructions}\n"
                    report += f"  Exercise Time: {exercise.exercise_time}\n"

                print(report)
            else:
                print("User not found!")


        elif  choice  == '6':
                user_id = input("Enter User ID : ")
                user = session.query(User).filter_by(id=user_id).first()

                if user:
                    session.delete(user)
                    session.commit()
                    print("user successfully deleted")
                else:
                    print("user not found")

# updating instructor details
        elif choice  == '14':
            instructor_id =  input("Enter instructor ID")
            instructor  = session.query(Instructor).filter_by(id=instructor_id).first()

        if instructor:
            instructor_name  = input("Enter instructor name :")
            instructor_email = input("Enter instructor email :")
            instructor_specialization = input("Enter instructor specialization :")
            instructor_password = input("Enter instructor password :")
            instructor_experience = input("Enter instructor experience")

        #creating instance of the data
            instructor = instructor_name  = instructor_name
            instructor = instructor_email = instructor_email
            instructor = instructor_specialization = instructor_specialization
            instructor  =  instructor_password  = instructor_password
            instructor =  instructor_experience  = instructor_experience

        # committing the session

            session.commit()
            print("Instructor updated successfully")
        else:
            print("instructor not updated")








            
    
        elif  choice == '19':
            break

session.close()