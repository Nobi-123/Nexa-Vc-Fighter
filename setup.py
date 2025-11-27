from setuptools import setup, find_packages

setup(
    name="nexa-vc-fighter",
    version="1.0.0",
    author="sexyxcoders",
    description="Telegram Multi-VC Assistant Bot",
    url="https://github.com/Nobi-123/Nexa-Vc-Fighter",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.9,<3.10",
    install_requires=[
        "pyrogram==2.0.106",
        "tgcrypto",
        "pydub",
        "aiohttp"
    ],
    entry_points={
        "console_scripts": [
            # Allows running the bot with "nexa-bot" if bot.py has main()
            "nexa-bot=bot:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: POSIX :: Linux",
        "Topic :: Communications :: Chat",
    ],
)
