class person:
    def __init__(self, first_name, last_name, age, gender, dob, state_of_origin):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.dob = dob
        self.state_of_origin = state_of_origin

    def talk(self):
        print(f"""Hello, my name is {self.first_name} {self.last_name}. I am {self.age} years old and I am from {self.state_of_origin}. 
              I am a {self.gender}.I am from {self.state_of_origin} and I was born on {self.dob}.
              """)