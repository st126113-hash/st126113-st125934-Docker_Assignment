### Docker Assignment Project

This project is a machine learning web application for predicting BMW global sales using Flask and Docker.

---

## How to Run

```bash
docker build -t bmw-app .
docker run -p 5000:5000 bmw-app
```

Open: http://localhost:5000

---

## Project Structure

```
.
├── app.py
├── templates/
│   └── index.html
├── model.pkl
├── bmw_global_sales_2018_2025.csv
├── bmw_modified_prediction.ipynb
├── Dockerfile
├── requirements.txt
├── Demo_Assignment_Video.mp4
└── README.md
```

---

## Author

* Natthanon Narongsaksakul, st126113  & Waranon Neamtuptim, st125934
* https://github.com/st126113-hash
* https://github.com/Waranon021
