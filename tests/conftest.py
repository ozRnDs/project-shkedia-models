import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
import sys, os
import pytest
from datetime import datetime

sys.path.append(f"{os.getcwd()}/src/project_shkedia_models")
print(sys.path)
