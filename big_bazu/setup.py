from setuptools import setup

package_name = 'my_robot'


setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        (os.path.join('share', package_name,'launch'), glob('launch/*')),
        
        (os.path.join('share', package_name,'urdf'), glob('urdf/*')),

        (os.path.join('share', package_name,'config'), glob('config/*')),
        
        (os.path.join('share', package_name,'mesh'), glob('mesh/*')),
        
        (os.path.join('share', package_name,'world'), glob('world/*'))


    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='komalsai',
    maintainer_email='saianurag234@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'trajectory_generator = my_robot.trajectory_gen:main',
        'inverse_kinematics = my_robot.inverse_kinematics_solution:main',
        'waste_server = my_robot.waste_server:main',
        'waste_client = my_robot.waste_client:main',
        'image_save = my_robot.image_save:main',
        'move = my_robot.movement:main',
        'check = my_robot.test_move:main',
        'test = my_robot.gazebo:main'
        
        ],
    },
)
