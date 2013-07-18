pkguninstaller
==============

Uninstall packages using StarCluster from an Ubuntu EC2 cluster. To use, copy the pkguninstaller.py
into your plugins directory. Configuration looks like this

```
# Use this plugin to uninstall one or more packages on all nodes
[plugin pkguninstaller]
SETUP_CLASS = pkguninstaller.PackageUninstaller
# list of comma-separated apt-get installable packages 
PACKAGES = hadoop-0.20
```


