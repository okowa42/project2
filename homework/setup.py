from setuptools import setup

package_name = 'homework'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'requests'],
    zip_safe=True,
    maintainer='Akari Hirohara',
    maintainer_email='a.hirohara.0526@gmail.com',
    description='a package for homework',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'bitcoin_publisher = homework.bitcoin_publisher:main',
        ],
    },
)
