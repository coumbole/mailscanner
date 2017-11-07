from setuptools import setup

setup(
    name='mailscanner',
    packages=['mailscanner'],
    version='1.0.0',
    description='Parses email messages using IMAP',
    author='Ville Kumpulainen',
    author_email='ville.kumpulainen@gmail.com',
    url='http://github.com/coumbole/mailscanner',
    keywords = ['email', 'imap', 'parser'],
    classifiers = [
        'Programming Language :: Python',
        'Inteded Audience :: Developers',
        'License :: GNU General Public License v.3.0 (GPL-3.0)'
    ]
)
