import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from src.map.Road import Road
from src.map.Coordinates import Coordinates
from src.map.Intersection import Intersection

def test_