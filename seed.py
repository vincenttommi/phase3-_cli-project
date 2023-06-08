from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Instructor, Exercise, Diet, Guidelines ,Admin  # Import the tables from your models module

# Create the engine and session
engine = create_engine('sqlite:///fitness.db')
Session = sessionmaker(bind=engine)
session = Session()

# Seed data for User
user1 = User(name='John Doe', email='johndoe@example.com', password='password1', enrolled_date=date(2022, 1, 15))
user2 = User(name='Jane Smith', email='janesmith@example.com', password='password2', enrolled_date=date(2022, 3, 20))
user3 = User(name='Michael Johnson', email='michael@example.com', password='password3', enrolled_date=date(2022, 4, 10))
user4 = User(name='Emily Davis', email='emily@example.com', password='password4', enrolled_date=date(2022, 6, 5))
session.add_all([user1, user2, user3, user4])
session.commit()

# Seed data for Instructor
instructor1 = Instructor(name='Instructor 1', email='instructor1@example.com', specialization='Yoga', password='password5', experience=5, user=user1)
instructor2 = Instructor(name='Instructor 2', email='instructor2@example.com', specialization='Pilates', password='password6', experience=3, user=user2)
instructor3 = Instructor(name='Instructor 3', email='instructor3@example.com', specialization='CrossFit', password='password7', experience=4, user=user3)
instructor4 = Instructor(name='Instructor 4', email='instructor4@example.com', specialization='Zumba', password='password8', experience=2, user=user4)
session.add_all([instructor1, instructor2, instructor3, instructor4])
session.commit()

# Seed data for Exercise
exercise1 = Exercise(exercise_name='Push-ups', description='Upper body exercise', instructions='Perform 3 sets of 10 repetitions', exercise_time='10 minutes', user=user1)
exercise2 = Exercise(exercise_name='Squats', description='Lower body exercise', instructions='Perform 3 sets of 12 repetitions', exercise_time='15 minutes', user=user2)
exercise3 = Exercise(exercise_name='Running', description='Cardiovascular exercise', instructions='Run for 30 minutes at a moderate pace', exercise_time='30 minutes', user=user3)
exercise4 = Exercise(exercise_name='Plank', description='Core exercise', instructions='Hold a plank position for 1 minute', exercise_time='5 minutes', user=user4)
session.add_all([exercise1, exercise2, exercise3, exercise4])
session.commit()

# Seed data for Diet
diet1 = Diet(day_of_week='Monday', instruction='Consume a balanced meal', user=user1)
diet2 = Diet(day_of_week='Tuesday', instruction='Include more fruits and vegetables', user=user2)
diet3 = Diet(day_of_week='Wednesday', instruction='Focus on lean protein sources', user=user3)
diet4 = Diet(day_of_week='Thursday', instruction='Limit processed food intake', user=user4)
session.add_all([diet1, diet2, diet3, diet4])
session.commit()

# Seed data for Guidelines
guidelines1 = Guidelines(day_of_week='Monday', exercise_details='Cardio workout', user=user1)
guidelines2 = Guidelines(day_of_week='Tuesday', exercise_details='Strength training', user=user2)
guidelines3 = Guidelines(day_of_week='Wednesday', exercise_details='Flexibility exercises', user=user3)
guidelines4 = Guidelines(day_of_week='Thursday', exercise_details='High-intensity interval training', user=user4)
session.add_all([guidelines1, guidelines2, guidelines3, guidelines4])
session.commit()

# Seed data for Admins
admin1 = Admin(name='Admin 1', email='admin1@example.com', password='adminpassword1', logged_date=date.today(), user=user1)
admin2 = Admin(name='Admin 2', email='admin2@example.com', password='adminpassword2', logged_date=date.today(), user=user2)
admin3 = Admin(name='Admin 3', email='admin3@example.com', password='adminpassword3', logged_date=date.today(), user=user3)
admin4 = Admin(name='Admin 4', email='admin4@example.com', password='adminpassword4', logged_date=date.today(), user=user4)
session.add_all([admin1, admin2, admin3, admin4])
session.commit()

# Close the session
session.close()