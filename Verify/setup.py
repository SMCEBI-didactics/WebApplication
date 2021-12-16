from setuptools import setup

setup(
    name="Verify",
    description="Some Python scripts",
    version="1.0",
    author="awowra",
    author_email="github.com/awowra0",
    licence="None",
    packages=['Verify'],
    entry_points={
        'console_scripts' : ['verify = Verify.main:main']
    }
)



        
