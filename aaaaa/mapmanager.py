# напиши здесь код создания и управления картой
class Mapmanager():
    def __init__(self):
        self.model = 'block'
        self.texsture = 'block.png'
        # self.block = loader.loadModel(self.model)
        # self.block.setTexsture(loader.loadTexsture(self.texsture))
        self.color = (0.2, 0.2, 0.35, 1)

        self.startNew()
        # self.addBlock((0, 10, 0))

    def startNew(self):
        self.land = render.attadhNewNode('Land')

    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexsture(loader.loadTexture(self.texsture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

    def clear(self):
        self.land.removeNode()
        self.startNew()
    
    def LoadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z)+1)
                        block = self.addBlock((x, y, z0))
                    x += 1
                y += 1

    def findBloks(self, pos):
        return self.land.findAllMatches("=at=" + str(pos))

    def isEmpty(self, pos):
        blocks = self.findBloks(pos)
        if blocks:
            return False
        else:
            return True

    def findHighestEmpty(self, pos):
        x, y, z = pos
        z = 1
        while not self.isEmpty((x,y,z)):
            z += 1
        return(x,y,z)

    def buildBlock(self, pos):
       """Ставим блок с учётом гравитации: """
       x, y, z = pos
       new = self.findHighestEmpty(pos)
       if new[2] <= z + 1:
           self.addBlock(new)
 
   def delBlock(self, position):
       """удаляет блоки в указанной позиции """
       blocks = self.findBlocks(position)
       for block in blocks:
           block.removeNode()
 
   def delBlockFrom(self, position):
       x, y, z = self.findHighestEmpty(position)
       pos = x, y, z - 1
       for block in self.findBlocks(pos):
               block.removeNode()
 
   def saveMap(self):
       blocks = self.land.getChildren()
       with open('my_map.dat', 'wb') as fout:
           pickle.dump(len(blocks), fout)
 
           for block in blocks:
               x, y, z = block.getPos()
               pos = (int(x), int(y), int(z))
               pickle.dump(pos, fout)
 
   def loadMap(self):
       self.clear()

       with open('my_map.dat', 'rb') as fin:

           length = pickle.load(fin)
 
           for i in range(length):
               pos = pickle.load(fin)
 
               # создаём новый блок
               self.addBlock(pos)