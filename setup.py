from setuptools import setup, find_packages

setup(
    name="tutor-mycustompages",
    version="0.1.5",  # increment version as needed
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "tutor.plugins.v1": [
            "mycustompages = tutor_mycustompages.hooks",
        ],
    },
)


