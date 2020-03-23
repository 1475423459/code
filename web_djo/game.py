class Game(object):
    #类属性，历史最高分
    top_score = 0
    def __init__(self, player):
        self.player = player

    @staticmethod
    def show_help():
        print("帮助信息：僵尸进入大门")
    @classmethod
    def show_top_score(cls):
        print("历史最高分： %d" % cls.top_score)

    def start_game(self):
        print("%s 开始游戏。。。" % self.player)

#查看游戏帮助信息
Game.show_help()
#查看历史最高分
Game.show_top_score()
#创建游戏对象
game1 = Game("小米")
game1.start_game()