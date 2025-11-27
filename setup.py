from setuptools import setup, find_packages

setup(
    name="nexa-vc-fighter",
    version="1.0.0",
    author="sexyxcoders",
    description="Telegram Multi-VC Assistant Bot",
    url="https://github.com/sexyxcoders/Nexa-Vc-Fighter",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pyrogram==2.0.106",
        "tgcrypto",
        "pydub",
        "aiohttp",
        # Install PyTgCalls 2.0 fork directly from GitHub
        "git+https://github.com/Laky64/pytgcalls.git@2.0.0"
    ],
    python_requires=">=3.9,<3.10",
    entry_points={
        "console_scripts": [
            # Allows running the bot with "nexa-bot" command if bot.py has main()
            "nexa-bot=bot:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: POSIX :: Linux",
        "Topic :: Communications :: Chat",
    ],
)
