from setuptools import setup, find_packages

try:
    README = open('README').read()
except:
    README = None

setup(
    name='django-medusa',
    version=__import__('django_medusa').__version__,
    description='A Django static website generator.',
    include_package_data=True,
    author='Mike Tigas',  # update this as needed
    author_email='mike@tig.as',  # update this as needed
    url='https://github.com/mtigas/django-medusa/',
    download_url='https://github.com/mtigas/django-medusa',
    packages=find_packages(),
    install_requires=['django'],
    license='MIT',
    long_description=README,
    keywords='django static staticwebsite staticgenerator publishing',
    classifiers=["Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"],
    zip_safe=False
)
