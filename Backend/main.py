from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bs4 import BeautifulSoup, Doctype
import requests
from urllib.parse import urljoin, urlparse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class URLRequest(BaseModel):
    url: str

def analyze_page(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=str(e))

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract HTML version (simplified)
    doctype = next((d for d in soup.contents if isinstance(d, Doctype)), "HTML5")
    html_version = doctype if isinstance(doctype, Doctype) else "HTML5"

    # Extract title
    title = soup.title.string if soup.title else "No title"

    # Count headings
    headings = {f'h{i}': len(soup.find_all(f'h{i}')) for i in range(1, 7)}

    # Count internal and external links
    domain = urlparse(url).netloc
    internal_links = []
    external_links = []
    for link in soup.find_all('a', href=True):
        link_url = urlparse(link['href'])
        full_url = urljoin(url, link['href'])
        if link_url.netloc == domain:
            internal_links.append(full_url)
        else:
            external_links.append(full_url)

    # Detect login form
    login_form = any(form for form in soup.find_all('form') if
                     any(input for input in form.find_all('input', {'type': 'password'})))

    # Validate links
    def validate_link(link):
        try:
            res = requests.head(link, allow_redirects=True, timeout=5)
            return {"url": link, "reachable": res.status_code == 200}
        except requests.RequestException as e:
            return {"url": link, "reachable": False, "reason": str(e)}

    internal_links_validation = [validate_link(link) for link in internal_links]
    external_links_validation = [validate_link(link) for link in external_links]

    return {
        "html_version": html_version,
        "title": title,
        "headings": headings,
        "internal_links": internal_links,
        "external_links": external_links,
        "login_form": login_form,
        "internal_links_validation": internal_links_validation,
        "external_links_validation": external_links_validation
    }

@app.post("/analyze")
async def analyze(request: URLRequest):
    results = analyze_page(request.url)
    return results

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, adjust as needed
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods, adjust as needed
    allow_headers=["*"],  # Allow all headers, adjust as needed
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)