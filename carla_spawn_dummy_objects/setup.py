"""
Setup for carla_spawn_dummy_objects
"""
import os
from glob import glob
ROS_VERSION = int(os.environ['ROS_VERSION'])

if ROS_VERSION == 2:
    from setuptools import setup

    package_name = 'carla_spawn_dummy_objects'
    setup(
        name=package_name,
        version='0.0.0',
        packages=['src/' + package_name],
        data_files=[
            ('share/ament_index/resource_index/packages',
             ['resource/' + package_name]),
            ('share/' + package_name, ['package.xml']),
            ('share/' + package_name + '/config',
             ['config/objects.json']),
            (os.path.join('share', package_name), glob('launch/*.launch.py'))
        ],
        install_requires=['setuptools'],
        zip_safe=True,
        maintainer='YSH',
        maintainer_email='yshgit@gmail.com',
        description='CARLA spawn for dummy obstacle objects',
        license='MIT',
        tests_require=['pytest'],
        entry_points={
            'console_scripts': [
                'carla_spawn_dummy_objects = src.carla_spawn_dummy_objects.carla_spawn_dummy_objects:main',
            ],
        },
    )
