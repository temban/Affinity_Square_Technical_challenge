# HTML Page Analyzer

## How to Build and Run the Solution Locally

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd html_page_analyzer
    ```

2. **Set up and run the server:**
    ```bat
    build.bat
    ```

3. **Open the client:**
    Open `client/index.html` in a web browser.

## Assumptions

- The input URL is valid and accessible.
- The HTML structure of the analyzed pages follows common standards.

## Design Decisions

- Used FastAPI for the backend due to its performance and ease of use.
- Used jQuery for AJAX requests in the frontend for better compatibility and simplicity.

## Constraints and Limitations

- The solution relies on a simple HTML parser which may not handle all edge cases.
- Error handling is basic and may not cover all possible errors.
