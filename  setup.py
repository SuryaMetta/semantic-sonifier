"""
setup.py - Professional package configuration
WHY: Makes your project installable, enables proper imports, and prepares for distribution
"""

from setuptools import setup, find_packages

# Read requirements from file
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="semantic-sonifier",
    version="0.1.0",
    description="AI system that translates images into music by understanding both content and mood",
    author="Metta Surya Teja",  # Replace with your name
    author_email="mettasuryateja0@gmail.com",  # Replace with your email
    packages=find_packages(where="src"),
    package_dir={"": "src"},  # This tells setuptools that packages are under src/
    install_requires=requirements,
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",  # You'll choose a license later
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="ai music vision multimodal deep-learning",
)