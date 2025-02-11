# tuckAdvisorsInterview
Ensure you have Python installed, then install the required libraries:
```bash
pip install fastapi uvicorn
**Run the API** uvicorn api:app --reload
GET: no parameters in the request body, returns the current markdown string.
POST: takes a string as a parameter in the request body, and “updates” the existing markdown (ie. adds the string to the end of the existing markdown as a new sentence). The next time a GET / POST request to the API is made, it uses the updated markdown string.
These are the commands you would run in termingal to test the get and post endpoints:
curl -X GET "http://127.0.0.1:8000/"

curl -X POST "http://127.0.0.1:8000/" \
     -H "Content-Type: application/json" \
     -d '{"new_text": "This is a new insight about ABC."}' 
