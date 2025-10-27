import tokenize
import io
import dis

def a():
    source = "def f():\n" "\tif x\n" '\x00' '0000000000'
    fp = io.StringIO(source)
    list(tokenize.generate_tokens(fp.readline))


a()

'''
FIX:
    lexer.c to add a final check error at EOF to force raise Error:

    ```
            else if (c == EOF && PyErr_Occurred()) {
                return MAKE_TOKEN(ERRORTOKEN);
            }
    ```

'''