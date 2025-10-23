from setuptools import setup, find_packages

setup(
    name="verseposter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
    ],
    entry_points={
        "console_scripts": [
            "verseposter=verseposter.main:main"
        ],
    },
    description="Post the verse of the day to multiple platforms.",
    author="Carson Kopec",
    license="MIT",
    python_requires=">=3.9",
)
