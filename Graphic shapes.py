import arcade

arcade.open_window(500,550," Graphic shapes")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
n= 10
m= 10   
for i in range(1 ,n+1):
    
    for j in range(1 , m+1):
        
        if (i+j) % 2 == 0:
            arcade.draw_circle_filled(i,j,arcade.color.RED)
        else :
            arcade.draw_circle_filled(i,j,arcade.color.BLUE)
    print()       

arcade.finish_render()
arcade.run()


