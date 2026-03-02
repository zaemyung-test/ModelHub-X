from setuptools import setup, find_packages

setup(
    name="llama",
    version="0.0.0",
    description="LLaMA: Open and Efficient Foundation Language Models",
    packages=find_packages(exclude=("tests",)),
    install_requires=[
        "torch>=1.9.0",
        "numpy",
    ],
)
