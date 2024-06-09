import os
from crewai import Crew
from textwrap import dedent

from gen.agents import senior_software_engineer, senior_qa_engineer
from gen.tasks import coding_task, qa_task

from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_MODEL_NAME"] = 'gpt-4o'


class PandasToPolarsCrew:

    def run(self, pandas_code: dict):
        crew = Crew(
            agents=[senior_software_engineer, senior_qa_engineer],
            tasks=[coding_task, qa_task],
            verbose=True
        )
        return crew.kickoff(inputs=pandas_code)


if __name__ == "__main__":
    print("## Welcome to Pandas To Polars Crew")
    print('-------------------------------')
    pandas_code = input(
        dedent("""
          Write/paste your code?
        """))

    pandas_code = {
        'pandas_code': pandas_code
    }

    crew = PandasToPolarsCrew()
    result = crew.run(pandas_code)

    print("\n\n########################")
    print("## Here is the Final Polars Code:")
    print("########################\n")
    print(result)


