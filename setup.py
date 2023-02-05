# from distutils.core import setup
# setup(
#   name         = 'hips-hack',     # How you named your package folder (MyLib)
#   packages     = ['hips-hack'],   # Chose the same as "name"
#   version      = '0.1',      # Start with a small number and increase it with every change you make
#   license      = 'MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
#   description  = 'Python package to encode text into images',   # Give a short description about your library
#   author       = 'Jan Arvik, Truman DeWalch, Michael Peters',                   # Type in your name
#   author_email = 'truman99@vt.com',      # Type in your E-Mail
#   url          = 'https://github.com/Skumbl/hips-hack',   # Provide either the link to your github or to your website
#   # download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
#   keywords     = ['Encryption', 'Privacy'],   # Keywords that define your package best
#   install_requires = ['opencv-python', 'numpy'],
#   classifiers      = [
#     'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
#     'Intended Audience :: Developers',      # Define that your audience are developers
#     'Topic :: Software Development :: Build Tools',
#     'License :: OSI Approved :: MIT License',   # Again, pick a license
#     'Programming Language :: Python :: 3.7',
#     'Programming Language :: Python :: 3.8',
#     'Programming Language :: Python :: 3.9',
#     'Programming Language :: Python :: 3.10',
#     'Programming Language :: Python :: 3.11',
#   ],
# )

from setuptools import setup, find_packages


setup(
    name='hips_hack',
    version='0.5',
    license='MIT',
    author = 'Jan Arvik, Truman DeWalch, Michael Peters',
    author_email='truman99@vt.edu',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Skumbl/hips-hack',
    keywords     = ['Encryption', 'Privacy'],
    install_requires = ['opencv-python', 'numpy'],
)