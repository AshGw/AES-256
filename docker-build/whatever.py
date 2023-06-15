from src.Ash import *
from src.AshTextCrypt import *




c = Enc('hello',Enc.genMainkey())
print(c.encToBytes())