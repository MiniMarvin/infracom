# Simple filesocket transfer

This project aims to create a simple file transference example using the simple socket library provided in python as a default  library in the system.

# Instalation

To properly install the system run

```bash
pip install -r requirements.txt
```

or, if you have python and python3:

```bash
pip3 install -r requirements.txt
```

# Arguments

```
usage: client.py [-h] [--command COMMAND] [--file FILE] [--output OUTPUT]
                 [--data DATA]

optional arguments:
  -h, --help            show this help message and exit
  --command COMMAND, -c COMMAND
                        GET file filename | to get a file from the server
  --file FILE, -f FILE  File to get from server
  --output OUTPUT, -o OUTPUT
                        Output file name for get
  --data DATA, -d DATA  Output file data for post
```


# Running

In order to make it possible to run you must first start the server and them make the requests with the client:

```bash
python server.py
```

or, if you have python and python3

```bash
python3 server.py
```

Now to make the client requests the adopted call examples are:

### Get
Obs: tested with text files and with images

```bash
python client.py -c get -f serverFiles/file.txt -o clientFiles/example.txt
python client.py -c get -f serverFiles/img.jpg -o clientFiles/example.jpg
```

or, if you have python and python3

```bash
python3 client.py -c get -f serverFiles/file.txt -o clientFiles/example.txt
python3 client.py -c get -f serverFiles/img.jpg -o clientFiles/example.jpg
```

### Post
Tested with texts


```bash
python client.py -c post -f serverFiles/example.txt -d "o exemplo funcionou!"
python client.py -c post -f serverFiles/example.txt -d "$(cat clientFiles/loremipsum.txt)"
```

or, if you have python and python3

```bash
python3 client.py -c post -f serverFiles/example.txt -d "o exemplo funcionou!"
python3 client.py -c post -f serverFiles/example.txt -d "$(cat clientFiles/loremipsum.txt)"
```

### GetProg

```bash
python client.py -c getprog -f serverFiles/a.x -o clientFiles/example.x
```

or, if you have python and python3

```bash
python3 client.py -c getprog -f serverFiles/a.x -o clientFiles/example.x
```