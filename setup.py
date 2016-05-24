from distutils.core import setup

setup(
    name='SNoBoL',
    version='0.2',
    description='Supernova Bolometric Lightcurves',
    author='Jeremy A. Lusk',
    author_email='jeremy.lusk@gmail.com',
    url='https://github.com/JALusk/SNoBoL',
    packages=['snobol'],
    package_data={'snobol' : ['data/sn_data.h5']},
    license='MIT License',
    )   
