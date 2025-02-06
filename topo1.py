from mininet.topo import Topo
class Topo1(Topo):
    def __init__(self):
        super().__init__(self)
        h1 = self.addHost('H1')
        h2 = self.addHost('H2')
        h3 = self.addHost('H3')
        h4 = self.addHost('H4')
        s1 = self.addSwitch('S1')
        s2 = self.addSwitch('S2')
        self.addLink(h1,s1)
        self.addLink(h2,s1)
        self.addLink(h3,s2)
        self.addLink(h4,s2)
        self.addLink(s1,s2)

topos = {'topo1':(lambda: Topo1())}
