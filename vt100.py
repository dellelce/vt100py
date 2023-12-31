"""Vt100 interface class.

Created:      100713
"""


class vt100(object):
    esc = chr(27)

    @classmethod
    def bold(self) -> str:
        return f"{self.esc}[1m"

    @classmethod
    def reset(self) -> str:
        return f"{self.esc}[0m"

    @classmethod
    def title(self, name=None) -> str:
        return f"{self.esc}];{name}{chr(7)}"

    @classmethod
    def cursor_pos(self, x=0, y=0) -> str:
        return f"{self.esc}[{x};{y}H"
