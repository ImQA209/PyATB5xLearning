from Browserpackage.startBrowser import openBrowser
from Browserpackage.StopBrowser import closeBrowser


def testcase():
    openBrowser()
    print("Hello browser running")
    closeBrowser()


testcase()
