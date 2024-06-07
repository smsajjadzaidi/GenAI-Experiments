from crewai_tools import (
  # FileReadTool,
  ScrapeWebsiteTool,
  SerperDevTool
)

search_tool = SerperDevTool()
pandas_documentation_scrape_tool = ScrapeWebsiteTool("https://pandas.pydata.org/docs/index.html")
polars_documentation_scrape_tool = ScrapeWebsiteTool("https://docs.pola.rs/")
# read_code = FileReadTool(file_path='')
