# ghidra_scripts

Collection of Ghidra RE scripts

## Scripts

* `ghidra_headless.py`: Wrapper to run Ghidra in headless mode and execute a provided script with arguments


* `dump_functions.py`: Example script to dump function names and addresses

## Usage

`ghidra_headless.py` can be used as follows:

```
python ghidra_headless.py <binary> <script> <script arg1> <script arg2> <...>
```

Example:

```
python ghidra_headless.py /bin/ls scripts/dump_functions.py output.txt
```

