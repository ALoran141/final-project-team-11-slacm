import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.obstacle import Obstacle

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the frog collides
    with the coins, or the frog collides with the obstacles, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_coin_collision(cast)
            self._handle_obstacle_collision(cast)
            self._handle_game_over(cast)

    def _handle_coin_collision(self, cast):
        """Updates the score and moves the coin if the frog collides with the coin.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        coin = cast.get_first_actor("coins")
        frog = cast.get_first_actor("frogs")


        if frog.get_position().equals(coin.get_position()):
            points = coin.get_points()
            score.add_points(points)
            coin.reset()
    
    def _handle_obstacle_collision(self, cast):
        """Sets the game over flag if the frog collides with one of the obstacles.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        frog = cast.get_first_actor("frogs")
        obstacle = cast.get_first_actor("obstacles")

        if frog.get_position().equals(obstacle.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        pass