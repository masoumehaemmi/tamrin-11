import random
import arcade

class Apple(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init(self)
        self.image = 'apple.jpg'
        self.pear = arcade.Sprite(self.image, 0.1)
        self.pear.center_x = random.randint(25, w + 5)
        self.pear.center_y = random.randint(25, h + 5)

    def draw(self):
        arcade.apple.draw()
    
class Snake(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color = arcade.color.RED
        self.speed = 4
        self.width = 16
        self.height = 16
        self.center_x = w // 2
        self.center_y = h // 2
        self.r=8
        self.change_x = 0
        self.change_y = 0
        self.score = 0
        self.body =[]
        self.body.append([self.center_x,self.center_y])


    def draw(self):
        for i in range(len(self.body)):
            arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)

    def move(self):
        for i in range(len(self.body)):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][0] = self.body[i-1][1]

        self.center_x += self.speed * self. change_x
        self.center_y += self.speed * self. change_y

        if self.body:
            self.body[0][0] += self.speed *self.change_x
            self.body[0][1] += self.speed * self.change_y
    def eat(self,food):
        if food == "thorn":
            self.score -=1
            self.body.pop()
        elif food == "apple":
            self.score += 1
            self.body.append(self.body[len(self.body)+1])
        elif food == "pear":
            self.body += 2
            self.body.append(self.body[len(self.body)+2])

class Pear(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.image = 'pear.jpg'
        self.pear = arcade.Sprite(self.image, 0.1)
        self.pear.center_x = random.randint(25, w + 5)
        self.pear.center_y = random.randint(25, h + 5)

    def draw(self):
        self.pear.draw()        

class Thorn(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.img = 'thron.jpg'
        self.thorn = arcade.Sprite(self.img, 0.1)
        self.thorn.center_x = random.randint(25, w + 5)
        self.thorn.center_y = random.randint(25, h + 5)

    def draw(self):
        self.thorn.draw()

class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self,self.width,self.height,"python snake")
        arcade.set_background_color(arcade.color.BLUE)
        self.Snake = Snake(500,550)
        self.apple = Apple(500,550)

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()

    def on_update(self,delta_time :float):
        self.Snake.move()
        if arcade.check_for_collision(self.snake, self.pear):
            self.Snake.eat("pear")
            self.pear = Pear(500,550)
            print(self.snake.score)
        elif arcade.check_for_collision(self.snake, self.apple):
            self.Snake.eat("apple")
            self.apple = Apple(500,550)
            print(self.snake.score)

        elif arcade.check_for_collision(self.snake, self.thorn):
            self.Snake.eat("thorn")
            self.thorn = Thorn(500,550)
            print(self.snake.score)

    def on_key_release(self, key, modifires):
        
        if key == arcade.key.RIGHT:
            self.Snake.change_x = 1
            self.Snake.change_y= 0

        elif key == arcade.key.UP:
            self.Snake.change_x = 0
            self.Snake.change_y= 1

        elif key == arcade.key.LEFT:
            self.Snake.change_x = -1
            self.Snake.change_y= 0

        elif key == arcade.key.DOWN:
            self.Snake.change_x = 0
            self.Snake.change_y= -1

        else:
            print(" input not key")
        



game=Game()
arcade.run()