# CrewaiVisionTool Crew

Welcome to the CrewaiVisionTool Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up an AI agent to use Vision Tool to extract text from images.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry

```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:
```bash
poetry lock
```
```bash
poetry install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**


## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```
or
```bash
poetry run crewai_vision_tool
```

This command initializes the crewai_vision_tool Crew, assembling the agents and assigning them tasks as defined in your configuration.

