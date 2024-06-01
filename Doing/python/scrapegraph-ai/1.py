# %%
from scrapegraphai.graphs import SmartScraperGraph
import markdown
from bs4 import BeautifulSoup

graph_config = {
    "llm": {
        "model": "ollama/qwen:7b",
        "temperature": 0,
        "format": "json",  # Ollama needs the format to be specified explicitly
        "base_url": "http://localhost:11434",  # set Ollama URL
    },
    "embeddings": {
        "model": "ollama/mxbai-embed-large",
        "base_url": "http://localhost:11434",  # set Ollama URL
    },
    "verbose": True,
}

# %%
smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the projects with their descriptions",
    # also accepts a string with the already downloaded HTML code
    source="https://daily.zhihu.com/story/9772809",
    config=graph_config
)


# %%
result = smart_scraper_graph.run()
print(result)
