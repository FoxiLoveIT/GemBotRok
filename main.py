from PIL import ImageGrab
import numpy as np
import cv2 as cv
import time
from threading import Thread
from farm_gem import FindGem
import telebot


class MainAgent:
    def __init__(self):
        self.screen = None
        self.screen1 = None

def update_screen(agent):
    """
    Function to continuously update the screen capture.

    Args:
        agent: Main agent object.
    """
    while True:
        # Capture the screen and convert it to OpenCV format
        agent.screen = ImageGrab.grab()
        agent.screen = np.array(agent.screen)
        agent.screen1 = cv.cvtColor(agent.screen, cv.COLOR_RGB2BGR)

        # Check for captcha
        captcha_template = cv.imread('Img/captcha.png')
        captcha_template = np.array(captcha_template)
        result = cv.matchTemplate(agent.screen1, captcha_template, cv.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv.minMaxLoc(result)

        # If captcha detected, send alert and exit
        if max_val >= 0.7:
            print("Captcha detected!")
            bot_token = 'YOUR_BOT_TOKEN'
            bot = telebot.TeleBot(token=bot_token)
            chat_id = 'YOUR_CHAT_ID'
            bot.send_message(chat_id=chat_id, text='Captcha detected!')
            sys.exit("Captcha detected! Exiting...")

def print_menu():
    """
    Function to print the main menu.
    """
    print("Enter a command:")
    print("\tS\tStart the main agent")
    print("\tG\tFind Gem")
    print("\tL\tQuiz answer")
    print("\tQ\tQuit")

if __name__ == "__main__":
    main_agent = MainAgent()
    print_menu()

    while True:
        user_input = input().strip().lower()

        if user_input == "s":
            # Start the screen update thread
            update_screen_thread = Thread(
                target=update_screen,
                args=(main_agent,),
                name='update_screen_thread',
                daemon=True)
            update_screen_thread.start()
            print("Thread Started")

        elif user_input == "g":
            # Start finding gems
            gem_agent = FindGem(main_agent, print_menu)
            print('Starting in 10 seconds...')
            time.sleep(10)
            gem_agent.run()

        elif user_input == "q":
            # Quit the program
            cv.destroyAllWindows()
            break

        else:
            print("Invalid input")
            print_menu()

    print("Exiting...")
def update_screen(agent):

    while True:
        agent.screen = ImageGrab.grab()
        agent.screen = np.array(agent.screen)
        agent.screen1 = cv.cvtColor(agent.screen, cv.COLOR_RGB2BGR)
        captcha_template = cv.imread('Img/captcha.png')
        captcha_template = np.array(captcha_template)
        result = cv.matchTemplate(agent.screen1, captcha_template, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        if max_val >= 0.7:
            print("Captcha detected!")
            bot_token = '7074732815:AAF02TzERJ8hD9HYXBwVT2jFyqVr4bMW0UI'
            bot = telebot.TeleBot(token=bot_token)
            chat_id = '1247823230'
            bot.send_message(chat_id=chat_id, text='Captcha detected!')
            sys.exit("Captcha detected! Exiting...")


def print_menu():
    print("Enter a command:")
    print("\tS\tStart the main agent")
    print("\tG\tFind Gem")
    print("\tL\tQuiz answer")
    print("\tQ\tQuit")

if __name__ == "__main__":
    main_agent = MainAgent()
    print_menu()
    while True:
        user_input = input()
        user_input = str.lower(user_input).strip()

        if user_input == "s":
            update_screen_tread = Thread(
                target=update_screen,
                args=(main_agent,),
                name='update_screen_tread',
                daemon=True)
            update_screen_tread.start()
            print("Thread Started")
        elif user_input == "g":
            march_agent = FindGem(main_agent, print_menu)
            print('start 10sec')
            time.sleep(10)
            march_agent.run()
        elif user_input == "q":
            cv.destroyAllWindows()
            break
        else:
            print("Invalid input")
            print_menu()
    print("Exiting...")
