from setuptools import setup , find_packages

setup(
    name='AshCrypt',
    version='1.0.0',
    author='AshrefGW',
    author_email='AshGw@users.noreply.github.com',
    description='Cryptography of text/files of any type with DBMS',
    url='https://github.com/yourusername/your-repository',
    packages=find_packages(),
    install_requires=[
        'bcrypt==4.0.1',
        'cryptography==40.0.2',
        'qrcode==7.4.2',
        'SQLAlchemy==2.0.15',
        'ttkbootstrap==1.10.1',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords=[
        'cryptography',
        'AES',
    ]
)
