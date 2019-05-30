A Helm chart for the Galaxy project CVMFS to be mounted as a read-only file
system in Kubernetes environments.

## Use
To use, clone this repository and install the chart:
```
git clone https://github.com/CloudVE/galaxy-cvmfs-csi-chart
cd galaxy-cvmfs-csi-chart
helm install --name gxy-csi galaxy-cvmfs-csi-chart
```
This will install the necessary storage classes into the current namespace that
other charts/deployments can leverage to mount the CVMFS. For an example of how
this is used, take a look at the Galaxy Helm chart:
https://github.com/CloudVE/galaxy-kubernetes/tree/v3/galaxy

This chart has been tailored for use with the Galaxy project CVMFS. A generic
version of the chart can be found at https://github.com/cernops/cvmfs-csi/pull/3
