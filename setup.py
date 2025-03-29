from setuptools import setup, find_packages
from webscout.version import __prog__, __version__

with open("README.md", encoding="utf-8") as f:
    README = f.read()

setup(
    name=__prog__,
    version=__version__,
    description="Search for anything using Google, DuckDuckGo, phind.com, Contains AI models, can transcribe yt videos, temporary email and phone number generation, has TTS support, webai (terminal gpt and open interpreter) and offline LLMs and more",
    long_description=README,
    long_description_content_type="text/markdown",
    author="OEvortex",
    author_email="helpingai5@gmail.com",
    packages=find_packages(),
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
        install_requires=[
            "setuptools",
            "wheel",
            "pip",
            "nodriver",
            "mistune",
            "tenacity",
            "curl_cffi",
            "nest-asyncio",
            'websocket-client',
            'colorama',
            "rich",
            "markdownify",
            "requests",
            "google-generativeai",
            "lxml>=5.2.2",
            "termcolor",
            "orjson",
            "PyYAML",
            "ollama",
            "pillow",
            "bson",
            "cloudscraper",
            "html5lib",
            "aiofiles",
            "openai",
            "prompt-toolkit",
            "primp",
            "pyreqwest_impersonate",
            "gradio_client",
            "psutil",
            "aiohttp",
        ],

    entry_points={
        "console_scripts": [
            "WEBS = webscout.cli:cli",
            "webscout = webscout.cli:cli",
        ],
    },
    extras_require={
        "dev": [
            "ruff>=0.1.6",
            "pytest>=7.4.2",
        ],
    },
    license="HelpingAI",
    project_urls={
        "Source": "https://github.com/OE-LUCIFER/Webscout",
        "Tracker": "https://github.com/OE-LUCIFER/Webscout/issues",
        "YouTube": "https://youtube.com/@OEvortex",
    },
)
