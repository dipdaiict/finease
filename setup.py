import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "finease"
AUTHOR_USER_NAME = "dipdaiict"
SRC_REPO = "finease"
AUTHOR_EMAIL = "dippatel256@gmail.com"

setuptools.setup(
    # Package name
    name=SRC_REPO,
    # Package version
    version=__version__,
    # Author name
    author=AUTHOR_USER_NAME,
    # Author email
    author_email=AUTHOR_EMAIL,
    # Short package description
    description="FinEase is a Python package for financial calculations and analysis.",
    # Detailed package description (can be README contents)
    long_description=long_description,
    # Specify the type of long description (Markdown format)
    long_description_content_type="text/markdown",
    # URL to the project homepage
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    # URLs to additional project-related pages (e.g., Bug Tracker)
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues"
    },
    # Directory containing Python packages (source code)
    package_dir={"": "src"},
    # Automatically find all packages under the "src" directory
    packages=setuptools.find_packages(where="src"),
)
