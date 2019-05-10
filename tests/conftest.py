import shutil
import sys
import pytest
from pathlib import Path

sys.path.append(str(Path.joinpath(Path(__file__).parent, 'helpers')))

@pytest.fixture(scope="function")
def default_download_folder(tmpdir):
    tmp = Path(tmpdir.mkdir("Downloads"))
    yield tmp
    shutil.rmtree(tmp)
