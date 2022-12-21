A Helm chart for installing the [CVMFS-CSI driver[(https://github.com/cvmfs-contrib/cvmfs-csi/tree/master/deployments/helm),
with Galaxy specific repositories preconfigured.

History
-------
The original version of this chart has been PR-ed back to CERN: https://github.com/cernops/cvmfs-csi/pull/3
This version now contains only Galaxy specific customizations, and includes the CERN chart as a dependency.

This chart is used by the Galaxy Helm chart:
https://github.com/galaxyproject/galaxy-helm


## Use

To use, clone this repository and install the chart:
```
git clone https://github.com/CloudVE/galaxy-cvmfs-csi-helm
```
Helm v3 Installation:
```
helm install gxy-cvmfs galaxy-cvmfs-csi-helm/galaxy-cvmfs-csi/
```
