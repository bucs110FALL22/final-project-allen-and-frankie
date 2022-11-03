
# Final Project Milestone II

*Place this document in your final project repo folder `/etc`. *

***

Come up with interfaces for 3 possible classes you think you may need for your project. Again, brainstorm a little. Nothing is *wrong*.

## class Player
  1. 
  
  attributes:
    - name
    - health
    - major: affects stats like speed, health
    - image
    - speed

  methods:
    - jump()
    - attack()
    - move_left()
    
## class Bearcat

 i. attributes 
   - health
   - speed 
   - image
   - x coordinate
   - y coordinate
   - damage dealt: to player
  ii. methods
   - attack_player()
   - location_chk()
   - walk()
   - jump()


## class River

  attributes:
    - image
    - depth
    - width
    - speed
    - distance to bridge: alternate option
  methods
    - damage_player()
    - increase_depth()