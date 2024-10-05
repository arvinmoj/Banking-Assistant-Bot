from setuptools import setup, find_packages

setup(
    name='banking_assistant',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'setuptools',
        'python-telegram-bot',
    ],
    entry_points={
        'console_scripts': [
            'src=main:main',
        ],
    },
    author='Arvin',
    author_email='arvinmoj@protonmail.com',
    description='A Telegram bot for banking assistance',
    url='https://github.com/yourusername/banking_assistant',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)