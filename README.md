# hudlQEproj

Hello, 

Prior to running the tests within this framework and test suite:

1. This testsuite was designed for use within the PyCharm IDE by JetBrains
2. using settings-template.py, enter in username and password that will be used to run the suite,
and save the file as settings.py (this new file will be automatically ignored by Git when checking in)



A note: The security test was something I added while I was working through creating some of the other test scripts as I had noticed that a
user can be logged back in to their account if the back button is clicked within the same browser window and session.

I appreciate the opportunity to work on and develop my skills with Python and Selenium.
I had not had a chance to write test automation with Python prior to this and I thoroughly enjoyed having the chance to work on it.

Thank you!
Andrew Morgan


OVERVIEW OF TEST CASES

*NEGATIVE SCENARIOS*

Ensure that login is not allowed without entering a username and password

Ensure that login is not allowed when entering a username and a blank password

Ensure that login is not allowed when entering a blank username and a correct password

Ensure that login is not allowed when entering an incorrect username and password combination


*KEY FUNCTION TESTING*

Ensure that a User can successfully login using valid username and password credentials

*SECURITY TESTING*

Verify that when a User logs out, they cannot be logged back in by hitting back arrow in browser


