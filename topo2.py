from mininet.topo import Topo
class Topo2(Topo):
    def __init__(self):
        super().__init__(self)
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        self.addLink(h1,s1,bw=20,delay='5ms')
        self.addLink(h2,s1,bw=1000,delay='50ms')
        self.addLink(h3,s2,bw=1000,delay='1ms')
        self.addLink(h4,s2,bw=20,delay='30ms')
        self.addLink(h5,s3,bw=50000,delay='1ms')
        self.addLink(s1,s2,bw=100000,delay='1ms')
        self.addLink(s2,s3,bw=10000,delay='1ms')

topos = {'topo2':(lambda: Topo2())}
