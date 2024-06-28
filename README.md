# HTML Page Analyzer

## How to Build and Run the Solution Locally

1. **Clone the repository:**
    ```sh
    git clone <https://github.com/temban/Affinity_Square_Technical_challenge>
    cd Affinity_Square_Technical_challenge
    ```

2. **Set up and run the Backend:**
    ```bat
    build.bat
    NB: I used .bat because I am on Windows
    ```

3. **Open the Frontend:**
    Open `Frontend/index.html` in a web browser.

## Assumptions

- The input URL is valid and accessible.
- The HTML structure of the analyzed pages follows common standards.

## Design Decisions

- Used FastAPI for the backend due to its performance and ease of use.
- Used jQuery for AJAX requests in the frontend for better compatibility and simplicity.

## Constraints and Limitations

- The solution relies on a simple HTML parser which may not handle all edge cases.
- Error handling is basic and may not cover all possible errors.


## Entir Project Summary
Functionalities:

1- HTML version extraction.

2- Title extraction.

3- Heading count.

4- Internal and external link extraction.

5- Login form detection.

6- Link validation using the validate_link function.

7- Redirection Handling:
The requests.head method with allow_redirects=True handles redirections automatically. If a link redirects, the final status and new location (if available) are captured.

![Screenshot (1008)](https://github.com/temban/Affinity_Square_Technical_challenge/assets/76685729/61540d26-16ec-4f06-af81-22ca95b56cb0)
![Screenshot (1009)](https://github.com/temban/Affinity_Square_Technical_challenge/assets/76685729/01595797-b8d8-4f7c-93d1-cd50729cd896)
![Screenshot (1006)](https://github.com/temban/Affinity_Square_Technical_challenge/assets/76685729/bb421ae3-6f0b-4346-8e28-7bcd472020ab)
![Screenshot (1007)](https://github.com/temban/Affinity_Square_Technical_challenge/assets/76685729/80dd2f8d-26b3-4628-ba12-f67eaddc093f)


