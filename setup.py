import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="TextSummarizer",
    version="0.0.1",
    author="Harshabhi6129",
    author_email="harshakusampudi@gmail.com",
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Harshabhi6129/Text_Summarizer_Project",
    project_urls={
        "Bug Tracker": "https://github.com/Harshabhi6129/Text_Summarizer_Project/issues",
    },
    package_dir={"": "src"},  # Ensure package structure is correct
    packages=setuptools.find_packages(where="src"),
)
