from crewai import Task

from gen.agents import senior_software_engineer, senior_qa_engineer


coding_task = Task(
    description=(
        "Analyze the code provided ({pandas_code}). "
        "See what the code is doing and make a code in polars that does the exact same thing"
    ),
    expected_output=(
        "A well written polars code with comments."
    ),
    agent=senior_software_engineer,
    # async_execution=True
)


qa_task = Task(
    description=(
        "Analyze the code made by senior software engineer agent in coding task and make sure it runs correctly"
        "Double check if the initial code provided ({pandas_code}) and code created by senior software engineer "
        "agent performs the same task"
    ),
    expected_output=(
        "A well written polars code with any changes if required"
    ),
    agent=senior_qa_engineer,
    # async_execution=True
)
