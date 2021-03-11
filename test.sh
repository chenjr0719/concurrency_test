hey -n 40 -c 20 -m GET -t 30 \
    http://localhost:8000


hey -n 40 -c 20 -m POST -t 30 \
    -T application/json \
    -D ./test-body.json \
    http://localhost:8000