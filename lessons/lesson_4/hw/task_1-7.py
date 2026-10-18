# Блок 1: Рядки (str) — Валідація та нормалізація

raw_text = "cOnNeCt:192.168.1.1:8080\n"

stripped_text = raw_text.strip()
command, ip_address, port = stripped_text.split(":")
command = command.lower()
is_port_valid = port.isdigit()

parsed_text = ":".join((command, ip_address, port))

print('Port is valid' if is_port_valid else 'Port is invalid')
print('User input: ', parsed_text)

# Блок 2: Байти (bytes) — Серіалізація для мережі

encoded_ip = ip_address.encode()

# encoded_ip[0] = 2
# TypeError: 'bytes' object does not support item assignment
# In python bytes objects are immutable and can't be changed after creation

print('Ip as text bytes', encoded_ip)

# Блок 3: Масиви байтів (bytearray) — Модифікація пакета на льоту

incoming_package = bytearray([0, 0, 0, 0, 0])
incoming_package[0] = 0xAA
incoming_package[-1] = 0xFF

incoming_package.extend(encoded_ip)

print("Package:", incoming_package)
print("Package size:", len(incoming_package), "bytes")
# Блок 4: Списки (list) — Черга відправки даних

packet_queue = [command, encoded_ip, incoming_package]
packet_queue.insert(0, 'PING')

processed_packet = packet_queue.pop()

print("Proccessed: ", processed_packet)

# Блок 5: Кортежі (tuple) — Незмінний архів (Лог)

log_entry = (tuple(packet_queue), processed_packet)
# ^ This tuple can't be used as a key in the dict since
# all elements of the tuple should be hasbale themselves
# Since our tuple contains bytearray ( which is processed_packet ) which is mutable
# we can't use it as a key

# Блок 6: Типізовані масиви (array.array) — Економія пам'яті

import array

raw_ports = [80, 443, int(port)]
array_with_port = array.array('H', raw_ports)
print(array_with_port)

# array_with_port.append("8080")
# TypeError: 'str' object cannot be interpreted as an integer
# Array should take only digits

# Блок 7: Іменовані кортежі (collections.namedtuple) — Читабельність коду

from collections import namedtuple

Session = namedtuple("Session", ["command", "ip", "port", "status"])

session_results = Session(command=command, ip=ip_address, port=port, status="Active")

print(session_results)
print(f"{'IP: ':<10} {session_results.ip}")
print(f"{'STATUS: ':<10} {session_results.status}")
