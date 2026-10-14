A Helm chart for installing the [CVMFS-CSI
driver](https://github.com/cvmfs-contrib/cvmfs-csi/tree/master/deployments/helm),
with Galaxy specific repositories preconfigured.


## Use

To use, clone this repository and install the chart:
```
git clone https://github.com/CloudVE/galaxy-cvmfs-csi-helm
```

Install the chart:
```
helm dep up
helm install gxy-cvmfs galaxy-cvmfs-csi-helm/galaxy-cvmfs-csi/
```


## Reference repositories

The defaults configure `data.galaxyproject.org` and `idc.galaxyproject.org`,
including their server URLs and public signing keys. The node plugin receives
these files under `/etc/cvmfs/config.d`; both repositories are available through
its CVMFS automounter. Consumers can mount each repository from the same CSI
volume using its repository name as the subpath.

Galaxy's chart configures application/job mounts and loads IDC's data-table XML.
This chart configures the CVMFS client; it does not load Galaxy tables or
provision CVMFS on remote compute workers.

## Validation

```console
helm dependency build galaxy-cvmfs-csi
helm lint galaxy-cvmfs-csi
python -m pip install PyYAML
python -m unittest discover -s tests -v
```

## History

The original version of this chart has been PR-ed back to CERN:
https://github.com/cernops/cvmfs-csi/pull/3 This version now contains only
Galaxy specific customizations, and includes the CERN chart as a dependency.

This chart is used by the Galaxy Helm chart:
https://github.com/galaxyproject/galaxy-helm
