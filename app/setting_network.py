#!/usr/bin/env python
# -*- coding: utf-8 -*-

import network
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    networkInfos = None
    button_dhcp = None
    button_setting_ip = None
    entry_ip = None
    entry_mask = None
    entry_gateway = None
    entry_dns = None

    def __init__(self):
        Gtk.Window.__init__(self, title = '网络设置')
        self.set_border_width(10)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)
        MainWindow.networkInfos = network.getNetworkInfo()
        grid = Gtk.Grid()
        grid.set_row_spacing(10)
        grid.set_column_spacing(20)
        self.page = Gtk.Box()
        self.page.set_border_width(20)
        self.notebook.append_page(self.page, Gtk.Label(MainWindow.networkInfos[0].get('id')))
        self.page.add(grid)
        MainWindow.button_dhcp = Gtk.RadioButton.new_with_label_from_widget(None, '自动获取IP地址')
        separator1 = Gtk.HSeparator()
        MainWindow.button_setting_ip = Gtk.RadioButton.new_with_mnemonic_from_widget(MainWindow.button_dhcp, '设置IP地址')
        lable_ip = Gtk.Label('IP地址：')
        MainWindow.entry_ip = Gtk.Entry()
        MainWindow.entry_ip.set_max_length(15)
        lable_mask = Gtk.Label('子网掩码：')
        MainWindow.entry_mask = Gtk.Entry()
        MainWindow.entry_mask.set_max_length(15)
        lable_gateway = Gtk.Label('默认网关：')
        MainWindow.entry_gateway = Gtk.Entry()
        MainWindow.entry_gateway.set_max_length(15)
        lable_dns = Gtk.Label('DNS：')
        MainWindow.entry_dns = Gtk.Entry()
        MainWindow.entry_dns.set_max_length(15)
        separator2 = Gtk.HSeparator()
        button_ok = Gtk.Button.new_with_label('确定')
        button_cancel = Gtk.Button.new_with_label('取消')
        grid.attach(MainWindow.button_dhcp, 0, 0, 3, 1)
        grid.attach(separator1, 0, 1, 3, 1)
        grid.attach(MainWindow.button_setting_ip, 0, 2, 3, 1)
        grid.attach(lable_ip, 0, 3, 1, 1)
        grid.attach(MainWindow.entry_ip, 1, 3, 2, 1)
        grid.attach(lable_mask, 0, 4, 1, 1)
        grid.attach(MainWindow.entry_mask, 1, 4, 2, 1)
        grid.attach(lable_gateway, 0, 5, 1, 1)
        grid.attach(MainWindow.entry_gateway, 1, 5, 2, 1)
        grid.attach(lable_dns, 0, 6, 1, 1)
        grid.attach(MainWindow.entry_dns, 1, 6, 2, 1)
        grid.attach(separator2, 0, 7, 3, 1)
        grid.attach(button_ok, 1, 8, 1, 1)
        grid.attach(button_cancel, 2, 8, 1, 1)

        #if MainWindow.networkInfos[0].get('method') == 'manual':
        if not MainWindow.networkInfos[0].get('is_auto'):
            MainWindow.button_setting_ip.set_active(True)
            MainWindow.entry_ip.set_text(MainWindow.networkInfos[0].get('ip'))
            MainWindow.entry_mask.set_text(MainWindow.networkInfos[0].get('subnet_mask'))
            MainWindow.entry_gateway.set_text(MainWindow.networkInfos[0].get('gateway'))
            MainWindow.entry_dns.set_text(MainWindow.networkInfos[0].get('dns'))
        else:
            MainWindow.entry_ip.set_editable(False)
            MainWindow.entry_mask.set_editable(False)
            MainWindow.entry_gateway.set_editable(False)
            MainWindow.entry_dns.set_editable(False)

        MainWindow.button_dhcp.connect("toggled", self.on_button_toggled, 'dhcp')
        MainWindow.button_setting_ip.connect("toggled", self.on_button_toggled, 'setting_ip')
        button_ok.connect("clicked", self.on_button_ok_clicked)
        button_cancel.connect("clicked", self.on_button_cancel_clicked)

    def on_button_toggled(self, button, name):
        print name
        if name == 'dhcp':
            MainWindow.entry_ip.set_text('')
            MainWindow.entry_mask.set_text('')
            MainWindow.entry_gateway.set_text('')
            MainWindow.entry_dns.set_text('')
            MainWindow.entry_ip.set_editable(False)
            MainWindow.entry_mask.set_editable(False)
            MainWindow.entry_gateway.set_editable(False)
            MainWindow.entry_dns.set_editable(False)
        else:
            #if MainWindow.networkInfos[0].get('method') == 'manual':
            if not MainWindow.networkInfos[0].get('is_auto'):
                MainWindow.entry_ip.set_text(MainWindow.networkInfos[0].get('ip'))
                MainWindow.entry_mask.set_text(MainWindow.networkInfos[0].get('subnet_mask'))
                MainWindow.entry_gateway.set_text(MainWindow.networkInfos[0].get('gateway'))
                MainWindow.entry_dns.set_text(MainWindow.networkInfos[0].get('dns'))
            MainWindow.entry_ip.set_editable(True)
            MainWindow.entry_mask.set_editable(True)
            MainWindow.entry_gateway.set_editable(True)
            MainWindow.entry_dns.set_editable(True)
        '''if button.get_active():
            state = 'on'
        else:
            state = 'off'
        print state'''

    def on_button_ok_clicked(self, button):
        if MainWindow.button_dhcp.get_active():
            network.setDHCP(MainWindow.networkInfos[0].get('id'), MainWindow.networkInfos[0].get('mac'))
        else:
            self.ip = MainWindow.entry_ip.get_text()
            self.mask = MainWindow.entry_mask.get_text()
            self.gateway = MainWindow.entry_gateway.get_text()
            self.dns = MainWindow.entry_dns.get_text()
            #print self.ip, self.mask, self.gateway, self.dns
            if self.ip and self.mask and self.gateway and self.dns and network.isIP(self.ip) and network.isIP(self.mask) and network.isIP(self.gateway) and network.isIP(self.dns):
                network.setNetwork(MainWindow.networkInfos[0].get('id'), MainWindow.networkInfos[0].get('mac'), self.ip, self.mask, self.gateway, self.dns)
            else:
                print 'address error!'
        Gtk.main_quit()

    def on_button_cancel_clicked(self, button):
        Gtk.main_quit()

def main():
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == '__main__':
    main()
