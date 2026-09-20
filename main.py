import arcade
from src.views.game_view import GameView
from src.views.ai_game_view import AiGameView
import argparse
from src.constant import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE


def main():
    parser = argparse.ArgumentParser(description="2D Racing AI Simulation Controller")

    parser.add_argument("--game", action="store_true", help="Launch manual player mode")
    parser.add_argument("--ai", action="store_true", help="Launch the best ai to play the game")
    
    args = parser.parse_args()

    if args.game:
        play_game()
    elif args.ai:
        best_ai()
    else:
        play_game()


def play_game():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.show_view(GameView())
    arcade.run()
    
def best_ai():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.show_view(AiGameView())
    arcade.run()


if __name__ == "__main__":
    main()
