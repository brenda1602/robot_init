from setuptools import setup

PACKAGE_NAME = 'robot_gazebo'

setup(
    name=PACKAGE_NAME,
    version='1.0.0',
    package_dir={'': 'src'}
    packages=[PACKAGE_NAME],
    install_requires=['setuptools'],
    zip_safe=True,
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'spawn_robot = robot_gazebo.spawn_robot:main',
        ],
    },
)