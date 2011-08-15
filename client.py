#-*-coding:Utf-8 -*

#    TheSecretTower
#    Copyright (C) 2011 Pierre SURPLY
#
#    This file is part of TheSecretTower.
#
#    TheSecretTower is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    TheSecretTower is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with TheSecretTower.  If not, see <http://www.gnu.org/licenses/>.

# Auteur : Pierre Surply

import socket

import const
import map
from perso import *

def connect():
    stop = False
    id_last_event = 0
    tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 
    try:
        tcp.connect((const.host,const.port))
        for i in const.input:
            send(tcp,i);
            const.input = []
        const.input = []
    except socket.error:
        const.output = const.host+":"+str(const.port)+" : Connection Refused"
    else:
        if const.input_udp != "":
            send_udp(udp,const.input_udp)
            const.input_udp = ""
        const.output = "Connected"
        send(tcp, "get_perso")
        send(tcp, "get_map")
        id_last_event = send(tcp, "get_last_event")
        while const.runned:
            for i in const.input:
                send(tcp,i);
                const.input = []
            if const.input_udp != "":
                send_udp(udp,const.input_udp)
                const.input_udp = ""

            send_udp(udp, "get_pos", tcp)
            id_last_event = send(tcp,"get_event;"+str(id_last_event));

        

def send_udp(sock, cmd, tcp=None):
    sock.sendto(cmd, (const.host, const.port))
    buffer = sock.recv(2048)

    if cmd == "get_pos":
        for i in buffer.split("\n"):
            if i != " " and i != "":
                found = False
                nom = i.split(";")[0]
                for perso in const.persos:
                    if perso.nom == nom:
                        found = True  
                        char_perso = i.split(";")
                        perso.map = int(char_perso[1])
                        perso.x = int(char_perso[2])
                        perso.y = int(char_perso[3])
                        perso.v_x = int(char_perso[4])
                        perso.v_y = int(char_perso[5])
                        perso.sens = bool(int(char_perso[6]))
                        perso.isingrav = bool(int(char_perso[7]))
                        perso.hitting = bool(int(char_perso[8]))
                        perso.fired = bool(int(char_perso[9]))

                if not found:
                    send(tcp, "get_perso")
            
def send(sock, cmd):
    sock.send(cmd)
    buffer = sock.recv(4096)

    if cmd == "get_perso":
        for i in buffer.split("\n"):
            if i != " ":
                found = False
                nom = i.split(";")[0]
                for perso in const.persos:
                    if perso.nom == nom:
                        found = True
                if not found:
                    new_perso = Perso()
                    new_perso.ctlr = False
                    char_perso = i.split(";")
                    new_perso.nom = char_perso[0]
                    new_perso.map = int(char_perso[1])
                    new_perso.id_porte = int(char_perso[2])
                    new_perso.vie = int(char_perso[3])
                    new_perso.fired = bool(int(char_perso[4]))
                    new_perso.inv.load(char_perso[5])
                    new_perso.inv.item_sel = int(char_perso[6])
                    for nbr in range(5):
                        new_perso.char2color(char_perso[nbr+7], nbr)
                    new_perso.update_color()
                    const.persos.append(new_perso)
    if cmd == "get_map":
        const.map = map.char2map(buffer, True) 

    if cmd == "get_last_event":
        return int(buffer)

    if cmd.split(";")[0] == "get_event":
        buffer = buffer.split("\n")
        id_last_event = buffer[0]
        buffer.remove(id_last_event)
        if buffer != [""]:
            print buffer
            const.events.extend(buffer)
        return id_last_event
    return True

