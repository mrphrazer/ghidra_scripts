# example script to dump function starts

#  check arguments
args = getScriptArgs()
if len(args) != 1:
    print("[*] Parameters: <output file>")
    exit(-1)

# parse arguments
output_file = args[0]

# get function iterator
fm = currentProgram.getFunctionManager()
functions = fm.getFunctions(True)

# walk over all functions
content = ""
for f in functions:
    content += "{}: 0x{:x}\n".format(f.name, f.getEntryPoint().getOffset())

# write output
open(output_file, "w").write(content)
