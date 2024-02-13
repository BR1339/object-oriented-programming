class Button:
    def __init__(self):
        self.count = 0
    def click(self):
        self.count += 1
    def click_count(self):
        return self.count

    def reset(self):
        self.count = 0

button = Button()
button.click()
button.click()
button.click()
print(button.click_count())
button.reset()
button.click()
button.click()
print(button.click_count())
button.reset()
button.click()
print(button.click_count())
