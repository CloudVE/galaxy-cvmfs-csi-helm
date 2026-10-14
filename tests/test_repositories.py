"""Verify that the CSI defaults deliver repository configuration to automount.

Requires Helm, PyYAML and built chart dependencies.
"""

import os
import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml

CHART = Path(os.environ.get(
    "GALAXY_CVMFS_CHART",
    Path(__file__).resolve().parents[1] / "galaxy-cvmfs-csi",
))


class RepositoryConfigurationTest(unittest.TestCase):
    def test_repository_configuration_reaches_automounter(self):
        output = subprocess.check_output(
            ["helm", "template", "galaxy-deps", str(CHART), "-n", "galaxy-deps"],
            text=True,
        )
        documents = [d for d in yaml.safe_load_all(output) if d]
        config = next(d for d in documents if d["kind"] == "ConfigMap"
                      and d["metadata"]["name"] == "cvmfs-csi-config-d")
        for repository in ("data.galaxyproject.org", "idc.galaxyproject.org"):
            with self.subTest(repository=repository):
                conf = config["data"][f"{repository}.conf"]
                self.assertIn(f"/etc/cvmfs/config.d/{repository}.pub", conf)
                self.assertIn("CVMFS_SERVER_URL=", conf)
                with tempfile.TemporaryDirectory() as directory:
                    key = Path(directory) / "repository.pub"
                    key.write_text(config["data"][f"{repository}.pub"])
                    subprocess.run(
                        ["openssl", "pkey", "-pubin", "-in", str(key), "-noout"],
                        check=True, capture_output=True,
                    )
        daemon = next(d for d in documents if d["kind"] == "DaemonSet")
        pod = daemon["spec"]["template"]["spec"]
        volume = next(v for v in pod["volumes"]
                      if v.get("configMap", {}).get("name") == config["metadata"]["name"])
        automount = next(c for c in pod["containers"] if c["name"] == "automount")
        mount = next(m for m in automount["volumeMounts"] if m["name"] == volume["name"])
        self.assertEqual(mount["mountPath"], "/etc/cvmfs/config.d")
        self.assertNotIn("subPath", mount)


if __name__ == "__main__":
    unittest.main()
