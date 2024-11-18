Browser_name = input("Enter the Browser Name:\n")
match Browser_name:
    case "firefox":
        print("Starting the browser with Firefox!!!")
    case "Chrome":
        print("The browser start with Chrome!!!!")
    case _:
        print("Browser not found")
