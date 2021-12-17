from setuptools import setup

setup(
    name="Verify",
    description="Verify",
    version="1.0",
    author="akopec",
    author_email="a.kopec.b@gmail.com",
    licence="None",
    packages=['Verify'],
    entry_points={
        'console_scripts' : ['verify = Verify.main:main']
    }
)



    
