docker run -it --rm -v $PWD:/code -w /code -p 8000:8000 python:3.8 bash
# apt update && apt install -y libev-dev
pip install -r requirements.txt
# python main.py
gunicorn -w 9 -b 0.0.0.0:8000 main:app
