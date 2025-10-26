import tokenize
import io

source = "def f():\n" "\tif x\n" '\x00'
fp = io.StringIO(source)
list(tokenize.generate_tokens(fp.readline))
