# tuckAdvisorsInterview
## **Setup**  
Install the required dependencies:  
```sh
pip install fastapi uvicorn
```

## **Run the API**  
Start the FastAPI application with:  
```sh
uvicorn api:app --reload
```

## **API Endpoints**  

### **GET Request**  
- **URL:** `http://127.0.0.1:8000/`  
- **Parameters:** None  
- **Response:** Returns the current markdown string.  

#### **Example Command:**  
```sh
curl -X GET "http://127.0.0.1:8000/"
```

---

### **POST Request**  
- **URL:** `http://127.0.0.1:8000/`  
- **Parameters:**  
  - Takes a string as `"new_text"` in the request body.  
  - Appends the new text to the existing markdown as a new sentence.  
  - The next GET or POST request will return the updated markdown.  

#### **Example Command:**  
```sh
curl -X POST "http://127.0.0.1:8000/" \
     -H "Content-Type: application/json" \
     -d '{"new_text": "This is a new insight about ABC."}'
```
