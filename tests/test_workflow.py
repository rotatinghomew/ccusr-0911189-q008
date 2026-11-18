import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest

from slots.workflow import report


class WorkflowTest(unittest.TestCase):
    def setUp(self):
        self.path = Path(__file__).resolve().parents[1] / 'data' / 'sample.json'
        self.data = json.loads(self.path.read_text(encoding='utf-8'))

    def test_entry(self):
        result = subprocess.run([sys.executable, '-m', 'slots', 'offers', str(self.path)],
                                check=True, capture_output=True, text=True)
        self.assertEqual(json.loads(result.stdout), report(self.data))

    def test_shared_path_and_paid_cost(self):
        result = report(self.data)
        self.assertEqual(result['downtime'],{'maintenance':['QA','QB']})
        self.assertEqual(result['budget'],{'spent':44,'remaining':56})
        self.assertEqual(len(result['by_station']),4)

    def test_locked_slot_cannot_be_reused(self):
        self.data['orders'].append({'offer':'QD','paid':20})
        with self.assertRaises(ValueError):
            report(self.data)
