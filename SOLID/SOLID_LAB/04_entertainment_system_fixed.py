class EntertainmentDevice:

    def plug_device_in_power_outlet(self, power_outlet):
        pass


class HDMIConnection:

    def connect_via_hdmi(self, other):
        pass


class EthernetCableConnection:

    def connect_via_ethernet(self, other):
        pass


class RCACableConnection:

    def connect_via_rca(self, other):
        pass


class Television(EntertainmentDevice, HDMIConnection, EthernetCableConnection, RCACableConnection):

    def connect_to_dvd(self, dvd_player):
        self.connect_via_rca(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_via_hdmi(game_console)

    def plug_in_power(self, power_station):
        self.plug_device_in_power_outlet(power_station)


class DVDPlayer(EntertainmentDevice, HDMIConnection):
    def connect_to_tv(self, television):
        self.connect_via_hdmi(television)

    def plug_in_power(self, power_station):
        self.plug_device_in_power_outlet(power_station)


class GameConsole(EntertainmentDevice, HDMIConnection, EthernetCableConnection):
    def connect_to_tv(self, television):
        self.connect_via_hdmi(television)

    def connect_to_router(self, router):
        self.connect_via_ethernet(router)

    def plug_in_power(self, power_station):
        self.plug_device_in_power_outlet(power_station)


class Router(EntertainmentDevice, EthernetCableConnection):
    def connect_to_tv(self, television):
        self.connect_via_ethernet(television)

    def connect_to_game_console(self, game_console):
        self.connect_via_ethernet(game_console)

    def plug_in_power(self, power_station):
        self.plug_device_in_power_outlet(power_station)

