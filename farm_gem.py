import time
import cv2 as cv
import numpy as np
import pyautogui
import keyboard

class FindGem:
    def __init__(self, main_agent, print_menu):
        """
        Initializes FindGem object.

        Args:
            main_agent: Main agent object for interaction with the game.
            print_menu: Boolean flag to print the menu or not.
        """
        self.main_agent = main_agent
        self.print_menu = print_menu
        self.running = True
        self.paused = False
        self.q_pressed = False
        self.screen = self.main_agent.screen1

        # Load images
        self.load_images()

        # Main algorithm to find gem
        self.movement_sequence = ['left'] * 14 + ['down'] + ['right'] * 14 + ['down']
        self.current_movement_index = 0
        self.move_camera_count = 0

    def load_images(self):
        # Load images required for image recognition.
        images = {
            'gem_pit': 'IMG/gem_pit.png',
            'pic1': 'IMG/pic1.png',
            'pic3': 'IMG/pic3.png',
            'gather': 'IMG/gather1.png',
            'new_troop': 'IMG/new_troop1.png',
            'time': 'IMG/time.png',
            'findplace': 'IMG/find.png'
        }
        for name, path in images.items():
            setattr(self, name, cv.imread(path, cv.IMREAD_ANYCOLOR))

    def start_place(self):
        # Start the process of finding the gem.
        march_location = cv.matchTemplate(self.screen, self.findplace, cv.TM_CCOEFF_NORMED)
        march_loc_arr = np.array(march_location)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(march_loc_arr)
        threshold = 0.7
        if max_val >= threshold:
            x, y = max_loc
            x += 14
            y += 12
            screen_pos2 = x, y
            pyautogui.moveTo(screen_pos2[0], screen_pos2[1], 0.2, pyautogui.easeOutQuad)
            time.sleep(0.1)
            pyautogui.doubleClick()
            time.sleep(0.1)
            pyautogui.press('tab')
            time.sleep(0.1)
            pyautogui.press('tab')
            pyautogui.write('1166')
            time.sleep(0.1)
            pyautogui.press('tab')
            pyautogui.write('1166')
            pyautogui.moveTo(1194, 292, 0.2, pyautogui.easeOutQuad)
            pyautogui.doubleClick()
            self.find_gem()

    def find_gem(self):
        # Search for the gem on the screen.
        if self.screen is not None:
            time.sleep(1)
            march_location = cv.matchTemplate(self.screen, self.gem_pit, cv.TM_CCOEFF_NORMED)
            march_loc_arr = np.array(march_location)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(march_loc_arr)
            threshold = 0.52
            if max_val >= threshold:
                if self.pic1 is not None:
                    square_size = 150
                    x, y = max_loc
                    x += 66
                    y += 36
                    top_left = (max(0, x - square_size // 2), max(0, y - square_size // 2))
                    bottom_right = (
                    min(self.screen.shape[1], x + square_size // 2), min(self.screen.shape[0], y + square_size // 2))
                    square_region = self.screen[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
                    second_march_location1 = cv.matchTemplate(square_region, self.pic1, cv.TM_CCOEFF_NORMED)
                    second_march_location2 = cv.matchTemplate(square_region, self.pic3, cv.TM_CCOEFF_NORMED)
                    second_max_val1 = cv.minMaxLoc(second_march_location1)[1]
                    second_max_val2 = cv.minMaxLoc(second_march_location2)[1]
                    threshold = 0.5
                    if second_max_val1 >= threshold or second_max_val2 >= threshold:
                        self.move_camera()
                    else:
                        x, y = max_loc
                        x += 66
                        y += 36
                        self.get_gem_position(x, y)
            else:
                self.move_camera()

    def get_gem_position(self, x, y):
        # Get the position of the gem.
        screen_pos = x, y
        pyautogui.moveTo(screen_pos[0], screen_pos[1], 0.2, pyautogui.easeOutQuad)
        self.mouse_click()

    def mouse_click(self):
        # Simulate a mouse click.
        time.sleep(0.1)
        pyautogui.doubleClick()
        time.sleep(0.5)
        self.click_gather()

    def click_gather(self):
        # Click on the gather button.
        march_location = cv.matchTemplate(self.screen, self.gather, cv.TM_CCOEFF_NORMED)
        march_loc_arr = np.array(march_location)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(march_loc_arr)
        threshold = 0.5
        if max_val >= threshold:
            x, y = max_loc
            x += 100
            y += 32
            screen_pos = x, y
            pyautogui.moveTo(screen_pos[0], screen_pos[1], 0.2, pyautogui.easeOutQuad)
            time.sleep(0.1)
            pyautogui.doubleClick()
            time.sleep(0.5)
            self.click_new_troop()
        else:
            time.sleep(0.5)
            self.move_camera()

    def click_new_troop(self):
        # Click on the new troop button.
        march_location = cv.matchTemplate(self.screen, self.new_troop, cv.TM_CCOEFF_NORMED)
        march_loc_arr = np.array(march_location)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(march_loc_arr)
        threshold = 0.5
        if max_val >= threshold:
            x, y = max_loc
            x += 100
            y += 35
            screen_pos2 = x, y
            pyautogui.moveTo(screen_pos2[0], screen_pos2[1], 0.2, pyautogui.easeOutQuad)
            time.sleep(0.1)
            pyautogui.doubleClick()
            time.sleep(0.5)
            self.send_march()
        else:
            pyautogui.doubleClick()
            time.sleep(180) # time to sleep before clicking on the node again.

    def send_march(self):
        # Send the troop for march.
        march_location = cv.matchTemplate(self.screen, self.time, cv.TM_CCOEFF_NORMED)
        march_loc_arr = np.array(march_location)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(march_loc_arr)

        threshold = 0.5
        if max_val >= threshold:
            x, y = max_loc
            screen_pos = x, y
            pyautogui.moveTo(screen_pos[0], screen_pos[1], 0.2, pyautogui.easeOutQuad)
            time.sleep(0.1)
            pyautogui.doubleClick()
            time.sleep(0.5)
            self.move_camera()

    def move_camera(self):
        # Move the camera to search for the gem.
        direction = self.movement_sequence[self.current_movement_index]
        if direction in ['up', 'down']:
            move_delay = 0.6    # duration of pressing the up or down button.
        else:
            move_delay = 0.8    # duration of pressing the left or right button.
        pyautogui.keyDown(direction)
        time.sleep(move_delay)
        pyautogui.keyUp(direction)
        self.current_movement_index = (self.current_movement_index + 1) % len(self.movement_sequence)
        time.sleep(0.6)
        self.move_camera_count += 1
        print(self.move_camera_count)
        if self.move_camera_count == 250: # count to start a new loop
            self.move_camera_count = 0
            time.sleep(0.5)
            pyautogui.press('space')
            time.sleep(1)
            pyautogui.press('space')
            time.sleep(3)
            self.start_place()
            self.current_movement_index = 0
        elif self.move_camera_count == 50: # fix possible misclicks
            time.sleep(0.1)
            pyautogui.press('esc')
            time.sleep(0.1)
            pyautogui.press('esc')

    def stop(self):
        # Pause the execution.
        print("stop...")
        self.paused = True

    def start(self):
        # Resume the execution.
        print("start...")
        self.paused = False

    def exit(self):
        # Exit the program.
        if not self.q_pressed:
            print("Exiting...")
            self.running = False
            self.q_pressed = True

    def run(self):
        # Run the main loop.
        keyboard.add_hotkey('e', self.stop)
        keyboard.add_hotkey('t', self.start)
        keyboard.add_hotkey('q', self.exit)
        self.start_place()
        while self.running:
            if not self.paused:
                self.find_gem()
            time.sleep(0.5)