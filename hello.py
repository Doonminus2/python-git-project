import config 
<<<<<<< HEAD


def say_hello(name):
    print(f"Hello, {name} from {config.APP_NAME}!")
=======
import datetime

def say_hello(name):
    now = datetime.datetime.now()
    print(f"Hello, {name} from {config.APP_NAME}!")
    print(f"Today is {now.strftime('%Y-%m-%d')}.")

>>>>>>> feature-date
def greet_user():
    name = input("please enter name: ")
    say_hello(name)

if __name__ == "__main__":
    greet_user()
