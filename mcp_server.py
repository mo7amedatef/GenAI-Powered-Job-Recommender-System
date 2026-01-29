from mcp.server.fastmcp import FastMCP
from src.job_api import fetch_linkedin_jobs, fetch_naukri_jobs 

mcp = FastMCP("Job Recommender")

@mcp.tool()
async def fetchlinkedin(listofkey: list[str], location: str = "Egypt"):
    """Fetch LinkedIn jobs based on a list of keywords and location."""
    query = " ".join(listofkey)
    return fetch_linkedin_jobs(query, location)

@mcp.tool()
async def fetchnaukri(listofkey: list[str], location: str = "india"):
    """Fetch Naukri jobs based on a list of keywords and location."""
    query = " ".join(listofkey)
    return fetch_naukri_jobs(query, location)


if __name__ == "__main__":
    mcp.run(transport='stdio')