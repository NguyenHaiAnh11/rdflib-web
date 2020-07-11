from setuptools import setup, find_packages

setup(
    name = 'rdflib-web',
    version = __version__,
    description = "RDFLib Web Apps.",
    author = "Gunnar Aastrand Grimnes",
    author_email = "gromgull@gmail.com",
    url = "https://github.com/RDFLib/rdflib-web",
    license = "BSD",
    platforms = ["any"],
    classifiers = ["Programming Language :: Python",
                   "License :: OSI Approved :: BSD License",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   "Operating System :: OS Independent",
                   ],
    packages = ['rdflib_web'],
    package_dir = { 'rdflib_web': 'rdflib_web' },
    package_data = { 'rdflib_web': ['templates/*.html','static/*',]}
    #packages=find_packages(include=['exampleproject', 'exampleproject.*'])
)

install_requires = [
    'flask',
    'rdflib>=4.0',
]


