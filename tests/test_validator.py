import unittest

from core.validator import DEFAULT_SAMPLE, load_metrics, validate_metrics


class ValidatorTests(unittest.TestCase):
    def test_public_sample_passes(self):
        document = load_metrics(DEFAULT_SAMPLE)
        self.assertEqual(validate_metrics(document), [])
        self.assertEqual(set(document["residues"]), {"Lys22", "Asp44", "Gly46"})

    def test_threshold_can_fail_a_record(self):
        document = load_metrics(DEFAULT_SAMPLE)
        document["residues"]["Gly46"]["pLDDT"] = 84.9
        self.assertEqual(validate_metrics(document), ["Gly46"])


if __name__ == "__main__":
    unittest.main()
