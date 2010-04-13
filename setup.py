from distutils.core import setup

setup(
    name='pychimp',
    version=__import__('pychimp').__version__,
    description='A reusable Django app for queuing the sending of email',
    long_description=open('docs/usage.txt').read(),
    author='Hunter Ford',
    author_email='hunterford@gmail.com',
    url='http://code.google.com/p/pychimp/',
    packages=[
        'pychimp',
    ],
    package_dir={'pychimp': 'pychimp'},
    classifiers=[
    ]
)
