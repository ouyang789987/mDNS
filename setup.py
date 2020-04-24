import setuptools

#get long description
with open('README.md') as readme:
    long_description = readme.read()
#get version number
version = '0.0.0a0'
with open('mdns/__init__.py') as info:
    for line in info:
        if '__version__' in line:
            version = line.split('=')[-1].strip(' \'\n')
            break


setuptools.setup(
    name='mDNS',
    version=version,
    author='Andrea Parisotto',
    description='',
    long_description=long_description,
    url='https://github.com/Anubi85/mDNS',
    license='MIT',
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',
    packages = setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3.8',
    ],
    keywords=['Multicast DNS', 'mDNS'],
    python_requires='>=3.8',
)