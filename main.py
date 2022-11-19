import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

import random

workout_list = ["Leg Raises", "Burpees", "Ankle Touches", "Arm Circles",
"Lunges", "Bicycle Crunches", "Calf Raises", "Crunches", "Crossing Punches",
"Inclined Wall Push-ups", "Leg Raises", "Low Plank", "Diamond Push-ups", "Inclined Push-ups",
"Decline Push-ups", "Squats", "Punches", "Push-ups", "Side Lunges", "Sit-ups", "Triceps Dip",
"Up Down Push-ups", "Up Downs", "Wall Push Offs", "Wide Push-ups"]

random_number_one = random.randint(0, 24)
random_number_two = random.randint(0, 24)
random_number_three = random.randint(0, 24)
random_number_four = random.randint(0, 24)
random_number_five = random.randint(0, 24)
random_number_six = random.randint(0, 24)
random_number_seven = random.randint(0, 24)

random_workout_one = workout_list[random_number_one]
random_workout_two = workout_list[random_number_two]
random_workout_three = workout_list[random_number_three]
random_workout_four = workout_list[random_number_four]
random_workout_five = workout_list[random_number_five]
random_workout_six = workout_list[random_number_six]
random_workout_seven = workout_list[random_number_seven]


class Output_Workouts(BoxLayout):

    def __init__(self):
        super(Output_Workouts, self).__init__()

    def generate_workout(self):
        self.workout_label_1.text = str(random_workout_one)
        self.workout_label_2.text = str(random_workout_two)
        self.workout_label_3.text = str(random_workout_three)
        self.workout_label_4.text = str(random_workout_four)
        self.workout_label_5.text = str(random_workout_five)
        self.workout_label_6.text = str(random_workout_six)
        self.workout_label_7.text = str(random_workout_seven)

class Better_You_App(App):

    def build(self):
        return Output_Workouts()

better_you_app = Better_You_App()

better_you_app.run()
