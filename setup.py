from setuptools import setup, find_packages

setup(
    name='PyScraper',
    version='1.0.0',
    author='Sondre Gustavsen',
    author_email='sondre.gus@gmail.com',
    description='PyScraper is a python framework that is ment to be a efficient, user-friendly webscraping framework.'
                'It was made as a shcool Exam project at the College University of Østfold, Norway in the subject "Frameworks"'
                'Along with Sondre, Kristoffer and Zakaria also assisted with report writing. ',
    packages=find_packages(),
    install_requires=[
        "python_version == 3.9.13",
        "requests==2.28.2",
        "urllib3==1.26.15",
        "pytest==7.2.2"
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
)
