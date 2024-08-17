from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import VisionTool
import os

@CrewBase
class CrewaiVisionToolCrew():
    """CrewaiVisionToolCrew crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"
    image_url = "https://m.media-amazon.com/images/M/MV5BNDUwNjBkMmUtZjM2My00NmM4LTlmOWQtNWE5YTdmN2Y2MTgxXkEyXkFqcGdeQXRyYW5zY29kZS13b3JrZmxvdw@@._V1_.jpg"
    vision_tool = VisionTool()
    
    @agent
    def image_text_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['image_text_extractor'],
            goal= f"Extract and analyze text from images efficiently using AI-powered tools. You should get the text from {self.image_url}",
            tools=[self.vision_tool],
            verbose=True
        )

    @task
    def text_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config['text_extraction_task'],
            output_file='extracted_text.txt'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewaiVisionToolCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )