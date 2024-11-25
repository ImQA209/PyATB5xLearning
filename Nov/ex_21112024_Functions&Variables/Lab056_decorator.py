def before_add_ui(func):
    def wrapper():
        print("Before starting UI")
        print("start the browser")
        func()
        print('Ending the UI')
        print("Stop the browser")
    return wrapper()

@ before_add_ui
def test_ui():
    print("I will test the UI")
