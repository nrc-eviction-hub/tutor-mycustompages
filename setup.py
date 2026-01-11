from setuptools import setup, find_packages

setup(
    name="tutor-mycustompages",
    version="0.1.3",
    packages=find_packages(),
    entry_points={
        "tutor.plugin.v1": [
            "mycustompages = tutor_mycustompages",
        ],
    },
)

