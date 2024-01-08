import time
import compiled.tomllib as tomllib

from pathlib import Path

from tqdm import tqdm


def hello():
    n = 100000
    pyproject_toml = Path(__file__).parent.parent.parent / "pyproject.toml"
    text = pyproject_toml.read_text()
    start = time.perf_counter()
    for i in tqdm(range(n)):
        tomllib.loads(text)
    end = time.perf_counter()
    rate = n / (end - start)
    print(f"tomllib.loads: {rate:.0f} loads/sec")


if __name__ == "__main__":
    hello()
