class Gun:
    #添加属性
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0
    #添加子弹函数
    def add_bullet(self, count):
        self.bullet_count += count
    #枪可以射击
    def shoot(self):
        if self.bullet_count <= 0:
            print("%s，该枪没有子弹，请添加子弹" % self.model)
            return
        self.bullet_count -= 1
        print("%s,射击后还剩子弹数 %d" % (self.model, self.bullet_count))
class Slodier:
    def __init__(self,name):
        self.name = name
        self.gun = None
    def fire(self):
        #若没有枪
        if self.gun is None:
            print("%s 士兵没有抢，请教官配备一把枪" % self.name)
            return
        #若有枪高喊口号
        print("%s 有把 %s 枪，冲啊" % (self.name, self.gun.model))

        #装子弹
        self.gun.add_bullet(50)

        #射击
        self.gun.shoot()

gun = Gun("AK47")
slodier = Slodier("许三多")
slodier.gun = gun
slodier.fire()
