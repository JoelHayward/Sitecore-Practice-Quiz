from cx_Freeze import setup, Executable

# Replace 'sitecorePracticeQuiz.py' with the actual name of your Python script
script = 'sitecorePracticeQuiz.py'

# Specify the base as 'Console' or 'Win32GUI' depending on your application type
base = 'Console'

executables = [Executable(script, base=base, targetName='sitecorePracticeQuiz.exe')]

setup(
    name='Sitecore Practice Quiz',
    version='1.0',
    description='Quiz application for Sitecore practice',
    executables=executables
)
