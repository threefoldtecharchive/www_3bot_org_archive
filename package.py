from Jumpscale import j


class Package(j.baseclasses.threebot_package):
    """
    JSX> cl = j.servers.threebot.local_start_zerobot(background=False)
    JSX> cl = j.clients.gedis.get("abc", port=8901, package_name="zerobot.packagemanager")
    JSX> cl.actors.package_manager.package_add(git_url="https://github.com/threefoldtech/www_3bot_org/tree/3bot")
    """
    DOMAIN = "3bot.org"
    def start(self):
        server = self.openresty
        server.configure()
        website_3bot = server.websites.get("self.name")
        website_3bot.domain = self.DOMAIN
        website_3bot.port = 80
        website_3bot.ssl = False

        websites = [server.get_from_port(80), server.get_from_port(443), website_3bot]
        for website in websites:
            locations = website.locations.get(f"threebot_locations_{website.name}")

            website_location = locations.locations_static.new()
            website_location.name = f"{self.name}_location"
            website_location.path_url = "/" if website.domain == self.DOMAIN else f"/{self.name}"
            fullpath = j.sal.fs.joinPaths(self.package_root, "html/")
            website_location.path_location = fullpath

            locations.configure()
            website.configure()
            website.save()
