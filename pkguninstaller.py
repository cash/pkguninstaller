from starcluster import clustersetup
from starcluster.logger import log


class PackageUninstaller(clustersetup.DefaultClusterSetup):
    """
    This plugin uninstalls Ubuntu packages on all nodes in the cluster. The
    packages are specified in the plugin's config:

    [plugin pkguninstaller]
    setup_class = pkguninstaller.PackageUninstaller
    packages = hadoop-0.20
    """
    def __init__(self, packages=None):
        super(PackageUninstaller, self).__init__()
        self.packages = packages
        if packages:
            self.packages = [pkg.strip() for pkg in packages.split(',')]

    def run(self, nodes, master, user, user_shell, volumes):
        if not self.packages:
            log.info("No packages specified!")
            return
        log.info('Uninstalling the following packages on all nodes:')
        log.info(', '.join(self.packages), extra=dict(__raw__=True))
        pkgs = ' '.join(self.packages)
        for node in nodes:
            self.pool.simple_job(node.apt_install, (pkgs), jobid=node.alias)
        self.pool.wait(len(nodes))

    def on_add_node(self, new_node, nodes, master, user, user_shell, volumes):
        log.info('Uninstalling the following packages on %s:' % new_node.alias)
        pkgs = ' '.join(self.packages)
        new_node.apt_command('remove %' % pkgs)

    def on_remove_node(self, node, nodes, master, user, user_shell, volumes):
        raise NotImplementedError("on_remove_node method not implemented")

