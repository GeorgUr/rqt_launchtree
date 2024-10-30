import os
from glob import glob
from setuptools import setup
from setuptools import find_packages

package_name = 'rqt_launchtree'

setup(
    name=package_name,
    version='0.1.5',
    packages=[package_name, package_name],
    package_dir={'': 'src'},
	data_files=[
		('share/ament_index/resource_index/packages',
			['resource/' + package_name]),
		(os.path.join('share', package_name, 'resource/img'), glob(os.path.join('resource/img', '*'))),
		(os.path.join('share', package_name, 'resource'), glob(os.path.join('resource', 'launchtree_widget.ui'))),
		('share/' + package_name, ['package.xml']),
		('share/' + package_name, ['plugin.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Philipp Schillinger',
    maintainer_email='schillin@kth.se',
    description='An RQT plugin for hierarchical launchfile configuration introspection.',
    license='BSD',
    entry_points={
        'console_scripts': [
            'rqt_launchtree = rqt_launchtree.main:main',
        ],
    },
)
