from setuptools import setup, find_packages


setup(
    name='hips_hack',
    version='0.8',
    license='MIT',
    author = 'Jan Arvik, Truman DeWalch, Michael Peters',
    author_email='truman99@vt.edu',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Skumbl/hips-hack',
    keywords     = ['Encryption', 'Privacy'],
    install_requires = ['opencv-python', 'numpy'],
    long_description=open('README.md').read(),
)