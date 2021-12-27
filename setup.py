from setuptools import find_packages, setup

with open("version", "r") as f:
    version = f.read().strip()
with open("docs/README.md", "r") as f:
    ld = f.read().strip()

setup(
    name="MangDL",
	author="whinee",
	author_email="whinyaan@gmail.com",
    version=version,
    description="The most inefficent Manga downloader for PC",
    long_description=ld,
    url="https://github.com/MangDL/MangDL",
	license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	packages=find_packages(),
	include_package_data=True,
    python_requires=">=3.9",
	install_requires=[
        "BeautifulSoup4",
		"click",
        "httpx",
		"lxml",
        "patool",
        "pyyaml",
        "tabulate",
        "toml",
        "tqdm",
        "yachalk",
        "yarl",
	],
	entry_points = {
        'console_scripts': ['mangdl=mangdl.cli:cli'],
    },
)
