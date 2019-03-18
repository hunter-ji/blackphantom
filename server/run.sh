gunicorn -w 1 -b 0.0.0.0:5000 server:app --log-level debug --worker-class eventlet
