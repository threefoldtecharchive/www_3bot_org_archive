from Jumpscale import j

class Package(j.baseclasses.threebot_package):
    """
    JSX> cl = j.servers.threebot.local_start_zerobot(background=False)
    JSX> cl = j.clients.gedis.get("abc", port=8901, package_name="zerobot.packagemanager")
    JSX> cl.actors.package_manager.package_add(git_url="https://github.com/threefoldtech/www_3bot_org/tree/3bot")
    """
    def start(self):
        server = self.openresty
        server.configure()
        for port in [80, 443]:
            website = server.get_from_port(port)
            website.domain = "3bot.org"
            locations = website.locations.get(f"3bot_locations_{port}")

            website_location = locations.locations_static.new()
            website_location.name = "3botwebsite"
            website_location.path_url = "/"
            fullpath = j.sal.fs.joinPaths(self.package_root, "html/")
            website_location.path_location = fullpath

            locations.configure()
            website.configure()
            website.save()
