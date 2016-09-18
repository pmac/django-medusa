from setuptools import setup, find_packages

try:
    README = open('README.md').read()
except:
    README = None

setup(
    name='django-medusa',
    version='0.3.2',
    description='A Django static website generator.',
    include_package_data=True,
    author='Brandon Taylor',  # update this as needed
    author_email='alsoicode@gmail.com',  # update this as needed
    url='https://github.com/alsoicode/django-medusa',
    download_url='https://github.com/alsoicode/django-medusa',
    packages=find_packages(),
    install_requires=['django'],
    license='APL',
    long_description=README,
    keywords='django static staticwebsite staticgenerator publishing',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
    zip_safe=False
)
