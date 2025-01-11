# Leetcode: https://leetcode.com/problems/validate-ip-address/

from typing import List


class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        ip = queryIP.split(".")
        if len(ip) == 4:

            return self.check_valid_ipv4(ip)

        ip = queryIP.split(":")
        if len(ip) == 8:

            return self.check_valid_ipv6(ip)

        return "Neither"

    def check_valid_ipv4(self, ip: List[str]) -> None:

        for sub_ip in ip:

            if len(sub_ip) > 1 and sub_ip[0] == "0":
                return "Neither"
            if not sub_ip.isnumeric():
                return "Neither"
            if int(sub_ip) < 0 or int(sub_ip) > 255:
                return "Neither"
        return "IPv4"

    def check_valid_ipv6(self, ip: List[str]) -> None:

        valid_char = set(["a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"])
        for sub_ip in ip:

            if len(sub_ip) < 1 or len(sub_ip) > 4:
                return "Neither"
            for char in sub_ip:
                if char.isalpha() and char not in valid_char:
                    return "Neither"
        return "IPv6"
