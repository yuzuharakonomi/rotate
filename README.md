# rotate

Simple Caesar-style rotation for ASCII letters.

## Install

```bash
pip install -e .
```

## Use

```python
from rotate.rotate import rotate

rotate("Hello, World!", 1)  # "Ifmmp, Xpsme!"
```

## Test

```bash
uvx pytest
```

## Format
```bash
uvx ruff format
```

## Type Check
```bash
uvx pyright
```

