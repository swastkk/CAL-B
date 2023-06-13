from setuptools import setup, find_packages

classifiers =[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: POSIX :: Linux",
]
    
setup(
    name= 'CAL-B',
    version= '0.0.1',
    description= 'basiCALC- A basic Calculator python package',
    long_description= open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/swastkk/CAL-B',
    project_urls= {
        Bug Tracker: "https://github.com/swastkk/CAL-B/issues"
    },
    author= 'Swastik Sharma',
    author_email= 'swastkk@gmail.com',
    license= 'MIT',
    classifiers= classifiers,
    keywords= 'calculators',
    packages= find_packages(),
    install_requires= ['']


)
