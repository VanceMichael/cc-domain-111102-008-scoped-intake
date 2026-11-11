import unittest
import json
from app.wire import Replay

from app.partner import Partner
class DomainTests(unittest.TestCase):
    def test_projection(self):
        self.assertEqual(set(Partner().page("public",["id"],"public")["items"][0]),{"id"})
    def test_fault_mode(self):
        self.assertIn("lon",Partner().page("public",["id"],"public",violate=True)["items"][0])
    def test_grant_copy(self):
        p=Partner();v=p.grant("public");v["fields"].clear()
        self.assertTrue(p.grant("public")["fields"])


class WireTests(unittest.TestCase):
    def test_unknown_route(self):
        from tempfile import TemporaryDirectory
        from pathlib import Path
        with TemporaryDirectory() as d:
            p=Path(d)/"routes.json";p.write_text("{}")
            self.assertEqual(Replay(p).get("https://missing.invalid").status,404)
