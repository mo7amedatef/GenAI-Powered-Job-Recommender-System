from mcp.server.fastmcp import FastMCP
from src.job_api import fetch_linkedin_jobs, fetch_naukri_jobs 

mcp = FastMCP("Job Recommender")

@mcp.tool()
async def fetchlinkedin(listofkey: list[str]):
    """Fetch LinkedIn jobs based on a list of keywords."""
    return fetch_linkedin_jobs(listofkey)

@mcp.tool()
async def fetchnaukri(listofkey: list[str]):
    """Fetch Naukri jobs based on a list of keywords."""
    return fetch_naukri_jobs(listofkey)


if __name__ == "__main__":
    mcp.run(transport='stdio')