import sys, os

from jsonrpc_python_client_generator.generator import ClientGenerator

openRpcFile = ''
clientFile = ''

for i in range(len(sys.argv)):
    if sys.argv[i] == "--schema":
        openRpcFile = sys.argv[(i+1)]
    if sys.argv[i] == "--output":
        clientFile = sys.argv[(i+1)]

if (os.path.isfile(clientFile)):
    raise SystemExit("Output file is already exists: " + clientFile)

if (os.path.isfile(openRpcFile) == False):
    raise SystemExit("OpenRpc file does not exist: " + openRpcFile)

with open(openRpcFile) as f: schema = f.read()

generator = ClientGenerator(schema=schema,output=os.path.abspath(clientFile))
generator.run()

